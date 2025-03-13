import dash
from dash import Dash, html, dcc

app = Dash(__name__, use_pages=True)

app.layout = html.Div([
    dash.page_container,

])

@app.callback(
    dash.dependencies.Output('url', 'href'),
    [dash.dependencies.Input('navigate-button', 'n_clicks')]
)
def navigate(n_clicks):
    if n_clicks:
        return '/not_home'
    return dash.no_update
@app.callback(
    dash.dependencies.Output('url2', 'href'),
    [dash.dependencies.Input('navigate-button2', 'n_clicks')]
)
def navigate2(n_clicks):
    if n_clicks:
        return '/'
    return dash.no_update
if __name__ == '__main__':
    app.run(debug=True)