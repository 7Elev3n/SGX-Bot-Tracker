## Stock Manager (by 7Elev3n)
# Uses a CSV list of companies (manually downloaded off SGX directly) to create a list of (all) companies.
# User can edit 'Coy-master.csv' to add more companies. Use the same format as the download from https://www.sgx.com/securities/stock-screener 

## Assumptions
# - No (?) transaction fees (maybe to add later)
# - Prices of stocks do not change within a fixed interval (2 mins to start with)
# - One can buy (any amount) if they offer a price equal to or above the ask price.
# - One can sell (any amount) if they offer a price equal to or below the bid price.

## import pandas to handle the main dataframe which is passed to trading algos
import pandas as pd

## Init creates empty columns in the dataframe. Only these columns are updated by the Updater.
import Init

## Updater fetches Yahoo Finance data and populates/updates the dataframe.
import Updater

## Important Variables for manager
update_interval = 2 	# Set how often (in minutes) to update the dataframe using Yahoo Finance data

## Company Filtering
sgx_pri = True 			# Only keep companies primarily listed in SG (have '.SI' in their RIC code)
rank_mtd = 'none'		# Use Mkt Cap to rank the companies. Other options: "yield", "gti", "rev", "pe", "none". See "rank_mtds_all".
top_n = 10			# Find the top n companies ranked by the above method.
debug = False			# Shows outputs at significant steps to pinpoint any problems

rank_mtds_all = {
	'mktcap': "Mkt Cap ($M)",
	'yield'	: "Yield (%)",
	'gti'   : "GTI Score",
	'rev'   : "Tot. Rev ($M)",
	'pe'    : "P/E"
}

## read the master csv containing all companies
coymaster = pd.read_csv('coy-master.csv')

## Filtering
if sgx_pri:
	sglisted = coymaster['RIC'].str.contains('.SI',regex=False, na=False)
	coymaster = coymaster[sglisted]

## Sort the list by measure specified in 'rank_mtd'
if rank_mtd != 'none':
	column = rank_mtds_all[rank_mtd]
	coymaster.sort_values(by=[column],inplace=True,ascending=False)

## Trim the list as required by 'top_n'
if top_n < len(coymaster.index):
	coymaster = coymaster.head(top_n)
	coymaster.reset_index(drop=True, inplace=True)

## Create yahoo-finance readable stock tickers
coymaster['yf_ticker'] = coymaster['Trading Code'].astype(str) +'.SI'

############################ END OF DATA CLEANING AND DATAFRAME CREATION ############################
print("Setup done, sending df to Init...")

## Updater checks Yahoo Finance for stock prices and other stock info and updates the dataframe with it. 
## Updater should run every x minutes, where x = 'update_interval'


row = coymaster[0:top_n+1]


df = Init.init(debug=debug, df = row)

print("Init done, sending df to Updater...")
updated_df = Updater.fetch(debug=debug, df = df)

############################ DATA IS UPDATED NOW ############################

print("Update done, starting Scorekeeping...")
import Scorekeep

## Scorekeep has 2 functions: Init and Update.
## Init: creates table 
## Find all the bots under the Bots folder
## Create a table with columns for each bot, and rows that reflect every company in the selected universe (uses coy-master.csv)
# Each column has:
# 1. A net worth row (in today's dollars, nominal)
# 2. Cash pile row (inflation adjusted everyday) (scrape inflation rate from online)
# 3. A row for each company in the universe and the bot's holdings of that company (# of shares)

## main.py
	# 1. Create an 'forAlgo' dataframe. !!DONE!!
	# 2. Read coy-master.csv and filter out the correct companies to focus on. !!DONE!!
	# 3. Copy their name, tickername into forAlgo. !!DONE!!
	# 4. Run updater.py and loop it, every 2 minutes. (make lower if can be fast enough) !!DONE!!
	# 5. Run trading algos after forAlgo.csv is updated. End process(es) within 2 minutes. 

## forAlgo Pandas DF
	# 1. stock info (bid/ask/open) in the abovementioned time interval (1 row)
	# 2. stock info (open/close/high/low/volume/dividends) within the past n days (configurable). n depends on how much data the algos use.
	# 3. (TBC) news articles?? sentiment analysis?? 

## updater.py
	# 1. downloads and updates forAlgo df

## Plotter.py
	# 1. Creates the plot, sends it to Plotly Chart Studio Free https://plotly.com/python/getting-started-with-chart-studio/
	# 2. Plot is shown online for anyone to see.

## DF columns
	# for val in df.columns.values.tolist():
	# 	print("\t- " + val)
	      # - Trading Name
	      # - Trading Code
	      # - RIC
	      # - Mkt Cap ($M)
	      # - Tot. Rev ($M)
	      # - P/E
	      # - Yield (%)
	      # - Sector
	      # - GTI Score
	      # - yf_ticker
	      # - regularMarketChangePercent
	      # - regularMarketChange
	      # - regularMarketPrice
	      # - open
	      # - dayLow
	      # - dayHigh
	      # - dividendRate
	      # - dividendYield
	      # - payoutRatio
	      # - beta
	      # - trailingPE
	      # - bid
	      # - ask
	      # - bidSize
	      # - askSize
	      # - marketCap
	      # - fiftyTwoWeekLow
	      # - fiftyTwoWeekHigh
	      # - priceToSalesTrailing12Months