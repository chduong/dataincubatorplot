import numpy as np
from numpy import genfromtxt
np.set_printoptions(precision=10) #sets np precision to 10

import matplotlib.pyplot as plt

import seaborn as sns

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
# print(df)

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
plt.show()
