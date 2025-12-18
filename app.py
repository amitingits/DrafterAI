from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ALL
import dash

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

@app.callback(
    Output("section-modal", "is_open"),
    Output("modal-title", "children"),
    Output("section-input", "value"),   # 👈 IMPORTANT
    Output("resume-inputs", "data"),
    Input({"type": "open-section", "section": ALL}, "n_clicks"),
    Input("modal-save", "n_clicks"),
    Input("modal-cancel", "n_clicks"),
    State("section-modal", "is_open"),
    State("modal-title", "children"),
    State("section-input", "value"),
    State("resume-inputs", "data"),
    prevent_initial_call=True
)
def handle_section_modal(
        open_clicks,
        save_click,
        cancel_click,
        is_open,
        title,
        current_text,
        data
):
    ctx = dash.callback_context
    if not ctx.triggered:
        return is_open, title, current_text, data

    trigger = ctx.triggered[0]["prop_id"]
    data = data or {}

    # 1️⃣ Open modal from section tile
    if "open-section" in trigger:
        section = eval(trigger.split(".")[0])["section"]
        existing_text = data.get(section, "")
        return True, f"Add {section}", existing_text, data

    # 2️⃣ Save
    if trigger == "modal-save.n_clicks":
        section = title.replace("Add ", "")
        data[section] = current_text or ""
        return False, title, "", data

    # 3️⃣ Cancel
    if trigger == "modal-cancel.n_clicks":
        return False, title, "", data

    return is_open, title, current_text, data

if __name__ == "__main__":
    app.run(debug=True)
