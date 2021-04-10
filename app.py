# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import psycopg2

from sql_queries import *

# Create connection to sparkify database
conn = psycopg2.connect(database='sparkifydb', user='student', password='student', host='127.0.0.1', port='5432')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Connects external_stylesheets to the styling of our Dash app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# The colors we'll use for the layout of the page
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# Read in data from a select query of the sparkify database into a pandas dataframe
df = pd.read_sql_query(artist_location_select, con=conn)

# Loads the dataframe into a geo scatter plot
fig = px.scatter_geo(df, lat="artist_latitude",
                     lon="artist_longitude",
                     color="artist_location",  # which column to use to set the color of markers
                     hover_name="artist_name",  # column added to hover information
                     projection="natural earth")

# fig.update_layout(
#     plot_bgcolor=colors['background'],
#     paper_bgcolor=colors['background'],
#     font_color=colors['text']
# )

fig.show()

# Creates the layout for our data visualization using Dash html components
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Sparkify Song Play Analysis',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(
        children='A view of artist locations',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.Graph(
        id='artists-locations',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
