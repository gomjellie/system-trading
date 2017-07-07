from .api import stock_api
import pandas as pd
import glob
import re

kosdaq_df = pd.read_pickle('./app/data/name_ticker/pickle/kosdaq.pickle')
kospi_df = pd.read_pickle('./app/data/name_ticker/pickle/kospi.pickle')


def save_kosdaq():
    for stock in kosdaq_df.values:
        kor_name = stock[0]
        ticker = stock[1]

        tmp_df = stock_api.get_csv(ticker, 'kosdaq')
        stock_api.save_csv(ticker, 'kosdaq', tmp_df)


def save_kospi():
    for stock in kospi_df.values:
        kor_name = stock[0]
        ticker = stock[1]

        tmp_df = stock_api.get_csv(ticker, 'kospi')
        stock_api.save_csv(ticker, 'kospi', tmp_df)

# save_kosdaq()


def reload_kospi():
    kospi_file_list = glob.glob('./app/data/prices/kospi/*.csv')
    six_digit = re.compile('\d{6}')

    for file_name in kospi_file_list:
        file = pd.read_csv('{}'.format(file_name))
        if file.empty:
            print("saved {}".format(file_name))
            ticker = six_digit.findall(file_name)[0]
            tmp_df = stock_api.get_csv(ticker, 'kospi')
            stock_api.save_csv(ticker, 'kospi', tmp_df)


def reload_kosdaq():
    kosdaq_file_list = glob.glob('./app/data/prices/kosdaq/*.csv')
    six_digit = re.compile('\d{6}')

    for file_name in kosdaq_file_list:
        file = pd.read_csv('{}'.format(file_name))
        if file.empty:
            print("saved {}".format(file_name))
            ticker = six_digit.findall(file_name)[0]
            tmp_df = stock_api.get_csv(ticker, 'kodsaq')
            stock_api.save_csv(ticker, 'kodsaq', tmp_df)


reload_kosdaq()
# save_kospi()
# reload_kosdaq()


