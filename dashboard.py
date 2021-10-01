#Pandas, Plotly, and NumPy modules
import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

# Modules imported to retrieve data from Google Sheets
import gspread
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials

SPREADSHEET_ID = '1-kUlYLeDEQyzw2PYnLn6quq7kFYJbduI_Zrk_bQ7_9A'
RANGE_NAME = 'PlayerOllie'

playerID = {
    1:'Lea Venezuela Ruz',
    2:'Bryan Rios',
    3:'Aidan McGarrity',
    4:'Sebastian Decady',
    5:'Dylan Savage',
    6:'Austin Holloway',
    7:'Collin Patterson',
    8:'Declan Anderson',
    9:'Owen Sheffield',
    10:'Brady Roberton',
    11:'James Knowlton',
    12:'Adam Saidi',
    13:'Michael Britton'
}

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Urbana Boys Soccer Statistics Dashboard', style={'marginBottom':10, 'color':'#FFAABB'}),

    html.H3(children=playerID.get(11)),

    html.Img(src='assets/tanjiro.jpg', style={'width':200})
], style={'fontFamily':"'Lato',sans-serif", 'marginLeft':20, 'marginRight':20})

if __name__ == '__main__':
    app.run_server(debug=True)