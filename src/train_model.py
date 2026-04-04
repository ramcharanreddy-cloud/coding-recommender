import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import pickle

# 🔷 Load dataset
df = pd.read_csv("data/dataset.csv")

# 🔷 Encode categorical columns
le_edu = LabelEncoder()
le_interest = LabelEncoder()
le_diff = LabelEncoder()
le_output = LabelEncoder()

df["Education"] = le_edu.fit_transform(df["Education"])
df["Interest"] = le_interest.fit_transform(df["Interest"])
df["Difficulty"] = le_diff.fit_transform(df["Difficulty"])
df["Recommended_Language"] = le_output.fit_transform(df["Recommended_Language"])

# 🔷 Features & Target
X = df.drop("Recommended_Language", axis=1)
y = df["Recommended_Language"]

# 🔷 Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 🔷 Train model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# 🔷 Accuracy
accuracy = model.score(X_test, y_test)
print("✅ Model Accuracy:", accuracy)

# 🔷 Save model + encoders
pickle.dump(model, open("models/model.pkl", "wb"))
pickle.dump(le_edu, open("models/le_edu.pkl", "wb"))
pickle.dump(le_interest, open("models/le_interest.pkl", "wb"))
pickle.dump(le_diff, open("models/le_diff.pkl", "wb"))
pickle.dump(le_output, open("models/le_output.pkl", "wb"))

print("🔥 Model saved successfully!")