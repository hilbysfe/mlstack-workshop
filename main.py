from typing import Optional
from fastapi import FastAPI
import yfinance
import datetime

app = FastAPI()

def fetch_ticker(symbol: str):
    return yfinance.Ticker(symbol)

def calc_prediction(ticker, days: int):
    return ticker.history(
                    start=(datetime.date.today() - datetime.timedelta(days=days)).isoformat(),
                    end=datetime.date.today().isoformat()
                    )

@app.get("/prediction/")
async def root(ticker: str, history: int = 1):
    
    # Call yahoo API for history
    y_ticker = fetch_ticker(ticker)

    # Calculate prediction
    pred = calc_prediction(y_ticker, history)
    print(pred)

    return {"Name:": ticker, "prediction": pred}
