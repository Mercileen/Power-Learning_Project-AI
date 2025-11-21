from sklearn datasets import load_iris       			# Provides access to several machine learning datasets including Iris.
from sklearn.model_selection import train_test_split 		 # Splits the data into training and testing sets.
from sklearn.preprocessing import StandardScaler, LabelEncoder  # Standardizes features by removing the mean and scaling to unit variance.
from sklearn.tree import DecisionTreeClassifier 		# for classification problems
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np						# for numerical operations 
import joblib							# for lightweight pipelining and parallel processing

# 1. Load the Iris Dataset.
iris = load_iris()

# separate the data features
X = iris.data                    
# labels (already encoded 0,1,2)
y = iris.target                  
# species names
label_names = iris.target_names  

# 2. Handle Missing Values,encode labels
# Replace any NaN values with the mean of that column
X = np.nan_to_num(X, nan=np.nanmean(X))

# 3. Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Train–Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# 5. Train Decision Tree
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 6. Predictions
y_pred = model.predict(X_test)

# 7. Evaluation
print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred, target_names=label_names))

print("\n=== Confusion Matrix ===")
print(confusion_matrix(y_test, y_pred))

# 8. Save Model & Preprocessing Artifacts
joblib.dump(model, "iris_decision_tree_model.pkl")
joblib.dump(scaler, "iris_scaler.pkl")
print("\nModel and preprocessing")
