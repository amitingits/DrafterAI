from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State, ALL
from dash_extensions import EventListener
import dash_bootstrap_components as dbc
import dash

from pages.landing import landing_layout
from pages.builder import builder_layout
from components.section_tiles import section_tiles


# -------------------------
# APP INITIALIZATION
# -------------------------
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)

server = app.server


# -------------------------
# APP LAYOUT
# -------------------------
app.layout = html.Div(
    [
        dcc.Location(id="url"),

        # JS → Dash bridge for drag-and-drop
        EventListener(
            id="section-order-listener",
            events=[{"event": "sectionOrderChanged"}],
        ),

        html.Div(id="page-content"),
    ]
)


# -------------------------
# ROUTING: LANDING → BUILDER
# -------------------------
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
)
def route_pages(pathname):
    if pathname == "/builder":
        return builder_layout()
    return landing_layout()


# -------------------------
# RENDER SECTION TILES
# -------------------------
@app.callback(
    Output("section-tiles-container", "children"),
    Input("section-order", "data"),
)
def render_section_tiles(section_order):
    if not section_order:
        return html.Div("No sections available")
    return section_tiles(section_order)


# -------------------------
# UPDATE SECTION ORDER (DRAG & DROP)
# -------------------------
@app.callback(
    Output("section-order", "data"),
    Input("section-order-listener", "event"),
    State("section-order", "data"),
    prevent_initial_call=True,
)
def update_section_order(event, current_order):
    if not event or "detail" not in event:
        return current_order

    # IDs come as: section-Experience, section-Projects, ...
    new_order = [item.replace("section-", "") for item in event["detail"]]
    return new_order


# -------------------------
# SECTION MODAL HANDLER
# -------------------------
@app.callback(
    Output("section-modal", "is_open"),
    Output("modal-title", "children"),
    Output("section-input", "value"),
    Output("resume-inputs", "data"),
    Input({"type": "open-section", "section": ALL}, "n_clicks"),
    Input("modal-save", "n_clicks"),
    Input("modal-cancel", "n_clicks"),
    State("section-modal", "is_open"),
    State("modal-title", "children"),
    State("section-input", "value"),
    State("resume-inputs", "data"),
    prevent_initial_call=True,
)
def handle_section_modal(
        open_clicks,
        save_click,
        cancel_click,
        is_open,
        title,
        current_text,
        data,
):
    ctx = dash.callback_context
    if not ctx.triggered:
        return is_open, title, current_text, data

    trigger = ctx.triggered[0]["prop_id"]
    data = data or {}

    # ---- OPEN MODAL ----
    if "open-section" in trigger:
        section = eval(trigger.split(".")[0])["section"]
        existing_text = data.get(section, "")
        return True, f"Add {section}", existing_text, data

    # ---- SAVE ----
    if trigger == "modal-save.n_clicks":
        section = title.replace("Add ", "")
        data[section] = current_text or ""
        return False, title, "", data

    # ---- CANCEL ----
    if trigger == "modal-cancel.n_clicks":
        return False, title, "", data

    return is_open, title, current_text, data


# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
