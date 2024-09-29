from flask import Flask, render_template, request
from flask import jsonify
import pandas as pd
from predict_heart_disease import compute_output

app = Flask(__name__)

# Function to process inputs
def process_inputs(data):
    # Example processing: sum the numeric values
    # You can replace this with your actual processing logic
    return data.sum().to_dict()  # Returning sum of each column as a dictionary

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def process():
    
    # Get data from the form and convert to a DataFrame
    input_data = {
        'HighBP': float(request.form.get('HighBP')),
        'HighChol': float(request.form.get('HighChol')),
        'CholCheck': float(request.form.get('CholCheck')),
        'BMI': float(request.form.get('BMI')),
        'Smoker': float(request.form.get('Smoker')),
        'Stroke': float(request.form.get('Stroke')),
        'Diabetes': float(request.form.get('Diabetes')),
        'PhysActivity': float(request.form.get('PhysActivity')),
        'Fruits': float(request.form.get('Fruits')),
        'Veggies': float(request.form.get('Veggies')),
        'HvyAlcoholConsump': float(request.form.get('HvyAlcoholConsump')),
        'AnyHealthcare': float(request.form.get('AnyHealthcare')),
        'NoDocbcCost': float(request.form.get('NoDocbcCost')),
        'GenHlth': float(request.form.get('GenHlth')),
        'MentHlth': float(request.form.get('MentHlth')),
        'PhysHlth': float(request.form.get('PhysHlth')),
        'DiffWalk': float(request.form.get('DiffWalk')),
        'Sex': float(request.form.get('Sex')),
        'Age': float(request.form.get('Age')),
        'Education': float(request.form.get('Education')),
        'Income': float(request.form.get('Income'))
    }

    # Create DataFrame from input data
    df = pd.DataFrame([input_data])
    
    # Call the processing function
    result = compute_output(df)[0]

    print(result)

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
