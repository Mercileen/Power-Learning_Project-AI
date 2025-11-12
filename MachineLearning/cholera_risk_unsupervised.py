# ==========================================================
# 🌍 Cholera Outbreak Risk Detection using Unsupervised Learning (SDG 3)
# ----------------------------------------------------------
# Tools: Python, Pandas, Scikit-learn, Matplotlib, Seaborn
# Goal: Identify high-risk regions for cholera outbreaks
# ==========================================================

# === 1. Import Libraries ===
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

print("✅ Libraries loaded successfully!")

# === 2. Load Data ===
# NOTE: Replace file names below with your dataset paths or URLs
cholera = pd.read_csv('cholera_cases.csv')
water = pd.read_csv('water_access.csv')
sanitation = pd.read_csv('sanitation.csv')
health = pd.read_csv('health_expenditure.csv')

print("✅ Data loaded successfully!")
print(cholera.head())

# === 3. Merge & Clean Data ===
df = cholera.merge(water, on=['Country', 'Year'], how='left') \
             .merge(sanitation, on=['Country', 'Year'], how='left') \
             .merge(health, on=['Country', 'Year'], how='left')

df = df.dropna()
print(f"✅ Dataset shape after cleaning: {df.shape}")

# === 4. Select Features for Clustering ===
features = [
    'Water_Access_%',
    'Sanitation_%',
    'Health_Exp_perCapita',
    'Population_Density',
    'Cholera_Cases'
]

X = df[features]

# === 5. Normalize Data ===
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("✅ Data normalized successfully!")

# === 6. Find Optimal K (Elbow Method) ===
inertia = []
K = range(1, 10)

for k in K:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X_scaled)
    inertia.append(km.inertia_)

plt.figure(figsize=(8,5))
plt.plot(K, inertia, marker='o')
plt.xlabel('Number of clusters k')
plt.ylabel('Inertia')
plt.title('Elbow Method – Optimal k')
plt.show()

# === 7. Train Model with K-Means ===
k_opt = 3  # You can change based on the Elbow Plot
kmeans = KMeans(n_clusters=k_opt, random_state=42)
clusters = kmeans.fit_predict(X_scaled)
df['Cluster'] = clusters

print("✅ Clustering complete! Sample results:")
print(df[['Country', 'Year', 'Cluster']].head())

# === 8. Visualize Clusters using PCA ===
pca = PCA(2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(8,6))
sns.scatterplot(x=X_pca[:,0], y=X_pca[:,1], hue=clusters, palette='viridis', s=100)
plt.title('Cholera Risk Clusters (PCA Visualization)')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.show()

# === 9. Save Clustered Data ===
df.to_csv('cholera_risk_clusters.csv', index=False)
print("💾 Clustered dataset saved as 'cholera_risk_clusters.csv'")
