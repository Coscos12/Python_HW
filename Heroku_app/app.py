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
app = dash.Dash(__name__)

last_table = pd.DataFrame()
last_table1 = pd.DataFrame()

fig = go.Figure()
fig1 = go.Figure()

for key in STOCKS:
    df = pd.read_csv(f'Aplhavantage/data/stocks/{key}_monthly.csv')
    df = df[(df["timestamp"] >= '2020-01-01') & (df["timestamp"] < '2021-01-01')]
    df["name"] = f'{STOCKS[key]}'

    df = df[["timestamp", "name", "open", "high", "low", "close", "volume"]]
    fig.add_trace(go.Scatter(x=df.timestamp, y=df.volume, mode='lines+markers',
                             name=f'{STOCKS[key]}', marker={'symbol': 'diamond', 'size': 10}))
    last_table = pd.concat([last_table, df], axis=0)

for key in CRYPTO:
    df = pd.read_csv(f'Aplhavantage/data/crypto/{key}_monthly.csv')
    df = df[(df["timestamp"] >= '2020-01-01') & (df["timestamp"] < '2021-01-01')]
    df["name"] = f'{CRYPTO[key]}'
    df = df[["timestamp", "name", "open (USD)", "high (USD)", "low (USD)", "close (USD)", "volume"]]
    df.columns = ["timestamp", "name", "open", "high", "low", "close", "volume"]
    fig1.add_trace(go.Scatter(x=df.timestamp, y=df.volume, mode='lines+markers',
                              name=f'{CRYPTO[key]}'))
    last_table1 = pd.concat([last_table1, df], axis=0)

df = pd.read_csv(f'Aplhavantage/data/technical/technical_monthly.csv')
df.columns = ['id', 'info', 'Real-Time', '1 Day', '5 Day', '1 Month', '3 Month',
              'Year-to-Date', '1 Year', '3 Year', '5 Year', '10 Year']
df = df.drop([0, 1])
df = df.drop(['info'], axis=1)
df.index = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
df = df.T
df = df.drop(['id'])
df.columns = ['Consumer Discretionary', 'Communication Services', 'Information Technology', 'Consumer Staples',
              'Materials', 'Industrials', 'Health Care', 'Financials', 'Energy', 'Real Estate', 'Utilities']
df['id'] = ['Real-Time', '1 Day', '5 Day', '1 Month', '3 Month',
            'Year-to-Date', '1 Year', '3 Year', '5 Year', '10 Year']
for i in df.columns:
    try:
        df[f'{i}'] = (df[f'{i}']).str.rstrip('%').astype('float')
    except ValueError:
        break
fig2 = go.Figure(data=[(go.Bar(name=df.columns[i], x=df.index, y=df[f'{df.columns[i]}']))
                       for i in range(len(df.columns) - 1)]
                 )

column = [dict(name=["date"], id="timestamp"),
          dict(name=["name"], id="name"),
          dict(name=["open"], id="open", type='numeric', format=dict(specifier='.4~f')),
          dict(name=["low"], id="low", type='numeric', format=dict(specifier='.4~f')),
          dict(name=["high"], id="high", type='numeric', format=dict(specifier='.4~f')),
          dict(name=["close"], id="close", type='numeric', format=dict(specifier='.4~f')),
          dict(name=["volume"], id="volume", type='numeric', format=Format(precision=2, scheme=Scheme.decimal_integer))
          ]
column1 = [dict(name=["period"], id="id"),
           dict(name=["Consumer Discretionary"], id="Consumer Discretionary"),
           dict(name=["Communication Services"], id="Communication Services"),
           dict(name=["Consumer Staples"], id="Consumer Staples"),
           dict(name=["Materials"], id="Materials"),
           dict(name=["Industrials"], id="Industrials"),
           dict(name=["Health Care"], id="Health Care"),
           dict(name=["Financials"], id="Financials"),
           dict(name=["Energy"], id="Energy"),
           dict(name=["Real Estate"], id="Real Estate"),
           dict(name=["Utilities"], id="Utilities")
           ]

fig.update_layout(
    plot_bgcolor=colors['plot_bgcolor'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    height=550,
    legend=style_legend
)
fig1.update_layout(
    plot_bgcolor=colors['plot_bgcolor'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    height=550,
    legend=style_legend
)
fig2.update_layout(
    plot_bgcolor=colors['plot_bgcolor'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    height=550,
    legend=style_legend
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
            # html.Div([
            #     html.H3('Tab content 3')
            # ]),
            html.Div([dcc.Graph(
                id='example-graph',
                figure=fig
            )],
                style={'width': '100%',
                       'height': '550px',
                       'height': '100%'
                       }),

            html.Div(dash_table.DataTable(
                id='table',
                columns=column,
                style_header=style_header,
                style_cell=style_cell,
                style_filter=style_filter,
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
                columns=column,
                style_header=style_header,
                style_cell=style_cell,
                style_filter=style_filter,
                data=last_table1.to_dict('records'),
                filter_action="native",
                sort_action="native",
                fixed_rows={'headers': True},
                style_table={'height': '500px', 'overflowY': 'auto'},
            ))
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.Div([dcc.Graph(
                id='example-graph2',
                figure=fig2
            )],
                style={'width': '100%',
                       }),
            html.Div(dash_table.DataTable(
                id='table2',
                columns=column1,
                style_header=style_header,
                style_cell=style_cell,
                style_filter=style_filter,
                data=df.to_dict('records'),
                filter_action="native",
                sort_action="native",
                fixed_rows={'headers': True},
                style_table={'height': '500px', 'overflowY': 'auto'},
            ))
        ])


if __name__ == '__main__':
    app.run_server(debug=True)
