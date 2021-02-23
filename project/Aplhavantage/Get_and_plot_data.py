import pandas as pd
import concurrent.futures
import os
import time
from io import StringIO
import requests
from dotenv import load_dotenv

APLPHAVANTAGE_URL = "https://www.alphavantage.co/query?"
DATA_PATH_STOCKS = "data/stocks"
DATA_PATH_CRYPTO = "data/crypto"
DATA_PATH_TECH = "data/technical"
API_CALL_SLEEP_SEC = 60

load_dotenv()
API_KEY = os.environ.get('ALPHAVANTAGE_API_KEY')

STOCKS = {
    'Alibaba': 'BABA',
    'Alphabet': 'GOOGL',
    'Amazon': 'AMZN',
    'Apple': 'AAPL',
    'Facebook': 'FB',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Oracle': 'ORCL',
    'Tesla': 'TSLA',
    'Twitter': 'TWTR'
}

CRYPTO = {
    'Bitcoin': 'BTC',
    'EOS': 'EOS',
    'Ethereum': 'ETH',
    'NEO': 'NEO',
    'Ripple': 'XRP'
}

TECHNICAL = {
    'technical': 'TCHN'
}

MARKETS = {
    'United States Dollar': 'USD'
}


def get_crypto_data(session, name, symbol, market, api_key, function, datatype):
    params = {
        "function": function,
        "symbol": symbol,
        "market": market,
        "apikey": api_key,
        "datatype": datatype
    }
    print(f"Getting {name} crypto currency")

    response = session.get(APLPHAVANTAGE_URL, params=params)

    if "5 calls per minute and 500 calls per day" in response.text:
        print("wait")
        time.sleep(API_CALL_SLEEP_SEC)
        response = session.get(APLPHAVANTAGE_URL, params=params)

    if response.status_code == requests.codes.ok:
        df = pd.read_csv(StringIO(response.text))
        df.to_csv(os.path.join(
            os.path.dirname(__file__),
            f'{DATA_PATH_CRYPTO}/{name}_monthly.csv'
        ))
        print(f'{name} OK')
    else:
        raise Exception(response.status_code, response.reason)


def get_stock_data(session, name, symbol, api_key, function, datatype):
    params = {
        "function": function,
        "symbol": symbol,
        "apikey": api_key,
        "datatype": datatype
    }
    print(f"Getting {name}")

    response = session.get(APLPHAVANTAGE_URL, params=params)

    if "5 calls per minute and 500 calls per day" in response.text:
        print("wait")
        time.sleep(API_CALL_SLEEP_SEC)
        response = session.get(APLPHAVANTAGE_URL, params=params)

    if response.status_code == requests.codes.ok:
        df = pd.read_csv(StringIO(response.text))
        df.to_csv(os.path.join(
            os.path.dirname(__file__),
            f'{DATA_PATH_STOCKS}/{name}_monthly.csv'
        ))
        print(f'{name} OK')
    else:
        raise Exception(response.status_code, response.reason)


def get_technical_data(session, name, api_key, function, datatype):
    params = {
        "function": function,
        "apikey": api_key,
        "datatype": datatype
    }
    print(f"Getting {name}")

    response = session.get(APLPHAVANTAGE_URL, params=params)

    if "5 calls per minute and 500 calls per day" in response.text:
        print("wait")
        time.sleep(API_CALL_SLEEP_SEC)
        response = session.get(APLPHAVANTAGE_URL, params=params)

    if response.status_code == requests.codes.ok:
        print(f'{name} trying')
        df = pd.read_json(StringIO(response.text))
        df.to_csv(os.path.join(
            os.path.dirname(__file__),
            f'{DATA_PATH_TECH}/{name}_monthly.csv'
        ))
        print(f'{name} OK')
    else:
        raise Exception(response.status_code, response.reason)


if __name__ == "__main__":

    start = time.perf_counter()
    session = requests.Session()

    if not API_KEY:
        raise Exception(
            f'Missing config wit api key'
        )

    # for name, symbol in STOCKS.items():
    #     monthly_stock_df = get_stock_data(
    #         session, name, symbol, API_KEY, "TIME_SERIES_MONTHLY", "csv"
    #     )
    #
    # _args = (
    #     (session, name, symbol, API_KEY, "TIME_SERIES_MONTHLY", "csv")
    #     for name, symbol in STOCKS.items()
    # )
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     executor.map(lambda p: get_stock_data(*p), _args)
    #
    _args = (
        (session, name, symbol, MARKETS['United States Dollar'], API_KEY, "DIGITAL_CURRENCY_MONTHLY", "csv")
        for name, symbol in CRYPTO.items()
    )
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(lambda p: get_crypto_data(*p), _args)

    # monthly_stock_df = get_technical_data(
    #             session, "technical", API_KEY, "SECTOR", "csv"
    #             )
    # _args = (
    #     (session, name, symbol, API_KEY, "SECTOR")
    #     for name, symbol in TECHNICAL.items()
    # )
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     executor.map(lambda p: get_technical_data(*p), _args)

    finish = time.perf_counter()
    # app.run_server(debug=True)

    print(f'Finished in {round(finish - start, 2)} second')
