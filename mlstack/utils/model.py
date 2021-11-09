import datetime
import numpy as np

class Model():    
    def predict(self, data):
        # Test if input is list/np.array or a single int, float
        if type(data) not in [list, np.array, np.ndarray, int, float]:
            raise TypeError("Data has to be a list or numpy array of int, float values.")
        
        return np.mean(data)

def get_prediction(model, ticker, days: int):
    # Get history
    data = ticker.history(
                    start=(datetime.date.today() - datetime.timedelta(days=days)).isoformat(),
                    end=datetime.date.today().isoformat()
                    )["Open"].to_numpy()
    # Calculate prediction
    return model.predict(data)