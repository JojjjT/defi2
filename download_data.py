import yfinance as yf

tickers = ["AAPL", "MSFT", "GOOG", "AMZN", "TSLA", "NVDA", "META", "JPM", "V", "JNJ"]

prices = yf.download(tickers, start="2020-01-01", end="2025-01-01", auto_adjust=True)["Close"].dropna()
prices.to_parquet("data/prices.parquet")

print(f"Listo: {prices.shape[0]} filas x {prices.shape[1]} tickers guardados en data/prices.parquet")
