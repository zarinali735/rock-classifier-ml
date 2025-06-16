import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import numpy as np

# Load and clean data
df = pd.read_csv("C:/Users/HP/Downloads/earthchem_download_46477_csv.csv")
df_clean = df.dropna(subset=["SIO2", "FEO", "AL2O3"])

# Rock classification function
def classify_rock(sio2):
    if sio2 < 52:
        return "Basalt"
    elif 57 <= sio2 <= 63:
        return "Andesite"
    elif sio2 > 70:
        return "Rhyolite"
    else:
        return "Other"

df_clean["RockType"] = df_clean["SIO2"].apply(classify_rock)

# Scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_clean, x="SIO2", y="FEO", hue="RockType", palette="viridis")
plt.title("FeO vs SiO₂ by Rock Type")
plt.xlabel("SiO₂ (wt%)")
plt.ylabel("FeO (wt%)")
counts = df_clean["RockType"].value_counts()
x_pos = df_clean["SIO2"].min() + 1
y_start = df_clean["FEO"].max()
line_spacing = (df_clean["FEO"].max() - df_clean["FEO"].min()) / 10
for i, (rock, count) in enumerate(counts.items()):
    plt.text(x_pos, y_start - i * line_spacing, f"{rock}: {count}", fontsize=10)
plt.legend(title="Rock Type")
plt.tight_layout()
plt.show()

# Train model
features = df_clean[['SIO2', 'FEO', 'AL2O3']]
labels = df_clean['RockType']
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)
clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Evaluation
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Confusion matrix plot
labels_order = ['Andesite', 'Basalt', 'Other', 'Rhyolite']
cm = confusion_matrix(y_test, y_pred, labels=labels_order)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels_order, yticklabels=labels_order)
plt.title('Confusion Matrix of Rock Type Classification')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.tight_layout()
plt.show()

# Normalized confusion matrix
cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
sns.heatmap(cm_normalized, annot=True, fmt='.2f', cmap='YlGnBu', xticklabels=labels_order, yticklabels=labels_order)
plt.title('Normalized Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.tight_layout()
plt.show()

# Save model
os.makedirs("output", exist_ok=True)
joblib.dump(clf, "output/rock_classifier_model.joblib")
print("Model saved successfully!")
