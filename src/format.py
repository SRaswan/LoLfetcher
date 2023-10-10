import pandas as pd
import json

def load_json(file_name: str) -> pd.DataFrame:
    """Given a path to a json file, uses pandas to load the data into
    a dataframe"""
    with open(file_name) as f:
        leagues_json = json.load(f)

    return pd.json_normalize(leagues_json)