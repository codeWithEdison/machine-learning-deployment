from flask import Flask, request, jsonify
import pandas as pd
import joblib

# Load the trained model and label encoder
model = joblib.load("decision_tree_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Initialize Flask app
app = Flask(__name__)

# Define a route for predictions
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get the JSON data from the POST request
        data = request.get_json()

        # Extract the features from the incoming JSON
        age = data["age"]
        gender = data["gender"]

        # Convert input into DataFrame for prediction
        input_data = pd.DataFrame([[age, gender]], columns=["age", "gender"])

        # Make prediction using the trained model
        prediction = model.predict(input_data)

        # Convert the prediction label back to the genre using the label encoder
        predicted_genre = label_encoder.inverse_transform(prediction)

        # Return the prediction as JSON
        return jsonify({"predicted_genre": predicted_genre[0]})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
