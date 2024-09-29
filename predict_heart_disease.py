import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def compute_output(inputs):
    hd = pd.read_csv('heart_disease_health_indicators_BRFSS2015.csv')
    y = hd['HeartDiseaseorAttack']
    X = hd.drop(columns=['HeartDiseaseorAttack'])

    model = DecisionTreeClassifier()
    model.fit(X, y)
    test = inputs # pd.read_csv('testcase.csv')
    X_test = test #.drop(columns=['BlankPredictor'])
    prediction = model.predict(X_test)
    print(prediction)
    return prediction
    # print("Your output value is above. A value of 0 means you do not have heart disease, while a value of 1 means you do.")
    
    
