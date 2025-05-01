# AI Stock Predictor

A simple Flask API that predicts the next day's stock closing price using an LSTM model based on the last 60 days of historical data.

## Features

-   Accepts a stock/crypto symbol via a POST request to `/predict`.
-   Fetches historical data using the `yfinance` library.
-   Trains a simple LSTM model on the historical data.
-   Returns the predicted closing price for the next day.

## Project Structure

```
ai-prediction/
├── app.py              # Main Flask application
├── model/
│   └── lstm_model.py   # LSTM model logic
├── utils/
│   └── data_fetcher.py # Data fetching logic (yfinance)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Setup and Installation

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <repository_url>
    cd ai-prediction
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1.  **Run the Flask development server:**
    ```bash
    export FLASK_APP=app.py # On Windows use `set FLASK_APP=app.py`
    flask run
    ```
    Alternatively, you can run directly:
    ```bash
    python app.py
    ```
    The application will start on `http://127.0.0.1:5000` (or the port specified by the `PORT` environment variable).

## Usage

Send a POST request to the `/predict` endpoint with a JSON body containing the stock symbol.

**Example using `curl`:**

```bash
curl -X POST http://127.0.0.1:5000/predict      -H "Content-Type: application/json"      -d '{"symbol": "AAPL"}'
```

**Example Response:**

```json
{
  "symbol": "AAPL",
  "predicted_price": 175.34 
}
```
*(Note: The predicted price is an example and will vary)*

## Disclaimer

This is a simple demonstrative model and should not be used for actual financial decisions. Stock market prediction is complex and involves significant risk.
