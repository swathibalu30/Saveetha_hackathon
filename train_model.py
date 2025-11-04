"""
Quick Model Training Script
This script trains the diagnostic model without using Jupyter Notebook.
Run this if you want to quickly train the model from command line.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

def train_model():
    """Train the diagnostic model and save it"""
    
    print("=" * 60)
    print("  Automated Diagnostic System - Model Training")
    print("=" * 60)
    print()
    
    # Load the dataset
    print("Loading dataset...")
    try:
        df = pd.read_csv('data/sample_patient_data.csv')
        print(f"✓ Dataset loaded: {df.shape[0]} samples, {df.shape[1]} features")
    except Exception as e:
        print(f"✗ Error loading dataset: {e}")
        return False
    
    # Preprocess the data
    print("\nPreprocessing data...")
    df['gender_numeric'] = df['gender'].apply(lambda x: 0 if x == 'Male' else 1)
    
    # Select features
    feature_columns = ['age', 'gender_numeric', 'bp', 'glucose', 'heart_rate']
    X = df[feature_columns]
    y = df['diagnosis']
    
    print(f"✓ Features prepared: {', '.join(feature_columns)}")
    print(f"✓ Target classes: {y.nunique()} unique diagnoses")
    
    # Split data
    print("\nSplitting data...")
    # Check if stratification is possible
    class_counts = y.value_counts()
    min_class_count = class_counts.min()
    
    if min_class_count < 2:
        print(f"⚠ Some classes have only {min_class_count} sample(s)")
        print("  Using random split instead of stratified split")
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
    else:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
    
    print(f"✓ Training set: {X_train.shape[0]} samples")
    print(f"✓ Testing set: {X_test.shape[0]} samples")
    
    # Train model
    print("\nTraining RandomForestClassifier...")
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)
    print("✓ Model training completed")
    
    # Evaluate
    print("\nEvaluating model...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"✓ Model accuracy: {accuracy * 100:.2f}%")
    
    # Save model
    print("\nSaving model...")
    model_dir = 'model'
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    
    model_path = os.path.join(model_dir, 'diagnostic_model.pkl')
    joblib.dump(model, model_path)
    print(f"✓ Model saved to: {model_path}")
    
    # Test the saved model
    print("\nTesting saved model...")
    loaded_model = joblib.load(model_path)
    sample_data = [[45, 0, 140, 110, 85]]  # Sample patient
    sample_df = pd.DataFrame(sample_data, columns=feature_columns)
    prediction = loaded_model.predict(sample_df)
    print(f"✓ Sample prediction: {prediction[0]}")
    
    # Display feature importance
    print("\nFeature Importance:")
    for feature, importance in zip(feature_columns, model.feature_importances_):
        print(f"  {feature:15s}: {importance:.4f}")
    
    print("\n" + "=" * 60)
    print("  Model training completed successfully!")
    print("=" * 60)
    print("\nYou can now run the Flask application:")
    print("  python app.py")
    print()
    
    return True

if __name__ == "__main__":
    try:
        success = train_model()
        if not success:
            print("\nTraining failed. Please check the errors above.")
            exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
