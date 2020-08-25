import pandas as pd 
import numpy as np

price_obj_vars = ['regularMarketChangePercent', 'regularMarketChange', 'regularMarketPrice']
info_obj_vars = ['open', 'dayLow', 'dayHigh', 'dividendRate', 'dividendYield', 'payoutRatio', 'beta', 'trailingPE', 'bid', 'ask', 'bidSize', 'askSize', 'marketCap', 'fiftyTwoWeekLow', 'fiftyTwoWeekHigh', 'priceToSalesTrailing12Months']

def init(debug, df):
	## The purpose of this function is to add empty columns to the df created by "main.py"
	## Then return the df so that Updater.py can keep updating it and passing it to the trading algorithms

	df = df.reindex(columns = df.columns.tolist() + price_obj_vars+info_obj_vars)
	# for col in price_obj_vars+info_obj_vars:
	# 	df[col] = np.nan
	df.set_index('yf_ticker', inplace=True, drop=False) ## Set the Index to the ticker name so that it is easy to merge later on with updated data.
	
	return df