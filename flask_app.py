from flask import Flask, request, jsonify
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the saved model and scaler
model = joblib.load("kmeans_model.pkl")  # Ensure this file exists
scaler = joblib.load("scaler.pkl")  # Ensure this file exists

# Dictionary to map prediction values to meaningful responses
prediction_messages = {
    0: "Developing Nation",
    1: "Developed Nation",
    2: "In need of Help"
}

# Feature names
required_features = [
    "child_mort", "income", "inflation", "life_expec", 
    "total_fer", "gdpp", "exports_in_dollars", 
    "imports_in_dollars", "healthS_in_dollars"
]

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        print(f"Received data: {data}")  # Log the full data received
        
        # Extract features
        features = data.get("features", [])
        
        # Validate that the number of features matches the model's requirement
        if len(features) != len(required_features):
            error_message = f"Invalid input. Expecting {len(required_features)} features, but got {len(features)}."
            print(error_message)
            return jsonify({"error": error_message}), 400

        # Log the received features for debugging
        print(f"Features for prediction: {features}")

        # Convert to numpy array and reshape for prediction
        final_input = np.array([features])
        print(f"Features for prediction (as array): {final_input}")

        # Standardize the features using the scaler
        final_input_scaled = scaler.transform(final_input)
        print(f"Scaled input: {final_input_scaled}")

        # Predict using the trained KMeans model
        prediction = model.predict(final_input_scaled)[0]
        print(f"Predicted cluster: {prediction}")

        # Convert the NumPy int to a native Python int to make it JSON serializable
        prediction = int(prediction)

        prediction_message = prediction_messages.get(prediction, "Unknown category")
        return jsonify({"prediction": prediction, "message": prediction_message})

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
