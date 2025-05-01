import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
# Correct the import path based on the project structure
from utils.data_fetcher import fetch_stock_data 

def predict_stock(symbol):
    """
    Fetches stock data, trains a simple LSTM model, 
    and predicts the next closing price.
    """
    # Fetch data using the function from data_fetcher
    data = fetch_stock_data(symbol) 
    
    # Reshape data for scaling
    data = data.reshape(-1, 1)

    # Scale the data
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(data)

    # Prepare data sequences for LSTM
    X, y = [], []
    sequence_length = 10 # Use 10 previous days to predict the next
    for i in range(sequence_length, len(data_scaled)):
        X.append(data_scaled[i-sequence_length:i, 0])
        y.append(data_scaled[i, 0])

    X, y = np.array(X), np.array(y)

    # Reshape X for LSTM input [samples, time steps, features]
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    # Build the LSTM model
    model = Sequential([
        LSTM(50, return_sequences=False, input_shape=(X.shape[1], 1)),
        Dense(1) # Output layer with 1 neuron for the prediction
    ])

    # Compile the model
    model.compile(optimizer="adam", loss="mean_squared_error") # Use mean_squared_error

    # Train the model
    model.fit(X, y, epochs=5, batch_size=8, verbose=0) # Keep verbose=0 for cleaner output

    # Prepare the input for predicting the next day
    # Use the last sequence from the training data
    last_sequence = data_scaled[-sequence_length:] 
    last_sequence = last_sequence.reshape((1, sequence_length, 1))

    # Make the prediction
    predicted_scaled_price = model.predict(last_sequence)

    # Inverse transform the predicted price to the original scale
    predicted_price = scaler.inverse_transform(predicted_scaled_price)

    # Return the result
    return {"symbol": symbol, "predicted_price": round(predicted_price[0][0], 2)}
