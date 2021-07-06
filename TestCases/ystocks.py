import yfinance as yf

voda = yf.Ticker('IDEA.NS')
data = voda.history(period="50d")
print(data)