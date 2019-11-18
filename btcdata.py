import numpy as np
from numpy import genfromtxt
np.set_printoptions(precision=10) #sets np precision to 10

import matplotlib.pyplot as plt

import glob

# from datetime import datetime

# import seaborn as sns

import pandas as pd
pd.set_option('precision', 10) #sets pandas precision to 10
pd.set_option('display.precision', 10) #sets pandas display precision to 10
#parameters for max column and row displays
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.plotting.register_matplotlib_converters()

def header(msg):
    print('-' * 50)
    print('[ ' + msg + ' ]')

filename = 'btcdata_2017-01-01-2019-11-04.csv'
df = pd.read_csv(filename)
df['Date'] = pd.to_datetime(df['Date'])
df = df[['Date', 'Price']]
df = df.set_index(['Date'])
df['Price'] = df['Price'].str.replace(',', '')

df = df.sort_values(by='Date') #sorting is optional
# df.plot(x='Date', y='Price')
# df = df['Price'].astype(float)

header('Plot 1, Federal Interest Rates Changed at Red Line')
#interest rate 1 Sept 18 2019
# previous federal interest rate = 2.25
# new federal interest rate = 2
df2 = df.loc['10/01/2019':'10/30/2019']
filename2 = 'data2.csv'
df2.to_csv(filename2)
df2 = pd.read_csv(filename2)

df3 = df.loc['10/01/2019':'11/4/2019']
filename3 = 'data3.csv'
df3.to_csv(filename3)
df3 = pd.read_csv(filename3)
# plot2 = df3.plot(x='Date', y='Price', color='red')

ax = df3.plot(x='Date', y='Price', color= 'red')
df2.plot(ax=ax, x='Date', y='Price', color='blue')
# plt.show()

header('Plot 2, Federal Interest Rates Changed at Red Line')
##interest rate 2 Oct 30 2019
# previous federal interest rate = 2.00
# new federal interest rate = 1.75

df4 = df.loc['08/15/2019':'09/17/2019']
filename4 = 'data4.csv'
df4.to_csv(filename4)
df4 = pd.read_csv(filename4)

df5 = df.loc['08/15/2019':'10/30/2019']
filename5 = 'data5.csv'
df5.to_csv(filename5)
df5 = pd.read_csv(filename5)
# plot2 = df3.plot(x='Date', y='Price', color='red')

ax2 = df5.plot(x='Date', y='Price', color= 'red')
df4.plot(ax=ax2, x='Date', y='Price', color='blue')
# plt.show()

# Properly Plot the first data frame without having to generate extra CSVs
df['Price'] = pd.to_numeric(df['Price'])
df = df.reset_index()
# print(df)

filename2 = 'vixcurrent.csv'
dfvix = pd.read_csv(filename2, skiprows=[0])
dfvix['Date'] = dfvix['Date'].astype('datetime64[ns]')
dfvix = dfvix.set_index(['Date'])
dfvix = dfvix.loc['1/1/2017':'11/4/2019']
dfvix = dfvix.reset_index()
# print(dfvix)
# print(dfvix.dtypes)

# Federal Interest Rate Data 2017 - 2019
all_files = glob.glob('data_fed/fir*.csv')

list = []
for filename in all_files:
    df_fir = pd.read_csv(filename, index_col=None, header=0)
    list.append(df_fir)

df_fir = pd.concat(list, axis=0, ignore_index=True)
df_fir['Date'] = df_fir['Date'].astype('datetime64[ns]')
df_fir = df_fir.set_index(['Date'])
df_fir = df_fir.loc['1/1/2017':'11/4/2019']
df_fir = df_fir.reset_index()
# print(df_fir)

# DOW Jones Data  2017-2019
filename3 = 'data_fed/DJI.csv'
df_dow = pd.read_csv(filename3)
df_dow['Date'] = df_dow['Date'].astype('datetime64[ns]')
df_dow = df_dow.set_index(['Date'])
df_dow = df_dow.loc['1/1/2017':'11/4/2019']
df_dow = df_dow.reset_index()
# print(df_dow)
# print(df_dow.dtypes)

# Comparison Plot of All Data
# fig, axes = plt.subplots(nrows=6, ncols=1, sharex=True)
fig, axes = plt.subplots(nrows=6, ncols=1)
df.plot(ax=axes[0], x='Date', y='Price')
df_dow.plot(ax=axes[1], x='Date', y='Open')
df_dow.plot(ax=axes[1], x='Date', y='Adj Close', color='r')
dfvix.plot(ax=axes[2], x='Date', y='VIX Close').set_xlabel('')
df_fir.plot(ax=axes[3], x='Date', y='1 Mo').set_xlabel('')
df_fir.plot(ax=axes[4], x='Date', y='3 Mo').set_xlabel('')
df_fir.plot(ax=axes[5], x='Date', y='6 Mo')
plt.show()
plt.close()
