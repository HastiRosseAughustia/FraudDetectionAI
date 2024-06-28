# train.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

# Load data
data = pd.read_csv('data/fraud_dataset.csv')

# Preprocessing
# Contoh saja, Anda perlu menyesuaikan dengan apa yang diperlukan oleh data Anda
X = data.drop('target_column_name', axis=1)
y = data['target_column_name']

# Split data menjadi train dan validation set
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Build model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.2),
    Dense(32, activation='relu'),
    Dropout(0.2),
    Dense(1, activation='sigmoid')
])

# Compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Define callbacks
early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

# Train model
history = model.fit(X_train, y_train, epochs=20, batch_size=32, 
                    validation_data=(X_val, y_val), callbacks=[early_stopping])

# Evaluate model
loss, accuracy = model.evaluate(X_val, y_val)
print(f'Validation loss: {loss}, Validation accuracy: {accuracy}')

# Save model
model.save('fraud_detection_model.h5')

