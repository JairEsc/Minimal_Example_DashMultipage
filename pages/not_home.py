import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(
    __name__,
    path='/not_home',
    title='Otro titulo',
    name='Otro nombre'
)

layout = html.Div([
    html.H1('This is an altern page'),
    html.Button('Go to Home', id='navigate-button2'),
    dcc.Location(id='url2', refresh=True)
])
