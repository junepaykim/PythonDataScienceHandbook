'''Python, Pandas, Numpy time handling study'''
from datetime import datetime
import pandas as pd
import numpy as np
from dateutil import parser
import numpy as np
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import seaborn
import yfinance as yf



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
    
def pandasTimeExample():
    '''pandas time example function'''
    '''Google chart is shown in book for example but google does not provide chart any more'''
    '''So, use yahoo chat. install pip install yfinance first'''
    yf.pdr_override()
    data = pdr.get_data_yahoo('005930.KS', start='2012-01-01', end='2020-12-31')
    #print(data.head())
    data = data['Close']
    
    seaborn.set()  
    data.plot()    
    
    #print(type(data.resample('BA').mean()))
    #print(type(data.asfreq('BA')))
    data.plot(alpha=0.5, style='-')
    data.resample('BA').mean().plot(style=':')
    data.asfreq('BA').plot(style='--')
    plt.legend(['input', 'resample', 'asfreq'], loc='upper left')
    '''input does not work for some reason...'''
    
    '''Working for NA values // forward fill vs backward fill'''
    fig, ax = plt.subplots(2, sharex=True)
    yaho = data.iloc[:10]
    yaho.asfreq('D').plot(ax=ax[0], marker='o')
    yaho.asfreq('D', method='bfill').plot(ax=ax[1], style='-o')
    yaho.asfreq('D', method='ffill').plot(ax=ax[1], style='--o')
    ax[1].legend(["back-fill", "forward-fill"])
    
    '''Time shift'''
    fig, ax = plt.subplots(3, sharey=True)
    yaho = data.asfreq('D', method='pad')
    
    yaho.plot(ax=ax[0])
    yaho.shift(900).plot(ax=ax[1])
    yaho.tshift(900).plot(ax=ax[2])
    
    local_max = pd.to_datetime('2017-11-05')
    offset = pd.Timedelta(900, 'D')
    
    ax[0].legend(['input'], loc=2)
    ax[0].get_xticklabels()[1].set(weight='heavy', color='red')
    ax[0].axvline(local_max, alpha=0.3, color='red')
    
    ax[1].legend(['shift(900)'], loc=2)
    ax[1].get_xticklabels()[1].set(weight='heavy', color='red')
    ax[1].axvline(local_max + offset, alpha=0.3, color='red')
    
    ax[2].legend(['tshift(900)'], loc=2)
    ax[2].get_xticklabels()[1].set(weight='heavy', color='red')
    ax[2].axvline(local_max + offset, alpha=0.3, color='red')
    
    
    '''value compute'''
    ROI = 100 * (yaho.tshift(-365) / yaho - 1)
    yaho.plot()
    plt.ylabel('% Return on Investment')
    
    

def main() :
    '''time handling main'''
    """ pythonNative()
    numpyTime()
    pandasTime() """
    pandasTimeExample()
    

if __name__ == "__main__" :
    main()