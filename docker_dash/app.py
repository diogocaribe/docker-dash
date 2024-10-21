import secrets

import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, callback, dcc, html
from werkzeug.middleware.proxy_fix import ProxyFix

from docker_dash.settings import Settings

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv'
)

settings = Settings()

app = Dash(__name__)

server = app.server
server.secret_key = secrets.token_urlsafe(16)
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

app.layout = html.Div(
    [
        html.H1(children='Title of Dash App', style={'textAlign': 'center'}),
        dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
        dcc.Graph(id='graph-content'),
    ]
)


@callback(
    Output('graph-content', 'figure'), Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country == value]
    return px.line(dff, x='year', y='pop')


if __name__ == '__main__':
    app.run(port=8050, host="0.0.0.0", debug=settings.DASH_DEBUG_MODE)
