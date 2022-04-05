import yfinance as yf

# Request historical data for past 5 years
data = yf.Ticker("NVDA").history(period='5y')

# Show info
print(data.info())



"""
Write out a list of things the program will do.
"""
