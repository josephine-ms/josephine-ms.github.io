"""U.S. retail sales trend forecasting and holdout evaluation."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from IPython.display import display, HTML

display(HTML("<h3 style='font-weight:bold;'>1. Load the retail Dataset & Plot the data</h3>"))

from pathlib import Path

data_path = Path(__file__).resolve().parents[1] / "data/raw/us_retail_sales.csv"
df = pd.read_csv(data_path)
display(HTML("<b>First 5 Rows of the Dataset:</b>"))
display(df.head())

df_long = df.melt(
    id_vars=["YEAR"],           
    var_name="Month",           
    value_name="Retail_Sales")
df_long["Date"] = pd.to_datetime(
    df_long["YEAR"].astype(str) + "-" + df_long["Month"],
    format="%Y-%b"
)
df_long = df_long.sort_values("Date")
df_long = df_long[["Date", "Retail_Sales"]]

df_display = df_long.copy()
df_display.columns = ["Date", "Retail Sales"]
display(HTML("<b>Reshaped Monthly Time Series (first 5 rows):</b>"))
display(df_display.head())

display(HTML("<b>Graph:</b>"))
plt.figure(figsize=(9,5))
plt.plot(df_long["Date"], df_long["Retail_Sales"])
plt.title("US Monthly Retail Sales Over Time (Jan 1992-Jun 2021) ")
plt.xlabel("Date")
plt.ylabel("Retail Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

display(HTML("<h3 style='font-weight:bold;'>2. Split data into a training and test set </h3>"))

df_long.set_index("Date", inplace=True)
train = df_long[df_long.index < "2020-07-01"]
test = df_long[
    (df_long.index >= "2020-07-01") &
    (df_long.index <= "2021-06-30")]

display(HTML("<br>"))
display(HTML(f"<b>Training set size:</b> {len(train)}"))
display(HTML(f"<b>Test set size:</b> {len(test)}"))

display(HTML("<h3 style='font-weight:bold;'>3. Build Predictive Model using train data</h3>"))

train = train.copy()
test = test.copy()

train["Time_Index"] = np.arange(len(train))
test["Time_Index"] = np.arange(len(train), len(train) + len(test))

X_train = train[["Time_Index"]]
y_train = train["Retail_Sales"]

model = LinearRegression()
model.fit(X_train, y_train)

display(HTML("<br>"))
display(HTML("<b>Model Parameters:</b>")) 
display(HTML(f"<b>Intercept:</b> {round(model.intercept_,2)}"))
display(HTML(f"<b>Slope (monthly growth rate):</b> {round(model.coef_[0],2)}"))

display(HTML("<h3 style='font-weight:bold;'>4. Predict monthly retail sales on test period</h3>"))

X_test = test[["Time_Index"]]
y_test = test["Retail_Sales"]

predictions = model.predict(X_test)

display(HTML("<br>"))
display(HTML("<b>Graph:</b>"))
plt.figure()
plt.plot(test.index, y_test, label="Actual Sales")
plt.plot(test.index, predictions, label="Predicted Sales")
plt.title("Actual vs Predicted Retail Sales (Test data)")
plt.xlabel("Date")
plt.ylabel("Retail Sales")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

results = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": predictions
}).round(2)

display(HTML("<b>First 5 Actual vs Predicted (Rounded to 2 Decimals):</b>"))
display(results.head())

display(HTML("<h3 style='font-weight:bold;'>5. Report the RMSE of the model predictions on the test set</h3>"))

rmse = np.sqrt(mean_squared_error(y_test, predictions))

display(HTML("<br>"))
display(HTML(f"<b>Root Mean Squared Error (RMSE):</b> {round(rmse,2)}"))
