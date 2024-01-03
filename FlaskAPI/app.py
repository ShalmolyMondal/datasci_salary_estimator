import flask
from flask import Flask, jsonify, request
import json
import numpy as np
import pickle
from data_input import data_in


def load_model():
    file_name = "models/model_file.p"
    with open(file_name, "rb") as pickled:
        data = pickle.load(pickled)
        model = data["model"]
    return model


app = Flask(__name__)


@app.route("/predict", methods=["GET"])
def predict():
    # Get input features from the request
    request_json = request.get_json()
    x = request_json["input"]
    # print(x)

    # Convert input to a numpy array
    x_in = np.array(x).reshape(1, -1)

    # load the model
    model = load_model()

    # Make prediction
    prediction = model.predict(x_in)[0]

    # Prepare response
    response = json.dumps({"response": prediction})
    return response, 200


if __name__ == "__main__":
    app.run(debug=True)
