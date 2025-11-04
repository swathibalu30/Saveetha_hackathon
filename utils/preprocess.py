def preprocess_input(data):
    """
    Preprocesses input data for the diagnostic model.
    Converts gender text to numeric values.
    
    Args:
        data (dict): Dictionary containing patient data with keys:
                    - age, gender, bp, glucose, heart_rate, symptoms
    
    Returns:
        dict: Preprocessed data with gender converted to numeric
    """
    # Create a copy to avoid modifying the original
    processed_data = data.copy()
    
    # Convert gender to numeric: 0 for Male, 1 for Female
    if 'gender' in processed_data:
        if processed_data['gender'].lower() == 'male':
            processed_data['gender'] = 0
        elif processed_data['gender'].lower() == 'female':
            processed_data['gender'] = 1
        else:
            processed_data['gender'] = 0  # Default to 0 if unknown
    
    return processed_data


def convert_gender_to_numeric(gender):
    """
    Converts gender text to numeric value.
    
    Args:
        gender (str): Gender as text ('Male' or 'Female')
    
    Returns:
        int: 0 for Male, 1 for Female
    """
    if isinstance(gender, str):
        return 0 if gender.lower() == 'male' else 1
    return gender
