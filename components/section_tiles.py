from dash import html
import dash_bootstrap_components as dbc

SECTIONS = [
    "Summary",
    "Experience",
    "Projects",
    "Education",
    "Skills",
    "Certifications"
]

def section_tiles():
    tiles = []

    for sec in SECTIONS:
        tiles.append(
            dbc.Button(
                dbc.Card(
                    dbc.CardBody(sec),
                    className="section-tile"
                ),
                id={"type": "open-section", "section": sec},
                color="light",
                className="w-100 p-0",
                n_clicks=0
            )
        )

    return dbc.Row(
        [dbc.Col(tile, width=6) for tile in tiles],
        className="g-2"
    )
