from dash import html, dcc
import dash_bootstrap_components as dbc

def landing_layout():
    return dbc.Container(
        fluid=True,
        className="landing-container",
        children=[
            dbc.Row(
                dbc.Col(
                    [
                        html.H1("Build Your Resume with AI", className="hero-title"),
                        html.P(
                            "Convert free-form text into a professional, ATS-ready resume with real-time preview and full control.",
                            className="hero-subtitle"
                        ),
                        dbc.Button(
                            "Create Resume Now",
                            href="/builder",
                            color="primary",
                            size="lg",
                            className="cta-btn"
                        )
                    ],
                    width=8
                ),
                justify="center",
                align="center",
                style={"minHeight": "100vh"}
            )
        ]
    )
