import dash_bootstrap_components as dbc
from dash import html, dcc

def section_modal():
    return dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle(id="modal-title")),
            dbc.ModalBody(
                dcc.Textarea(
                    id="section-input",
                    style={"width": "100%", "height": "180px"}
                )
            ),
            dbc.ModalFooter([
                dbc.Button("Cancel", id="modal-cancel", color="secondary"),
                dbc.Button("Save", id="modal-save", color="primary")
            ])
        ],
        id="section-modal",
        is_open=False
    )
