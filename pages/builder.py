from dash import html, dcc
import dash_bootstrap_components as dbc

from components.section_tiles import section_tiles
from components.section_modal import section_modal
from stores.state import resume_stores

def builder_layout():
    return dbc.Container(
        fluid=True,
        children=[
            *resume_stores(),

            dbc.Row([
                # LEFT PANEL
                dbc.Col(
                    [
                        html.H4("Sections"),
                        section_tiles(),
                        section_modal()
                    ],
                    width=4,
                    className="left-panel"
                ),

                # RIGHT PANEL (PREVIEW PLACEHOLDER)
                dbc.Col(
                    [
                        html.H4("Resume Preview"),
                        dbc.Card(
                            dbc.CardBody(
                                html.P(
                                    "Preview will appear here after generation.",
                                    className="text-muted"
                                )
                            ),
                            style={"minHeight": "80vh"}
                        ),
                    ],
                    width=8,
                    className="right-panel"
                )
            ]),


        ]
    )
