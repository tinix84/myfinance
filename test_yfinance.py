import yfinance as yf
import pprint

def test_yfinance_download():
    data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30", group_by="ticker")

def test_yfinance_msft():
    msft = yf.Ticker("MSFT")

    print(msft)

    # get stock info
    print(msft.info)

    # get historical market data
    print(msft.history(period="max"))

    # show actions (dividends, splits)
    print(msft.actions)

    # show dividends
    print(msft.dividends)

    # show splits
    print(msft.splits)

if __name__ == "__main__":
    test_yfinance_msft()