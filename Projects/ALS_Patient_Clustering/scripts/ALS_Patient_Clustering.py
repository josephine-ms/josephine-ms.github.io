"""ALS Patient Clustering Analysis."""
# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.environ["OMP_NUM_THREADS"] = "9"
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
from IPython.display import display, HTML

# 1.Load the ALS dataset
display(HTML("<h3 style='font-weight:bold;'>Step 1: Load ALS Dataset</h3>"))
from pathlib import Path
data_path = Path(__file__).resolve().parents[1] / "data/raw/als_data.csv"
df = pd.read_csv(data_path)
display(HTML("<b>First 5 Rows of the Dataset</b>"))
display(df.head())
display(HTML("<b>Dataset Structure and Data Types</b>"))
df.info()
display(HTML("<b>Summary Statistics</b>"))
display(df.describe())

# 2.Remove any data that is not relevant to the patient’s ALS condition
"""
Clustering aims to group patients based on similarities in ALS related clinical characteristics. SubjectID is a unique identifier and does not
not contain clinical meaning. Including it would distort distance calculations and bias cluster formation. 
"""
display(HTML("<h3 style='font-weight:bold;'>Step 2: Remove non-relevant variables</h3>"))
columns_to_drop = ['SubjectID']
df_clean = df.drop(columns=columns_to_drop)
print("Remaining columns used for clustering:")
display(df_clean.columns.tolist())
display(HTML(f"<b>Dataset shape after removal:</b> {df_clean.shape}")) 
display(HTML("<b>First 5 Rows of the cleaned Dataset</b>"))
display(df_clean.head())

# 3. Apply a standard scalar to the data
display(HTML("<h3><b>Step 3: Standardize the data</b></h3>"))
"""
K-means clustering relies on Euclidean distance. Variables measured on larger numeric scales would dominate distance calculations if the data
were left unscaled. Standardization ensures each feature contributes equally to the clustering process.
"""
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df_clean)
scaled_df = pd.DataFrame(scaled_data, columns=df_clean.columns)
display(HTML("<b>First 5 Rows of Standardized Data</b>"))
display(scaled_df.head())
display(HTML("<b>Feature Means After Standardization</b>"))
display(scaled_df.mean().to_frame("Mean"))
display(HTML("<b>Feature Standard Deviations After Standardization</b>"))
display(scaled_df.std().to_frame("Std Dev"))

# 4. Create a plot of the cluster silhouette score versus the number of clusters in a K-means cluster
display(HTML("<h3><b>Step 4: Compute silhouette scores</b></h3>"))
"""
Silhouette score evaluates how well data points fit within the assigned clusters.
"""
silhouette_scores = []
k_range = range(2, 11)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(scaled_df)
    score = silhouette_score(scaled_df, labels)
    silhouette_scores.append(score)
silhouette_df = pd.DataFrame({
    "Number of Clusters (k)": list(k_range),
    "Silhouette Score": silhouette_scores
})
display(HTML("<b>Silhouette Scores for Different Cluster Sizes</b>"))
display(silhouette_df)

# 4.1 Create a plot of the cluster silhouette score versus the number of clusters in a K-means cluster
display(HTML("<h3><b>Step 4.1: Plot silhouette score vs number of clusters</b></h3>"))
"""
Visualizing silhouette scores allows to clearly see where cluster quality peaks or stabilizes
"""
plt.figure(figsize=(8, 5))
plt.plot(k_range, silhouette_scores, marker='o')
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Silhouette Score")
plt.title("Silhouette Score vs Number of Clusters")
plt.grid(True)
plt.show()

# 5. Fit a K-means model to the data with the optimal number of clusters chosen in part (4).
display(HTML("<h3><b>Step 5: Fit Final K-Means Model</b></h3>"))
"""
The final K-means model assigns each patient to one of the two clusters, allowing subgroup-level analysis of ALS characteristics.
"""
optimal_k = 2
kmeans_final = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
clusters = kmeans_final.fit_predict(scaled_df)
scaled_df['Cluster'] = clusters
display(HTML("<b>Number of Observations per Cluster</b>"))
display(scaled_df['Cluster'].value_counts().to_frame("Count"))

# 6. Fit a PCA transformation with two features to the scaled data..
display(HTML("<h3><b>Step 6: Fit a PCA transformation with two features.</b></h3>"))
"""
The dataset contains many variables, making visualization difficult. PCA compresses the data into two components while preserving the most
important variance for visual inspection.
"""
pca = PCA(n_components=2)
pca_data = pca.fit_transform(scaled_df.drop(columns='Cluster'))
explained_variance = pd.DataFrame({
    "Principal Component": ["PC1", "PC2"],
    "Explained Variance Ratio": pca.explained_variance_ratio_
})
display(HTML("<b>Explained Variance by PCA Components</b>"))
display(explained_variance)
display(HTML(
    f"<b>Total Variance Explained:</b> "
    f"{np.sum(pca.explained_variance_ratio_):.2f}"
))
pca_df = pd.DataFrame(
    pca_data,
    columns=['Principal Component 1', 'Principal Component 2']
)
pca_df['Cluster'] = clusters

# 7. Make a scatterplot the PCA transformed data coloring each point by its cluster value.
display(HTML("<h3><b>Step 7: PCA Cluster Visualization</b></h3>"))
"""
Visual confirmation helps validate whether numerical clustering results reflect meaningful separation in reduced dimensions.
"""
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=pca_df,
    x='Principal Component 1',
    y='Principal Component 2',
    hue='Cluster',
    palette='Set2'
)
plt.title("PCA Visualization of ALS Patient Clusters")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend(title="Cluster")
plt.show()