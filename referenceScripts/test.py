from dash import Dash,html
import dash_bootstrap_components as dbc

app= Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(dbc.Card(children=[html.H3(children='Testing next button',
                                               className="text-center"),
                                       dbc.Row([dbc.Col(dbc.Button("Global", href="./dashboard.py",
                                                                   color="primary"),
                                                        className="mt-3"),
                                                ], justify="center")
                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4")

        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)