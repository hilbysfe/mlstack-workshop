from typing import Optional
from fastapi import FastAPI
import yfinance

from mlstack.utils.model import get_prediction, Model

app = FastAPI()

# Create model
model = Model()

def fetch_ticker(symbol: str):
    return yfinance.Ticker(symbol)

@app.get("/prediction/")
async def root(ticker: str, history: int = 10):
    
    # Call yahoo API for history
    y_ticker = fetch_ticker(ticker)

    # Calculate prediction
    pred = get_prediction(model, y_ticker, history)

    return {"Name:": ticker, "prediction": pred}
