from dash import dcc

def resume_stores():
    return [
        dcc.Store(id="resume-inputs", data={}),
        dcc.Store(id="resume-generated", data=False),
        dcc.Store(id="section-order", data=[
            "Summary", "Experience", "Projects",
            "Education", "Skills", "Certifications"
        ])
    ]
