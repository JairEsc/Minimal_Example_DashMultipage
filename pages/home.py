import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/')
info_home=html.Div(children=[html.Div("Grafo",id='graph'),html.Button('Go to not Home', id='navigate-button',style={"display":'none'}),
    dcc.Location(id='url', refresh=True)],id='div')
layout = html.Div([
    html.H1('This is our Home page'),
    html.Div('This is our Home page content.'),
    html.Button('Populate div. Graph+button', id='populate_div'),
    info_home,
    dcc.Location(id='url', refresh=True)
])
