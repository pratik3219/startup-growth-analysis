# ==============================
# Startup Success Prediction Model
# ==============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


df = pd.read_excel(r'C:\Users\prati\OneDrive\Desktop\project\Project Data.xlsx')
# ==============================
# 2️⃣ Data Cleaning (Updated)
# ==============================
df.replace('Nil', 0, inplace=True)
df.fillna(0, inplace=True)

# Function to handle ranges like "1001-5000"
def convert_range(value):
    if isinstance(value, str) and '-' in value:
        parts = value.split('-')
        try:
            return (float(parts[0]) + float(parts[1])) / 2
        except:
            return np.nan
    else:
        try:
            return float(str(value).replace(',', '').replace('$', '').replace(' ', ''))
        except:
            return np.nan

# Convert all numeric columns safely
numeric_cols = ['Funding(in $)', 'Number of Employees', 'Funding Rounds', 'Number of Investors', 'Market Valuation(in $)']
for col in numeric_cols:
    df[col] = df[col].apply(convert_range)
# ==============================
df['Success'] = np.where(df['Funding(in $)'] > 10000000, 1, 0)

# ==============================
# 4️⃣ Select Features
# ==============================
features = ['Start Year', 'Number of Employees', 'Funding Rounds', 'Number of Investors', 'Market Valuation(in $)']
X = df[features]
y = df['Success']

# ==============================
# 5️⃣ Split Dataset
# ==============================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==============================
# 6️⃣ Scale Features
# ==============================
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ==============================
# 7️⃣ Build Model (Random Forest)
# ==============================
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ==============================
# 8️⃣ Evaluate Model
# ==============================
y_pred = model.predict(X_test)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

# ==============================
# 9️⃣ Confusion Matrix
# ==============================
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix - Startup Success Prediction")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# ==============================
# 🔟 Feature Importance
# ==============================
importances = pd.Series(model.feature_importances_, index=features).sort_values(ascending=False)
print("\n🌟 Feature Importance:\n", importances)

sns.barplot(x=importances, y=importances.index, palette="viridis")
plt.title("Feature Importance - What drives startup success?")
plt.show()
