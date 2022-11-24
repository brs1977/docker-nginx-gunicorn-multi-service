import numpy as np
import pandas as pd

import dash
import dash_html_components as html


app = dash.Dash()

server = app.server

app.layout = html.Div([
    html.Div('Hello питон'),
])

if __name__ == '__main__':
    app.run_server(host= '0.0.0.0', port=8015,debug=True)
