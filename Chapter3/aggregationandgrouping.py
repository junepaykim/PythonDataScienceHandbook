'''2022.11.28 study'''
import numpy as np
import pandas as pd
import seaborn as sns

def main() :
    '''introduction to seaborn'''
    planets = sns.load_dataset('planets')    
    print(planets.head)
    #print(planets.shape)
    
    print(planets.dropna().shape)
    print(planets.dropna().describe())
    
if __name__ == "__main__" :
    main()
    