from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

df = pd.read_pickle('mergedDataFrame.pkl')

external_stylesheets = [dbc.themes.LUX]
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = dbc.Container([
    dbc.Row([
        dcc.Dropdown(df['test_period'].unique()[1:], 'Field_1', id='dropdown-xaxis-selection'),
        dcc.Dropdown(['R2', 'R3', 'R2v', 'R3v', 'I1', 'I2', 'I3'], 'R3', id='dropdown-yaxis-column')
    ]),
    dbc.Row([
        dcc.Graph(id='graph-content')
    ])
], fluid=True)


@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-xaxis-selection', 'value'),
    Input('dropdown-yaxis-column', 'value')
)
def update_graph(test_period_selection, yaxis_column_name):
    dff = df.loc[df['test_period'] == test_period_selection]
    return px.line(dff, x=dff.index, y=[yaxis_column_name+'_2', yaxis_column_name+'_3'])


if __name__ == '__main__':
    app.run_server(debug=True)
