import dash
from dash import Dash, html, dcc
import pandas as pd
import plotly.graph_objects as go

app = Dash(__name__, use_pages=True)

app.layout = html.Div([
    dash.page_container,

])
@app.callback(
    dash.dependencies.Output("graph", "children"),
    dash.dependencies.Output("navigate-button", "style"),
    dash.dependencies.Input("populate_div", "n_clicks"),
    prevent_initial_call=True
)
def populateDiv(click):
    df_industrial = pd.read_csv("./Balassa_Mod_Nivel_Municipio_por_Grupos_2015.csv")
    feature = {"properties": {"CVE_MUN": "001", "NOM_MUN": 'Acatlán'}}
    if not feature:
        return [html.P("Selecciona un municipio")]
    nombre = feature["properties"]["CVE_MUN"]
    row = df_industrial[df_industrial['cve_mun'] == int(nombre)].iloc[:, 2:]
    if row.empty:
        return [html.P(f"No data available for {nombre}")]
    data = row.iloc[0].to_dict()
    data = {k: (0 if pd.isna(v) else v) for k, v in data.items()}
    data = dict(sorted(data.items(), key=lambda item: item[1], reverse=True)[:5])
    x = list(data.keys())
    y = list(data.values())

    y = [round(val, 2) if val >= 0.01 else "<0.01" for val in y]

    fig = go.Figure(
        data=go.Bar(
            x=y,
            y=x,
            orientation='h',
            width=0.5,
            offset=-0.65,
            texttemplate="%{x}"
        ),
        layout={
            'title': {
                'text': f'Industrias con mayor personal en <br> {feature["properties"]["NOM_MUN"]} ()',
                'font': {'size': 10},
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top',
            },
            'height': 300,
            'yaxis': {'anchor': 'free', 'side': 'right'},
        }
    )
    return [dcc.Graph(figure=fig.update_layout(
        margin=dict(l=20, r=20, t=30, b=20),
    ), style={'height': '300px', 'width': '350px'}), {"display": "block"}]
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