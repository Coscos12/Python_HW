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

load_dotenv()
API_KEY = os.environ.get('ALPHAVANTAGE_API_KEY')
last_table = pd.DataFrame()

STOCKS = {
    'Alibaba': 'BABA',
    'Alphabet': 'GOOGL',
    'Amazon': 'AMZN',
    'Apple': 'AAPL',
    'Facebook': 'FB'
}

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
for key in STOCKS:
    df = pd.read_csv(f'Aplhavantage/data/stocks/{key}_monthly.csv')
    df = df[(df["timestamp"] > '2020-01-01') & (df["timestamp"] < '2021-01-01')]
    df["name"] = f'{STOCKS[key]}'
    df = df[["timestamp", "name", "open", "high", "low", "close", "volume"]]
    last_table = pd.concat([last_table, df], axis=0)

app = dash.Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF',
    'plot_bgcolor':'#202020'
}

for key in STOCKS:
    fig = go.Figure(data=go.Scatter(x=last_table.timestamp, y=last_table.volume, mode='lines+markers',
                                    name=f'{STOCKS[key]}'))
    column = [{"name": ["date"], "id": "timestamp"},
              {"name": ["name"], "id": "name"},
              dict(name=["open"], id="open", type='numeric', format=Format(precision=2, scheme=Scheme.fixed)),
              dict(name=["low"], id="low", type='numeric', format=Format(precision=2, scheme=Scheme.fixed)),
              dict(name=["high"], id="high", type='numeric', format=Format(precision=2, scheme=Scheme.fixed)),
              dict(name=["close"], id="close", type='numeric', format=Format(precision=2, scheme=Scheme.fixed)),
              dict(name=["volume"], id="volume", type='numeric'),
              ]

tabs_styles = {
    'height': '50px',
    'vertical-align': 'middle'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
    'vertical-align': 'bottom'
}

tab_selected_style = {
    'borderTop': '2px solid #1d6791',
    'vertical-align': 'middle',
    'backgroundColor': '#000000',
    'color': '#FFFFFF',
    'padding': '6px',

}
fig.update_layout(
    plot_bgcolor=colors['plot_bgcolor'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div([
        dcc.Tabs(id="tabs-styled-with-inline", value='tab-1', children=[
            dcc.Tab(label='Tab 1', value='tab-1', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Tab 2', value='tab-2', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Tab 3', value='tab-3', style=tab_style, selected_style=tab_selected_style),
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
                style_header={'backgroundColor': 'rgb(30, 30, 30)'},
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
            html.H3('Tab content 2')
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Tab content 3')
        ])


if __name__ == '__main__':
    app.run_server(debug=True)
