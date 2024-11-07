from typing import Dict
import requests
import yfinance as yf
import investpy as ipy
import pandas as pd

if (test := 0) == 1:
    spy = yf.Ticker("SPY")

    #lets print basic ticker information as a stock
    print(f"Stock Information: {spy.info}")
    print(f"History Metadata: {spy.history_metadata}")

    # show actions (dividends, splits, capital gains)
    print(f"Actions: {spy.actions}")
    print(f"Dividends: {spy.dividends}")
    print(f"Splits: {spy.splits}")
    print(f"Capital Gains: {spy.capital_gains}")  # only for mutual funds & etfs

    # show share count
    print(f"Shares Full: {spy.get_shares_full(start='2022-01-01', end=None)}")

    # show financials:
    print(f"Calendar: {spy.calendar}")
    print(f"SEC Filings: {spy.sec_filings}")
    # - income statement
    print(f"Income Statement: {spy.income_stmt}")
    print(f"Quarterly Income Statement: {spy.quarterly_income_stmt}")
    # - balance sheet
    print(f"Balance Sheet: {spy.balance_sheet}")
    print(f"Quarterly Balance Sheet: {spy.quarterly_balance_sheet}")
    # - cash flow statement
    print(f"Cash Flow: {spy.cashflow}")
    print(f"Quarterly Cash Flow: {spy.quarterly_cashflow}")
    # see `Ticker.get_income_stmt()` for more options

    # show holders
    print(f"Major Holders: {spy.major_holders}")
    print(f"Institutional Holders: {spy.institutional_holders}")
    print(f"Mutual Fund Holders: {spy.mutualfund_holders}")
    print(f"Insider Transactions: {spy.insider_transactions}")
    print(f"Insider Purchases: {spy.insider_purchases}")
    print(f"Insider Roster Holders: {spy.insider_roster_holders}")

    print(f"Sustainability: {spy.sustainability}")

    # show recommendations
    print(f"Recommendations: {spy.recommendations}")
    print(f"Recommendations Summary: {spy.recommendations_summary}")
    print(f"Upgrades/Downgrades: {spy.upgrades_downgrades}")

    # show analysts data
    print(f"Analyst Price Targets: {spy.analyst_price_targets}")
    print(f"Earnings Estimate: {spy.earnings_estimate}")
    print(f"Revenue Estimate: {spy.revenue_estimate}")
    print(f"Earnings History: {spy.earnings_history}")
    print(f"EPS Trend: {spy.eps_trend}")
    print(f"EPS Revisions: {spy.eps_revisions}")
    print(f"Growth Estimates: {spy.growth_estimates}")

    # Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default.
    # Note: If more are needed use spy.get_earnings_dates(limit=XX) with increased limit argument.
    print(f"Earnings Dates: {spy.earnings_dates}")

    # show ISIN code - *experimental*
    # ISIN = International Securities Identification Number
    print(f"ISIN: {spy.isin}")

    # show options expirations
    print(f"Options: {spy.options}")

    # show news
    print(f"News: {spy.news}")





    #informatio about the spy variable as an etf
    data = spy.funds_data



    #lets print the size of the spy variable
    ### Result: doesnt have len() method
    ##print(f'size of spy: {len(spy)}')

    #lets print the size of the data variable
    ### Result: aswell doesnt have len() method
    #print(f'size of data: {len(data)}')


    ### print the following
    """
    data.asset_classes
    data.top_holdings
    data.equity_holdings
    data.bond_holdings
    data.bond_ratings
    data.sector_weightings
    """

    print(f"Asset Classes: {data.asset_classes}")
    print(f"Top Holdings: {data.top_holdings}")
    print(f"Equity Holdings: {data.equity_holdings}")
    print(f"Bond Holdings: {data.bond_holdings}")
    print(f"Bond Ratings: {data.bond_ratings}")
    print(f"Sector Weightings: {data.sector_weightings}")





    ## lets use the history returned object
    ## turn off auto adjust, than pricing is exact as google yahoo finance etc.
    history = spy.history(period="max", interval="1mo",auto_adjust = False)
    print(f"History of spy max interval 1month: {history}")
    ## lets print the first and the last 5 rows
    print(f"First 5 rows: {history.head()}")
    print(f"Last 5 rows: {history.tail()}")


    ## testing investpy

    # lets get list of etfs in the US
    etfs = ipy.etfs.get_etfs(country='united states')
    print(f"ETFs in US: {etfs}")

    # all symbols
    print(f"ETFs in US: {etfs['symbol']}")
    # get overview of top etfs


    all_etfs = ipy.etfs.get_etfs()
    print(f"Total ETFs retrieved: {len(all_etfs)}")

    # print all columns
    print(f"Columns: {all_etfs.columns}")


    is_schd_present = 'SCHD' in all_etfs['symbol'].values
    print(f"Is SCHD in the list: {is_schd_present}")

    is_aaa_present = 'AAA' in all_etfs['symbol'].values
    print(f"Is AAA in the list: {is_aaa_present}")

    aaa = ipy.etfs.search_etfs(by='symbol', value='AAA')
    print(f"AAA: {aaa}")

    # find schd
    schd = ipy.etfs.search_etfs(by='symbol', value='SCHD')
    print(f"SCHD: {schd}")

    '''



    # from all etfs, print the 10 largest market cap etfs

    # first we need to get the market cap of all etfs
    # with a seperate search for each etf

    # all_etfs is a dataframe, so we can iterate over it
    # and get the market cap for each etf
    def get_ticker_metadata(ticker: str) -> Dict[str, str]:
        """
        :param ticker: stock ticker
        :return: Dictionary containing some metadata
        """
        result = {"company_name": "not_found",
                "market_cap": "not_found"}
        import yfinance as yf
        try:
            info = yf.Ticker(ticker).info
            if info:
                if 'longName' in info:
                    result["company_name"] = info['longName']
                if "marketCap" in info:
                    result["market_cap"] = str(round((info['marketCap']/1000000000), 2)) + " blns$"
            else:
                print(f"Ticker {ticker} not found")
                return result

        except Exception as e:
            return result


        
        return result

    mkt_cap_list = []
    counter = 0

    # first create a ticker list
    # than use yf.tickers to get the market cap
    # list should be a single string with all tickers seperated by a space
    # than use yf.tickers to get the market cap

    starting_string = ''
    for etf in all_etfs['symbol']:
        starting_string += etf + ' '

    tickers = yf.Tickers(starting_string)

    '''

        # Prepare the string of all ETF symbols
    starting_string = ' '.join(all_etfs['symbol'])
    tickers = yf.Tickers(starting_string)

    # Function to extract market cap for each ticker
    def get_market_cap_info(ticker_obj) -> Dict[str, str]:
        """
        Retrieves the market cap and name for a given Ticker object.
        
        :param ticker_obj: Ticker object from yf.Tickers
        :return: Dictionary containing company name and market capitalization.
        """
        result = {"company_name": "not_found", "market_cap": "not_found"}
        try:
            info = ticker_obj.info
            if info:
                result["company_name"] = info.get('longName', "not_found")
                market_cap = info.get("marketCap")
                if market_cap:
                    result["market_cap"] = f"{round(market_cap / 1e9, 2)} blns$"
                else:
                    result["market_cap"] = "not_found"
            else:
                print(f"Ticker {ticker_obj.ticker} not found")
        except Exception as e:
            print(f"Error for ticker {ticker_obj.ticker}: {e}")
        
        return result

    mkt_cap_list = []
    # Iterate over each ticker in the tickers object
    for symbol, ticker_obj in tickers.tickers.items():
        metadata = get_market_cap_info(ticker_obj)
        if metadata['market_cap'] != 'not_found':
            #print(f"Company: {metadata['company_name']} Market Cap: {metadata['market_cap']}")
            mkt_cap_list.append(metadata)



    for company in mkt_cap_list:
        print(f"Company: {company['company_name']} Market Cap: {company['market_cap']}")




    

##### another library called etfpy
####### NOT WORKING SINCE 10.7.24 #######
'''

from etfpy import ETF, load_etf, get_available_etfs_list

etfs = get_available_etfs_list()

print(f"Available ETFs: {etfs}")

for etf in etfs:
    print (f"etf: {etf}")
    etf = load_etf(etf)

    print(f"ETF info: {etf.info}")
'''
