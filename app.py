from flask import Flask, request, jsonify,render_template
import joblib, requests
import pandas as pd


app = Flask(__name__)


@app.route("/")

def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])


def prediction_quality_wine():
    
    # Check if request has a JSON content
    if request.json and request.method == "POST":
        
        # Get the JSON as dictionnary
        req = request.get_json()
        
        # Check mandatory key
        if "input" in req.keys():
            predict1 =[]
            
            X = pd.DataFrame(req["input"])
            # Load model
            classifier = joblib.load("model.joblib")
            # Predict
            prediction = classifier.predict(X)
            
            # We transform the predictions into a python list

            for i in range(len(prediction+1)):
                predict1.append(str(prediction[i]))

            prediction1 = [float(p)for p in predict1]
            
            # We display the results in a json dictionary
            
            return jsonify({"predict": prediction1}), 200
    return jsonify({"msg": "Error: not a JSON or no email key in your request"})


if __name__ == "__main__":
    app.run(debug=True)
