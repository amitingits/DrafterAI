from dash import html
import dash_bootstrap_components as dbc
from stores.state import resume_stores
from components.section_modal import section_modal

def builder_layout():
    return dbc.Container(
        fluid=True,
        children=[
            *resume_stores(),

            dbc.Row([
                dbc.Col(
                    [
                        html.H4("Sections"),
                        html.Div(id="section-tiles-container"),
                        section_modal()
                    ],
                    width=4,
                    className="left-panel"
                ),

                dbc.Col(
                    [
                        html.H4("Resume Preview"),
                        dbc.Card(
                            dbc.CardBody(
                                "Preview will appear here."
                            ),
                            style={"minHeight": "80vh"}
                        )
                    ],
                    width=8,
                    className="right-panel"
                )
            ])
        ]
    )
