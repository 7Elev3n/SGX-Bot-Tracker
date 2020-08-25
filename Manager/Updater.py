from yahooquery import Ticker
import pandas as pd

def fetch(df, debug=True):
	'''
	Takes the dataframe 'df' and adds a column to it with stock price in that interval.
	If there already existed a previous such column, it is renamed to 'prev_price' with replacement.

	It also adds in any dividends, (maybe balance sheet info) it can find.

	Returns the finished dataframe. Run this function in accordance with intervals, the function does not track time itself.
	'''

	## Variables for parallelizing
	maxworkers = 8

	## Get ticker names from coymaster and find the yahoo finance info about all of them
	ticker_list = df['yf_ticker'].values.tolist()
	
	## These return a dict of dicts, converted into a pd dataframe. See bottom for examples of outputs.
	yq_tickers_price = pd.DataFrame.from_dict(Ticker(ticker_list, asynchronous=True, max_workers=maxworkers).price, 		 orient='index')	
	yq_tickers_info  = pd.DataFrame.from_dict(Ticker(ticker_list, asynchronous=True, max_workers=maxworkers).summary_detail, orient='index')

	#print(yq_tickers_price)
	## We set the indexes of these dataframes to the same as coymaster so that copying columns is easier.
	merged = yq_tickers_price.merge(right=yq_tickers_info)
	merged.set_index('symbol', inplace=True, drop=False)

	##  Update whatever data the table already had (if you want more columns, add into "Init.py")
	df.update(merged)

	## Randomly choose 3 companies and compare the stock prices so we know there is no issue with Yahoo or our code
	priceChecker(debug, df)

	## Return the df to main.py so that we can send it to all the algorithms.
	return df

def priceChecker(debug, df):
	if debug == True:
		randStocks = df.sample(n=3).loc[:,"yf_ticker"].values.tolist()
		cfm_prices = Ticker(randStocks).price

		for stock, value in cfm_prices.items():
			price = value['regularMarketPrice']
			listprice = df.loc[stock, "regularMarketPrice"]
			if listprice == price:
				print("Stock: " + str(stock) +" "+str(df.loc[stock,"Trading Name"]) + ",\tPrices - Actual: " + str(price) + ",\tWorkers: " + str(listprice))
			else:
				print("The prices fetched are not accurately updated. Please check the merge and update functions in 'Updater.py'.")
				return 1
		print("\nSuccessful updating of df!") 

	# df.to_csv("test.csv")
	# if debug:
	# 	## Check if Singtel Price is 2.3 and dbs is 20.79 and capitaland is 2.76
	
				
			
	# 	#print(str(len(ticker_list)) + " tickers: " + ticker_list.head)


''' price
{'Z74.SI': {
	'maxAge': 1,
--	'regularMarketChangePercent': 0.0039525656, 
--	'regularMarketChange': 0.00999999, 
	'regularMarketTime': '2020-07-06 17:04:26', 
	'priceHint': 4, 
--	'regularMarketPrice': 2.54, 
	'regularMarketDayHigh': 2.56, 
	'regularMarketDayLow': 2.52, 
	'regularMarketVolume': 13925300, 
	'regularMarketPreviousClose': 2.53, 
	'regularMarketSource': 'DELAYED', 
	'regularMarketOpen': 2.53, 
	'exchange': 'SES', 
	'exchangeName': 'SES', 
	'exchangeDataDelayedBy': 0, 
	'marketState': 'POSTPOST', 
	'quoteType': 'EQUITY', 
	'symbol': 'Z74.SI', 
	'underlyingSymbol': None, 
	'shortName': 'Singtel', 
	'longName': 'Singapore Telecommunications Limited', 
	'currency': 'SGD', 
	'currencySymbol': '$', 
	'fromCurrency': None, 
	'toCurrency': None, 
	'lastMarket': None, 
	'marketCap': 41476165632
	}, 
'''

''' summary_detail
{'Z74.SI': {
	'maxAge': 1, 
	'priceHint': 4, 
	'previousClose': 2.53, 
--	'open': 2.53, 
--	'dayLow': 2.52, 
--	'dayHigh': 2.56, 
	'regularMarketPreviousClose': 2.53, 
	'regularMarketOpen': 2.53, 
	'regularMarketDayLow': 2.52, 
	'regularMarketDayHigh': 2.56, 
--	'dividendRate': 0.11,
--	'dividendYield': 0.0431,
	'exDividendDate': '2020-08-04 08:00:00',
--	'payoutRatio': 2.6676998,
	'fiveYearAvgDividendYield': 5.1, 
--	'beta': 0.733256, 
--	'trailingPE': 38.484848, 
	'forwardPE': 12.095239, 
	'volume': 13925300, 
	'regularMarketVolume': 13925300, 
	'averageVolume': 33372384, 
	'averageVolume10days': 21292166, 
	'averageDailyVolume10Day': 21292166, 
--	'bid': 2.55, 
--	'ask': 2.55, 
--	'bidSize': 0, 
--	'askSize': 0, 
--	'marketCap': 41476165632, 
--	'fiftyTwoWeekLow': 2.19, 
--	'fiftyTwoWeekHigh': 3.55, 
--	'priceToSalesTrailing12Months': 2.5072792, 
	'fiftyDayAverage': 2.5685713, 
	'twoHundredDayAverage': 2.8827858, 
	'trailingAnnualDividendRate': 0.122,
	'trailingAnnualDividendYield': 0.048221346, 
	'currency': 'SGD', 
	'fromCurrency': None, 
	'toCurrency': None, 
	'lastMarket': None, 
	'algorithm': None, 
	'tradeable': False}, 
'''