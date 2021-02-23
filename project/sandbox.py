import dash
import dash_table
import pandas as pd
import os
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_html_components as html
import plotly.express as px
from dash_table.Format import Format, Scheme
from dotenv import load_dotenv
import plotly.graph_objects as go

from styles import *
from names import *

load_dotenv()
API_KEY = os.environ.get('ALPHAVANTAGE_API_KEY')

last_table = pd.DataFrame()
last_table1 = pd.DataFrame()

fig = go.Figure()
fig1 = go.Figure()

for key in STOCKS:
    df = pd.read_csv(f'C:/Users/213/Documents/GitHub/Python_HW/project/Aplhavantage/data/stocks/{key}_monthly.csv')
    df = df[(df["timestamp"] >= '2020-01-01') & (df["timestamp"] < '2021-01-01')]
    df["name"] = f'{STOCKS[key]}'
    df = df[["timestamp", "name", "open", "high", "low", "close", "volume"]]
    fig.add_trace(go.Scatter(x=df.timestamp, y=df.volume, mode='lines+markers',
                             name=f'{STOCKS[key]}'))
    last_table = pd.concat([last_table, df], axis=0)

for key in CRYPTO:
    df = pd.read_csv(f'C:/Users/213/Documents/GitHub/Python_HW/project/Aplhavantage/data/crypto/{key}_monthly.csv')
    df = df[(df["timestamp"] >= '2020-01-01') & (df["timestamp"] < '2021-01-01')]
    df["name"] = f'{CRYPTO[key]}'
    df = df[["timestamp", "name", "open (USD)", "high (USD)", "low (USD)", "close (USD)", "volume"]]
    fig1.add_trace(go.Scatter(x=df.timestamp, y=df.volume, mode='lines+markers',
                             name=f'{CRYPTO[key]}'))
    last_table1 = pd.concat([last_table1, df], axis=0)

app = dash.Dash(__name__)

column = [{"name": ["date"], "id": "timestamp"},
          {"name": ["name"], "id": "name"},
          dict(name=["open"], id="open", type='numeric', format=Format(precision=2, scheme=Scheme.fixed)),
          dict(name=["low"], id="low", type='numeric', format=Format(precision=2, scheme=Scheme.fixed)),
          dict(name=["high"], id="high", type='numeric', format=Format(precision=2, scheme=Scheme.fixed)),
          dict(name=["close"], id="close", type='numeric', format=Format(precision=2, scheme=Scheme.fixed)),
          dict(name=["volume"], id="volume", type='numeric'),
          ]

column1 = [{"name": ["date"], "id": "timestamp"},
          {"name": ["name"], "id": "name"},
          dict(name=["open"], id="open (USD)", type='numeric', format=Format(precision=2, scheme=Scheme.fixed)),
          dict(name=["low"], id="low (USD)", type='numeric', format=Format(precision=2, scheme=Scheme.fixed)),
          dict(name=["high"], id="high (USD)", type='numeric', format=Format(precision=2, scheme=Scheme.fixed)),
          dict(name=["close"], id="close (USD)", type='numeric', format=Format(precision=2, scheme=Scheme.fixed)),
          dict(name=["volume"], id="volume", type='numeric'),
          ]

fig.update_layout(
    plot_bgcolor=colors['plot_bgcolor'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
fig1.update_layout(
    plot_bgcolor=colors['plot_bgcolor'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
app.layout = html.Div(style={'backgroundColor': colors['background'], 'border': '1px solid #000000',
                             'padding': '1px'}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'font-size': '3rem',
            'margin-top': '0px',
            'color': colors['text']
        }
    ),
    html.Div([
        dcc.Tabs(id="tabs-styled-with-inline", value='tab-1', children=[
            dcc.Tab(label='Stocks', value='tab-1', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Crypto', value='tab-2', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Performance', value='tab-3', style=tab_style, selected_style=tab_selected_style),
        ], style=tabs_styles),
        html.Div(id='tabs-content-inline')
    ])
])


@app.callback(Output('tabs-content-inline', 'children'),
              Input('tabs-styled-with-inline', 'value'))

def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.Div([dcc.Graph(
                id='example-graph',
                figure=fig
            )],
                style={'width': '100%',
                       }),

            html.Div(dash_table.DataTable(
                id='table',
                columns=column,
                style_header={'backgroundColor': '#E9967A',
                              'color': '#000000'},
                style_cell={
                    'backgroundColor': 'rgb(0, 0, 0)',
                    'color': 'white',
                    'textAlign': 'center'
                },
                data=last_table.to_dict('records'),
                filter_action="native",
                sort_action="native",
                fixed_rows={'headers': True},
                style_table={'height': '500px', 'overflowY': 'auto'},
            ))
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.Div([dcc.Graph(
                id='example-graph1',
                figure=fig1
            )],
                style={'width': '100%',
                       }),

            html.Div(dash_table.DataTable(
                id='table',
                columns=column1,
                style_header={'backgroundColor': '#E9967A',
                              'color': '#000000'},
                style_cell={
                    'backgroundColor': 'rgb(0, 0, 0)',
                    'color': 'white',
                    'textAlign': 'center'
                },
                data=last_table1.to_dict('records'),
                filter_action="native",
                sort_action="native",
                fixed_rows={'headers': True},
                style_table={'height': '500px', 'overflowY': 'auto'},
            ))
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Tab content 3')
        ])


if __name__ == '__main__':
    app.run_server(debug=True)
