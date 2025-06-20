import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv("diabetes.csv")

# Create Dash app
app = dash.Dash(__name__)
app.title = "Diabetes Dashboard"

# Layout of the dashboard
app.layout = html.Div(children=[
    html.H1("Diabetes Dashboard", style={'textAlign': 'center'}),

    dcc.Graph(
        id='pie-chart',
        figure=px.pie(df, names='Outcome', title='Diabetes vs Non-Diabetes')
    ),

    dcc.Graph(
        id='boxplot',
        figure=px.box(df, x='Outcome', y='Glucose', title='Glucose Distribution by Outcome')
    ),

    dcc.Graph(
        id='scatter',
        figure=px.scatter(df, x='Age', y='Glucose', color='Outcome',
                          title='Age vs Glucose by Outcome')
    )
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
