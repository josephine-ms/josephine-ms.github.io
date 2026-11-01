"""Reproducible telecom churn baseline comparison based on the portfolio notebook."""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline
from xgboost import XGBClassifier
ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "outputs"
OUTPUT.mkdir(exist_ok=True)
df = pd.read_csv(ROOT / "data" / "telco_customer_churn.csv")
assert {"Churn", "customerID", "TotalCharges", "Contract", "tenure"}.issubset(df.columns)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["Churn"] = df["Churn"].map({"No": 0, "Yes": 1})
df = df.drop(columns=["customerID"])
df["TenureGroup"] = pd.cut(df["tenure"], bins=[-1,12,24,48,60,72], labels=["0-12","13-24","25-48","49-60","61-72"]).astype(str)
def payment_category(v):
    if "automatic" in v.lower(): return "Automatic"
    if v == "Electronic check": return "Electronic Check"
    return "Mailed Check"
df["PaymentCategory"] = df["PaymentMethod"].apply(payment_category)
X, y = df.drop(columns=["Churn"]), df["Churn"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2,stratify=y,random_state=42)
nums=X.select_dtypes(include=["number"]).columns.tolist()
cats=X.select_dtypes(exclude=["number"]).columns.tolist()
pre=ColumnTransformer([("num",Pipeline([("imputer",SimpleImputer(strategy="median")),("scale",StandardScaler())]),nums),("cat",Pipeline([("imputer",SimpleImputer(strategy="most_frequent")),("encode",OneHotEncoder(handle_unknown="ignore",sparse_output=False))]),cats)])
models={
 "Dummy Baseline": Pipeline([("preprocess",pre),( "model",DummyClassifier(strategy="most_frequent"))]),
 "Logistic Regression": ImbPipeline([("preprocess",pre),("smote",SMOTE(random_state=42)),("model",LogisticRegression(max_iter=2000,solver="liblinear",random_state=42))]),
 "Random Forest": ImbPipeline([("preprocess",pre),("smote",SMOTE(random_state=42)),("model",RandomForestClassifier(n_estimators=200,max_depth=12,min_samples_leaf=2,random_state=42,n_jobs=1))]),
 "XGBoost": ImbPipeline([("preprocess",pre),("smote",SMOTE(random_state=42)),("model",XGBClassifier(n_estimators=300,learning_rate=.05,max_depth=4,subsample=.85,colsample_bytree=.85,eval_metric="logloss",random_state=42,n_jobs=1))])}
rows=[]
for name,model in models.items():
 print("Training",name,flush=True)
 model.fit(X_train,y_train)
 pred=model.predict(X_test); prob=model.predict_proba(X_test)[:,1]
 rows.append({"Model":name,"Accuracy":accuracy_score(y_test,pred),"Precision":precision_score(y_test,pred,zero_division=0),"Recall":recall_score(y_test,pred,zero_division=0),"F1":f1_score(y_test,pred,zero_division=0),"ROC_AUC":roc_auc_score(y_test,prob)})
 if name=="Random Forest":
  features=model.named_steps["preprocess"].get_feature_names_out()
  imp=pd.DataFrame({"feature":features,"importance":model.named_steps["model"].feature_importances_}).sort_values("importance",ascending=False)
  imp.to_csv(OUTPUT/"random_forest_feature_importance.csv",index=False)
results=pd.DataFrame(rows);results.to_csv(OUTPUT/"model_metrics.csv",index=False)
contracts=df.groupby("Contract")["Churn"].agg(["mean","count"]);contracts.to_csv(OUTPUT/"churn_by_contract.csv")
ax=contracts["mean"].mul(100).sort_values(ascending=False).plot.bar(figsize=(8,5));ax.set_ylabel("Churn rate (%)");ax.set_title("Churn rate by contract type");plt.tight_layout();plt.savefig(OUTPUT/"churn_by_contract.png",dpi=160);plt.close()
print("Rows:",len(df),"Churned:",int(y.sum()));print(results.round(4).to_string(index=False));print("Outputs:",OUTPUT)
