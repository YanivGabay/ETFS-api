import yfinance as yf


spy = yf.Ticker("SPY")

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





