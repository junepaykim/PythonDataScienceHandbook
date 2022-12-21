'''Python, Pandas, Numpy time handling study'''
from datetime import datetime
import pandas as pd
import numpy as np
from dateutil import parser
import numpy as np


def pythonNative() :
    '''python native style time handling'''
    datetime(year=2015, month=7, day=4)    
    date = parser.parse("4th of July, 2015")
    date.strftime("%A")

def numpyTime() :
    '''numpy style'''
    date = np.array('2015-07-04', dtype=np.datetime64)
    print(date)
    date + np.arange(12)
    np.datetime64('2015-07-04')
    np.datetime64('2015-07-04 12:00')
    
def pandasTime() :
    '''pandas style. best among three'''
    print("\nBelow is Pandas")
    date = pd.to_datetime("4th of July, 2015")
    print(date)
    date.strftime('%A')
    date + pd.to_timedelta(np.arange(12), 'D')
    index = pd.DatetimeIndex(['2014-07-04', '2014-08-04', '2015-07-04', '2015-08-04'])
    data = pd.Series([0, 1, 2, 3], index=index)
    print(data)
    
    '''easily select data'''
    data['2014-07-04':'2015-07-04']
    data['2015']
    
    '''Compute by date subtraction'''
    dates = pd.to_datetime([datetime(2015, 7, 3), '4th of July, 2015',
                            '2015-Jul-6', '07-07-2015', '20150708'])
    dates.to_period('D')
    dates - dates[0]
    
    pd.timedelta_range(0, periods=9, freq="2H30T")
    
    from pandas.tseries.offsets import BDay
    pd.date_range('2015-07-01', periods=5, freq=BDay())
    
    

def main() :
    '''time handling main'''
    pythonNative()
    numpyTime()
    pandasTime()
    

if __name__ == "__main__" :
    main()