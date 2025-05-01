from flask import Flask, request, jsonify
# Correct the import path based on the project structure
from model.lstm_model import predict_stock 
import os

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    """API endpoint to predict stock price based on symbol."""
    # Check if the request contains JSON data
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    symbol = data.get("symbol")

    # Validate that 'symbol' is provided
    if not symbol:
        return jsonify({"error": "symbol is required"}), 400
    
    # Check if symbol is a string
    if not isinstance(symbol, str):
         return jsonify({"error": "symbol must be a string"}), 400

    try:
        # Call the prediction function
        prediction = predict_stock(symbol)
        return jsonify(prediction)
    except Exception as e:
        # Handle potential errors during data fetching or prediction
        # Log the error for debugging (optional)
        # print(f"Error processing symbol {symbol}: {e}") 
        # Provide a generic error message to the client
        # Check for specific yfinance errors (e.g., symbol not found)
        if "No data found for symbol" in str(e) or "symbol may be delisted" in str(e):
             return jsonify({"error": f"Could not fetch data for symbol: {symbol}. It might be invalid or delisted."}), 404
        return jsonify({"error": f"An error occurred processing the request for symbol {symbol}"}), 500

if __name__ == "__main__":
    # Get port from environment variable or default to 5000
    port = int(os.getenv("PORT", 5000)) 
    # Run the app with debug mode enabled (consider disabling in production)
    app.run(debug=True, host='0.0.0.0', port=port)
