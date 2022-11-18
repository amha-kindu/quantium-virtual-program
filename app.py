import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

app = Dash(__name__)
df = pd.read_csv('data\daily_sales_data.csv')
df.sort_values('date')

tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

def build_graph(df):
    return px.line(df, x='date', y='sales', height=650, width=1300)

app.layout = html.Div([
    html.H1(id='header', children="Pink morsel price visualizer", style={'textAlign':'center'}),
    dcc.Tabs(id="region-picker", value='all', children=[
        dcc.Tab(label='All', value='all'),
        dcc.Tab(label='North', value='north'),
        dcc.Tab(label='South', value='south'),
        dcc.Tab(label='East', value='east'),
        dcc.Tab(label='West', value='west'),
    ], style=tab_style),
    html.Div(id='graph-container', children=[dcc.Graph(id='graph', figure=build_graph(df))], 
    )
])


@app.callback(Output('graph-container', 'children'),
              Input('region-picker', 'value'))
def render_graph(tab):
    m = df if tab=='all' else df[df['region']==tab]
    return  dcc.Graph(figure = build_graph(m), id='graph')
    

if __name__ == '__main__':
    app.run_server(debug=True)
