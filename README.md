# SGX-Bot-Tracker
A Manager/Simulator that can run Python Trading Bots and track their progress daily.

## Current Progress

1. Manager can select a universe of stocks, and update their current information from Yahoo Finance.

## Dependencies

- [Pandas](https://pandas.pydata.org/) (Manager + Bots)

- [YahooQuery](https://yahooquery.dpguthrie.com/) (Manager only)

- ~~~bash
  pip install pandas yahooquery
  ~~~

## Usage

The manager runs when "main.py" is started.

~~~python
python main.py
~~~

The manager uses "coy-master.csv" as well as variables inside "main.py" to create a universe of stocks. The stocks' information is fetched from Yahoo Finance (price, PE Ratio etc) and these are sent to every bot. Each bot is given SGD 100k, which it can use to buy stocks and then either hold or sell them. It returns these decisions to Manager which updates its database with bot holdings and net-worths. Since each bot uses different strategies to pick stocks to buy and sell, each bot should have a different trajectory of stocks. The Manager runs at a set interval (maybe twice a day) and updates stock information then. We can then plot a graph of all the bots and their progress. I aim to host this graph online. 

## Data passing/returning

### From Manager to Bot

To be done.

### From Bot to Manager

To be done.

## Bot Ideas

This repository is a facilitation for such bots. Without bots, the manager is useless. Here are some ideas for bots I aim to build myself. I hope I can crowdsource other bots as well in the future.

- "That one guy who judges using PE Ratio": Finds the highest PE Ratio and uses it to weight how much of a stock to buy. Simple.
- "The so-called Safe Investor": Buys according to some reputed ETF basket.
- "The Safest Investor": Sits on its pile of cash forever. Simple.
- "The Magic Formula Investor": Uses the "[Magic Formula](https://www.investopedia.com/terms/m/magic-formula-investing.asp)" to pick and buy stocks and hold for an year. Simple.