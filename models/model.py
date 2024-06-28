# Import library yang dibutuhkan
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# 1. Load data
data = pd.read_csv('data.csv')

# 2. Prepare data
X = data.drop('target', axis=1)  # Misalkan 'target' adalah kolom yang menandakan kecurangan
y = data['target']

# 3. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Choose model
model = RandomForestClassifier()

# 5. Train model
model.fit(X_train, y_train)

# 6. Evaluate model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# 7. Save the model (optional)
# model.save('fraud_detection_model')

# 8. Document your work in model.py

