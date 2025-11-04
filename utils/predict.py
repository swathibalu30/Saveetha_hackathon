import joblib
import pandas as pd
from utils.preprocess import preprocess_input
import os

def predict_disease(patient_data):
    """
    Predicts disease based on patient data using the trained model.
    
    Args:
        patient_data (dict): Dictionary containing patient information:
                           - age, gender, bp, glucose, heart_rate, symptoms
    
    Returns:
        str: Predicted disease name
    """
    try:
        # Get the model path
        model_path = os.path.join('model', 'diagnostic_model.pkl')
        
        # Load the saved model
        model = joblib.load(model_path)
        
        # Preprocess the input data
        processed_data = preprocess_input(patient_data)
        
        # Prepare features for prediction
        # The model was trained with: age, gender_numeric, bp, glucose, heart_rate
        features = [[
            processed_data.get('age', 0),
            processed_data.get('gender', 0),  # This is already converted to numeric by preprocess_input
            processed_data.get('bp', 0),
            processed_data.get('glucose', 0),
            processed_data.get('heart_rate', 0)
        ]]
        
        # Convert to DataFrame with proper column names (must match training)
        feature_names = ['age', 'gender_numeric', 'bp', 'glucose', 'heart_rate']
        features_df = pd.DataFrame(features, columns=feature_names)
        
        # Make prediction
        prediction = model.predict(features_df)
        
        # Return the predicted disease
        return prediction[0]
        
    except FileNotFoundError:
        return "Model not found. Please train the model first."
    except Exception as e:
        return f"Error during prediction: {str(e)}"
