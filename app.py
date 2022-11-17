
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('data\daily_sales_data.csv')
df.sort_values('date')
colors = {
    'background': '#111111',
    'text': '#7FDBFF',
}

fig = px.line(df, x='date', y='sales', color='region', height=650)

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(children=[
    html.H1(children="Analytics of Pink Morsels", style={'textAlign':'center'}),
    html.P(
        children="Analysis of the behavior of Pink Morsels prices over time",
        style={'textAlign':'center'}
    ),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
