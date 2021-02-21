import dash
import dash_html_components as html
import pandas as pd
import dash_core_components as dcc
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import plotly.express as px

import os
import time
from io import StringIO
import requests
from dotenv import load_dotenv

APLPHAVANTAGE_URL = "https://www.alphavantage.co/query?"
DATA_PATH = "data/stocks"
API_CALL_SLEEP_SEC = 60

load_dotenv()
API_KEY = os.environ.get('ALPHAVANTAGE_API_KEY')

STOCKS = {
    'Alibaba': 'BABA',
    'Alphabet': 'GOOGL',
    'Amazon': 'AMZN',
    'Apple': 'AAPL',
    'Facebook': 'FB'
}


df = pd.read_csv('Aplhavantage/data/stocks/Alibaba_monthly.csv', parse_dates=["timestamp"])
# df1 = pd.read_csv('Aplhavantage/data/stocks/Alphabet_monthly.csv')
# df2 = pd.read_csv('Aplhavantage/data/stocks/Amazon_monthly.csv')
# df3 = pd.read_csv('Aplhavantage/data/stocks/Apple_monthly.csv')
# df4 = pd.read_csv('Aplhavantage/data/stocks/Facebook_monthly.csv')

# def generate_table(dataframe, max_rows=10):
#     return html.Table([
#         # html.Thead(
#         #     html.Tr([html.Th(col) for col in dataframe.columns])
#         # ),
#         html.Tbody([
#             html.Tr([
#                 html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
#             ]) for i in range(min(len(dataframe), max_rows))
#         ])
#     ])
#
#
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# app.layout = html.Div(children=[
#     html.H4(children='US Agriculture Exports (2011)'),
#     generate_table(df)
# ])

# fig = px.line(data = go.Scatter(x = df["timestamp"], y = df["open"]))
# fig = go.Figure()
# fig.add_trace(
#     go.Scatter(
#         x=dfn['timestamp'],
#         y=dfn['open'],
#         mode='lines+markers',
#         name='Alibaba'
#     ))
#
# fig.add_trace(
#     go.Scatter(
#         x=df1n['timestamp'],
#         y=df1n['open'],
#         mode='lines+markers',
#         name='Alphabet'
#
#     ))
# fig.add_trace(
#     go.Scatter(
#         x=df2['timestamp'],
#         y=df2['open'],
#         mode='lines+markers'
#     ))
# fig.add_trace(
#     go.Scatter(
#         x=df3['timestamp'],
#         y=df3['open'],
#         mode='lines+markers'
#     ))
# fig.add_trace(
#     go.Scatter(
#         x=df4['timestamp'],
#         y=df4['open'],
#         mode='lines+markers'
#     ))


# fig.show()



# app = dash.Dash(__name__)

# app.layout = html.Div([
#     dcc.Graph(id="graph", figure=fig),
#     html.Pre(
#         id='structure',
#         style={
#             'border': 'thin lightgrey solid',
#             'overflowY': 'scroll',
#             'height': '275px'
#         }
#     )
# ])

if __name__ == "__main__":

    start = time.perf_counter()
    # session = requests.Session()
    #
    # for name, symbol in STOCKS.items():
    #     monthly_stock_df = get_stock_data(
    #         session, name, symbol, API_KEY, "TIME_SERIES_MONTHLY", "csv"
    #     )
    # app.run_server(debug=True)
    print(df["timestamp"].min() - df["timestamp"].max())
    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second')