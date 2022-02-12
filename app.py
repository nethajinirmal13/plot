import os
import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash(__name__)
server = app.server


app.layout = html.Div(children=[
    html.H1(children='Hello guvi'),
    html.H2(children='everyone is budding with plotly '),

    html.Div(children='''
        Dash: A web application framework for your data.this is d3 an d4
    '''),

  
])


if __name__ == '__main__':
    app.run_server(debug=True)
