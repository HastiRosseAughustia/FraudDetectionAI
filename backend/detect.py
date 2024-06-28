from flask import Blueprint, request, jsonify
import pickle
import pandas as pd
from utils.preprocess import preprocess_data

detect = Blueprint('detect', __name__)

# Load model
with open('model/fraud_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@detect.route('/')
def home():
    return "Fraud Detection API is running!"

@detect.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        df = pd.DataFrame([data])
        
        # Preprocess the data
        processed_data = preprocess_data(df)
        
        # Predict using the model
        prediction = model.predict(processed_data)
        result = 'fraud' if prediction[0] == 1 else 'not fraud'
        
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)})

