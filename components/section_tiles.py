from dash import html
import dash_bootstrap_components as dbc

def section_tiles(section_order):
    return html.Div(
        [
            html.Div(
                dbc.Button(
                    dbc.Card(
                        dbc.CardBody(
                            html.Div(
                                [
                                    # DRAG HANDLE
                                    html.Span(
                                        "☰",
                                        className="drag-handle",
                                        title="Drag to reorder"
                                    ),

                                    # SECTION NAME
                                    html.Span(
                                        section,
                                        className="section-title"
                                    ),
                                ],
                                className="section-content"
                            )
                        ),
                        className="section-tile"
                    ),
                    id={"type": "open-section", "section": section},
                    color="light",
                    className="w-100 p-0 mb-2",
                    n_clicks=0
                ),
                id=f"section-{section}",
                className="draggable-item"
            )
            for section in section_order
        ],
        id="section-sortable-container"
    )
