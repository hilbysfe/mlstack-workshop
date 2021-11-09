from typing import Optional
from fastapi import FastAPI
import yfinance
import datetime
import numpy as np

app = FastAPI()

def fetch_ticker(symbol: str):
    return yfinance.Ticker(symbol)

def calc_prediction(ticker, days: int):
    # Get history
    data = ticker.history(
                    start=(datetime.date.today() - datetime.timedelta(days=days)).isoformat(),
                    end=datetime.date.today().isoformat()
                    )["Open"].to_numpy()
    # Calculate prediction
    return np.mean(data)

@app.get("/prediction/")
async def root(ticker: str, history: int = 10):
    
    # Call yahoo API for history
    y_ticker = fetch_ticker(ticker)

    # Calculate prediction
    pred = calc_prediction(y_ticker, history)
    print(pred)

    return {"Name:": ticker, "prediction": pred}
