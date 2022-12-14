'''pivot table study'''
import pandas as pd
import numpy as np
import seaborn as sns

def main() :
    '''pivot table main'''
    titanic = sns.load_dataset('titanic')
    print(titanic.groupby(['sex','class'])['survived'].aggregate('mean').unstack())
    print(titanic.groupby(['sex','class'])['survived'].mean())
    

if __name__ == "__main__" :
    main()