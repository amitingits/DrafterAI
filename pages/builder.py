from dash import html
import dash_bootstrap_components as dbc

def builder_layout():
    return dbc.Container(
        fluid=True,
        children=[
            dbc.Row(
                dbc.Col(
                    html.H2("Resume Builder Dashboard"),
                    width=12
                )
            ),
            dbc.Row(
                dbc.Col(
                    html.P("Phase 2 will implement the editor and preview."),
                    width=12
                )
            )
        ]
    )
