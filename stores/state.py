from dash import dcc
from config.sections import SECTIONS
def resume_stores():
    return [
        dcc.Store(id="resume-inputs", data={}),
        dcc.Store(id="resume-generated", data=False),
        dcc.Store(id="section-order", data=SECTIONS.copy())
    ]
