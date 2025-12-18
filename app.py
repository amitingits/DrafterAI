from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from pages.landing import landing_layout
from pages.builder import builder_layout

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)

server = app.server  # for deployment

app.layout = html.Div([
    dcc.Location(id="url"),
    html.Div(id="page-content")
])

@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def route_pages(pathname):
    if pathname == "/builder":
        return builder_layout()
    return landing_layout()

if __name__ == "__main__":
    app.run(debug=True)
