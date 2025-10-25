from ucimlrepo import fetch_ucirepo
import pandas as pd

def load_data():
    # fetch dataset 
    auto_mpg = fetch_ucirepo(id=9) 
    
    # data (as pandas dataframes) 
    X = auto_mpg.data.features 
    y = auto_mpg.data.targets 
    
    # Combine features and target
    df = pd.concat([X, y], axis=1)
    
    return df