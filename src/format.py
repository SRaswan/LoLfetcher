import pandas as pd
import json
import os

def load_json(file_name: str) -> pd.DataFrame:
    """Given a path to a json file, uses pandas to load the data into
    a dataframe"""
    with open(file_name) as f:
        f_json = json.load(f)

    return pd.json_normalize(f_json)


if __name__ == "__main__":
    jsonload = []
    for filename in os.listdir("esports-data/"):
        json.append(load_json(filename))