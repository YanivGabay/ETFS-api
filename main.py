import yfinance as yf


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
