'''import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
 
USERNAME_PASSWORD_PAIRS = [
    ['nethu', '12345'],['guvi', 'guvi'],['tejas','tejas']
]
 
app = dash.Dash()
auth = dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)
server = app.server
 
app.layout = html.Div([
    dcc.RangeSlider(
        id='range-slider',
        min=-5,
        max=6,
        marks={i:str(i) for i in range(-5, 7)},
        value=[-3, 4]
    ),
    html.H1(id='product')  # this is the output
], style={'width':'50%'})
 
@app.callback(
    Output('product', 'children'),
    [Input('range-slider', 'value')])
def update_value(value_list):
    return value_list[0]*value_list[1]
 
if __name__ == '__main__':
    app.run_server(debug=True)'''


import plotly.express as px
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# Load Data
df = px.data.tips()
# Build App
app = JupyterDash(__name__)
server = app.server
app.layout = html.Div([
    html.H1("JupyterDash Demo"),
    dcc.Graph(id='graph'),
    html.Label([
        "colorscale",
        dcc.Dropdown(
            id='colorscale-dropdown', clearable=False,
            value='plasma', options=[
                {'label': c, 'value': c}
                for c in px.colors.named_colorscales()
            ])
    ]),
])
# Define callback to update graph
@app.callback(
    Output('graph', 'figure'),
    [Input("colorscale-dropdown", "value")]
)
def update_figure(colorscale):
    return px.scatter(
        df, x="total_bill", y="tip", color="size",
        color_continuous_scale=colorscale,
        render_mode="webgl", title="Tips"
    )
# Run app and display result inline in the notebook
if __name__ == '__main__':
    app.run_server(debug=True)
