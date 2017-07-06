from pandas_datareader import data
# https://github.com/ranaroussi/fix-yahoo-finance
# 야후 데이터 가져오는게 문제가 있어서 이걸 써줘야된다
import fix_yahoo_finance as yf

yf.pdr_override()  # <== that's all it takes :-)


class StockData:
    """
    arg stock = {
        "ticker": ticker_val, ...string
        "market": kospi, kosdaq, nasdaq, ...string
    }
    """
    def __init__(self):
        pass

    def format_ticker(stock):
        pass

    def _get_kospi(self, stock):  # conventional private naming
        ticker = stock['ticker']
        return data.get_data_google(ticker)

    def _get_kosdaq(self, stock):
        ticker = stock['ticker']
        return data.get_data_yahoo(ticker)

    def _get_nasdaq(self, stock):
        ticker = stock['ticker']
        return data.get_data_google(ticker)

    def error(self, stock):
        raise Exception('unexpected market name {}'.format(stock['market']))

    def get_csv(self, stock):
        mname = '_get_' + stock['market']
        if hasattr(self, mname):
            method = getattr(self, mname)
            return method(stock)
        else:
            self.error(stock)

stock_api = StockData()


class StockDataTester:
    def __init__(self):
        self.stocks = {
            'naver': {
                'ticker': 'KRX:035420',
                'market': 'kospi',
            },
            'apple': {
                'ticker': 'NASDAQ:AAPL',
                'market': 'nasdaq',
            },
            'afreeca tv': {
                'ticker': '067160.KQ',
                'market': 'kosdaq',
            },
        }

    def run(self):
        for stock in self.stocks.itervalues():
            print(stock_api.get_csv(stock).sample)


# stock_api_tester = StockDataTester()
# stock_api_tester.run()
