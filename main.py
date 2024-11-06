import yfinance as yf


spy = yf.Ticker("SPY")
data = spy.funds_data

#lets print the size of the spy variable
print(f'size of spy: {len(spy)}')

#lets print the size of the data variable
print(f'size of data: {len(data)}')



# lets print alot of data to understand what we are working with
def print_data(data: property):
    for key in data:
        print(f'{key}: {data[key]}')

print_data(data)