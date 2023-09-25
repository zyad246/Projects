# Import libraries
import gzip
import json
import pickle

import pandas as pd


# Add wrangle function from lesson 5.4
# Wrangle function
def wrangle(filename):
    
    with gzip.open(filename, "r") as f:
        data = json.load(f)
    df = pd.DataFrame().from_dict(taiwan_data["data"]).set_index("company_id")
    
    return df

# Add make_predictions function from lesson 5.3
def make_predictions(data_filepath, model_filepath):
   
    X_test = wrangle(data_filepath)
    with open(model_filepath, "rb") as f:
        loaded_model = pickle.load(f)
    y_test_pred = model.predict(X_test)
    y_test_pred=pd.Series(y_test_pred,index=X_test.index,name="bankrupt")
    return y_test_pred
