# -*- coding:utf-8 -*-
from pandas_datareader import data
# https://github.com/ranaroussi/fix-yahoo-finance
import fix_yahoo_finance as yf
import os

yf.pdr_override()  # <== that's all it takes :-)


class StockData:
    def __init__(self):
        pass

    def _get_path(self, ticker, market, base_dir='./app/data/prices'):
        path = os.path.join(base_dir, "{}/{}.csv".format(
            market,
            str(ticker)
        ))
        return path

    def _get_kospi_csv(self, ticker):  # conventional private naming
        #ticker = 'KRX:' + str(ticker)
        #return data.get_data_google(ticker, start='1996-05-06')
        ticker = str(ticker) + '.KS'
        return data.get_data_yahoo(ticker, start='1996-05-06', thread=20)

    def _get_kosdaq_csv(self, ticker):
        ticker = str(ticker) + '.KQ'
        return data.get_data_yahoo(ticker, start='1996-05-06', thread=2)

    def _get_nasdaq_csv(self, ticker):
        return data.get_data_google(ticker, start='1996-05-06')

    def error(self, market):
        raise Exception('unexpected market name {}'.format(market))

    def get_csv(self, ticker, market):
        market = str(market).lower()
        mname = '_get_' + market + '_csv'
        if hasattr(self, mname):
            method = getattr(self, mname)
            return method(ticker)
        else:
            self.error(market)

    def save_csv(self, ticker, market, df, path = None):
        market = str(market).lower()
        path = self._get_path(ticker, market)
        df.to_csv(path)

