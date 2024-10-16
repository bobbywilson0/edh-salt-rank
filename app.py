import re
from dash import Dash, html, dcc, callback, Output, Input, ClientsideFunction
import plotly.express as px
import pandas as pd

df = pd.read_json('./vis.json')
filtered_df = df[(df['edhrecRank'] <= 10000)]

app = Dash()
server = app.server


app.layout = [
    dcc.Graph(id='graph-content'),
    dcc.Textarea(
        id='decklist',
        value='Add cards here to filter the graph',
        style={'width': '100%', 'height': 300},
    ),
]

@callback(
    Output('graph-content', 'figure'),
    Input('decklist', 'value'),
)
def update_graph(value):
    if value == 'Add cards here to filter the graph' or value == '':
        updated_df = filtered_df
    else:
        cleaned_values = [re.sub(r'^\d+\s*', '', name.strip()) for name in value.split('\n')]
        updated_df = filtered_df[filtered_df['name'].isin(cleaned_values)]
    fig = px.scatter(updated_df, x='edhrecRank', y='edhrecSaltiness', title="Saltiness Vs EDHREC Rank", color_continuous_scale='portland', hover_name='name', color='edhrecSaltiness')
    fig.update_layout(xaxis=dict(autorange='reversed'))
    return fig

if __name__ == '__main__':
    app.run(debug=True)
