import pandas as pd

def readCsv():
    df = pd.read_csv('./data/input.csv', sep=',')
    return df.values

