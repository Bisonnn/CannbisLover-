from flask import Flask, jsonify, request
import pickle


app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Load the model
    with open('model_cannabis.pkl', 'rb') as f:
        model = pickle.load(f)

    # get the input data from the request
    data = request.get_json()

    # make a prediction using the loaded model
    result = model.predict(data)

    # return the prediction results as a response to the request
    return jsonify(result)

if __name__ == '__main__':
    app.run()


