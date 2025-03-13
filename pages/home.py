import dash
from dash import html
from dash import dcc

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1('This is our Home page'),
    html.Div('This is our Home page content.'),
    html.Button('Go to Not Home', id='navigate-button'),
    dcc.Location(id='url', refresh=True)
])
