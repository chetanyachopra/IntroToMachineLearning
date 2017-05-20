import pandas as pd
import numpy as np
import csv
def indexing():
    start_date='2010-01-22'
    end_date='2010-01-26'
    dates=pd.date_range(start_date,end_date)
    df1=pd.DataFrame(index=dates)
#    print(df1)
DFSPY=pd.read_csv('data/SPY.csv')
print(DFSPY)



if __name__ == '__main__':
    indexing()
