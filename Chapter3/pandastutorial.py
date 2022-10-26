'''initial pandas usage'''
import pandas as pd
import numpy as np

population_dict = {'California' : 38332521,
                   'Texas' : 26448193,
                   'New York' : 19651127,
                   'Florida' : 19552860,
                   'Illinois' : 12882135}
area_dict = {'California' : 1,
                   'Texas' : 2,
                   'New York' : 33333,
                   'Florida' : 44,
                   'Illinois' : 555}
population = pd.Series(population_dict)
pd.DataFrame(population, columns=['population'])
pd.DataFrame(population, columns=['test1'])

df = pd.DataFrame([[1, np.nan, 2],
                   [7, 3, 5],
                   [np.nan, 4, 6]])
print(population_dict)