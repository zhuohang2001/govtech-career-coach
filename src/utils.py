import pandas as pd
import json

# Save dataframe to CSV
def save_to_csv(df, filename, index_flag):
    df.to_csv(filename, index=index_flag)
    
# Load JSON data
def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

# Load Excel data
def load_excel(filename):
    return pd.read_excel(filename)