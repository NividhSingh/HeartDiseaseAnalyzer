import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def compute_output(inputs):
    hd = pd.read_csv('heart_disease_health_indicators_BRFSS2015.csv')  # Load dataset
    y = hd['HeartDiseaseorAttack']  # Target variable
    X = hd.drop(columns=['HeartDiseaseorAttack'])  # Feature set

    model = DecisionTreeClassifier()  # Initialize classifier
    model.fit(X, y)  # Train the model
    
    X_test = inputs  # Input data for prediction
    prediction = model.predict(X_test)  # Make predictions
    
    print(prediction)  # Print predictions
    return prediction  # Return predictions
    
