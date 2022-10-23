'''2022.10.23 study'''
import numpy as np
import pandas as pd

def main() :
    '''pandas3 main'''
    print(make_df('ABC', range(3)))
    

def make_df(cols, ind):
    """Quickly make a DataFrame"""
    data = {c : [str(c) + str(i) for i in ind]
            for c in cols}
    return pd.DataFrame(data, ind)

if __name__ == "__main__" :
    main()
    