import numpy as np
np.set_printoptions(precision=10) #sets np precision to 10

import matplotlib.pyplot as plt

from scipy import stats

import pandas as pd
pd.set_option('precision', 10) #sets pandas precision to 10
pd.set_option('display.precision', 10) #sets pandas display precision to 10
#parameters for max column and row displays
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def header(msg):
    print('-' * 50)
    print('[ ' + msg + ' ]')

filename = 'btcdata_2017-01-01-2019-11-04.csv'
df = pd.read_csv(filename)
df['Date'] = pd.to_datetime(df['Date'])
df2 = df.set_index(['Date'])
df2 = df2.loc['2019-10-01':'2019-10-31']

print(df2)


header('Plot 1')
# print(len(df))
#interest rate 1 Sept 18 2019
previousfir1 = 2.25
fir1 = 2

##interest rate 2 Oct 30 2019
previousfir2 = fir1
fir2 = 1.75

print(df.dtypes)
# df = df.set_index(['Date'])
# print(df2)
# df3 = df2.loc['Oct 1, 2018':'Oct 31, 2018']

# df2.plot(kind='scatter', x='Date', y='Change %', color='red')
# plt.show()