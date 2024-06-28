import argparse
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def load_model(model_path):
    """Load a pre-trained model from a file."""
    return joblib.load(model_path)

def load_data(data_path):
    """Load test data from a file."""
    # Implement sesuai format data yang Anda gunakan
    # Contoh untuk format CSV:
    import pandas as pd
    data = pd.read_csv(data_path)
    X_test = data.drop('label', axis=1)
    y_test = data['label']
    return X_test, y_test

def evaluate_model(model, X_test, y_test):
    """Evaluate the model on the test data and print evaluation metrics."""
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)

    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")
    print("Confusion Matrix:")
    print(conf_matrix)

def main(args):
    model = load_model(args.model_path)
    X_test, y_test = load_data(args.data_path)
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate a pre-trained model.")
    parser.add_argument("model_path", type=str, help="Path to the pre-trained model file.")
    parser.add_argument("data_path", type=str, help="Path to the test data file.")
    
    args = parser.parse_args()
    main(args)

