#Importing the libraries
import pickle
import json
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, session

#Loading the model
model = pickle.load(open('model_cannabis.pkl', 'rb'))

#Creating the app
app = Flask(__name__)

#Creating the home page
@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html')

#Creating the notebook page
@app.route('/project-lineup.html')
def project():
    return render_template('project-lineup.html')

@app.route('/upload.html', methods=['GET', 'POST'])
def upload():
    return render_template('upload.html')

@app.route('/response.html', methods=['POST', 'GET'])
def response():
    if request.method == 'POST':
        # Get the uploaded file
        json_file = request.files['file']

        # Read the file
        df = pd.read_json(json_file)

        # Load the .pkl model
        model = pickle.load(open('model_cannabis.pkl', 'rb'))

        # Use the model to make a prediction
        prediction = model.predict(df)

        # if the prediction is 0, the user seems not to consume cannabis and return a message

        if prediction == 0:
            prediction = "You don't smoke cannabis"
        else:
            prediction = "You smoke cannabis"   
            
        # Render the response template, passing the prediction as a parameter
        return render_template('response.html', prediction=prediction)

#Running the app
if __name__ == "__main__":
    app.run(debug=True)

