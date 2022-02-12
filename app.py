import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


app = dash.Dash(__name__)
server = app.server
df = pd.read_csv('https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/usa-agricultural-exports-2011.csv')


def generate_table(dataframe, max_rows=100):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app = JupyterDash(__name__)

app.layout = html.Div([
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)
])


if __name__ == '__main__':
    app.run_server(debug=True)
