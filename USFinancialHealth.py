import codecademylib3_seaborn
import pandas as pd 
import pandas_datareader.data as web
from datetime import datetime 
import pandas_datareader.wb as wb
import numpy as np

gold_prices = pd.read_csv('gold_prices.csv')
print(gold_prices.head())

crude_oil_prices = pd.read_csv('crude_oil_prices.csv')
print(crude_oil_prices.head())

start = datetime(1999,1,1)
end = datetime(2019,1,1)

nasdaq_data = web.DataReader('NASDAQ100', 'fred', start, end)
print(nasdaq_data.head())

sap_data = web.DataReader('SP500', 'fred', start, end)
print(sap_data.head())

export_data = wb.download(indicator='NE.EXP.GNFS.CN', country=['US'], start=start, end=end)
print(export_data.head())

def log_return(prices):
  return np.log(prices/prices.shift(1))
# Couldve done some sort of loop to avoid this
# But wanted to follow instructions 
gold_returns = log_return(gold_prices['Gold_Price'])
crude_oil_returns = log_return(crude_oil_prices['Crude_Oil_Price'])
nasdaq_returns = log_return(nasdaq_data['NASDAQ100'])
sap_returns = log_return(sap_data['SP500'])
export_returns = log_return(export_data['NE.EXP.GNFS.CN'])

print(gold_returns.var())
print(crude_oil_returns.var())
print(nasdaq_returns.var())
print(sap_returns.var())
print(export_returns.var())


