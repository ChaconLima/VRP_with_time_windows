import pandas as pd
from const import FILE

def readCsv():
    df = pd.read_csv('./data/'+FILE, sep=',')
    return df.values

