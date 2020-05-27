import numpy as np
from flask import Flask, request, jsonify
import pickle as pkl
from train import DummyModel
import pandas as pd

app = Flask(__name__)
model = pkl.load(open("model.pkl", "rb"))

@app.route("/api", methods=["POST"])
def apply_model():
    data = request.get_json(force = True)
    x = pd.DataFrame(data["x"], columns=["lat", "lon", "Season"]).values
    ans = model.map_to_locations(model.predict(x=x)).tolist()
    return jsonify(Input = data["x"], Recommendations = ans)

if __name__ == '__main__':
    app.run(port=8080, debug=True)




