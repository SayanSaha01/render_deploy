import dash
from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
#from dash_bootstrap_templates import ThemeChangerAIO, template_from_url
import pandas as pd
import plotly.express as px
import seaborn as sns
import squarify
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from urllib.request import urlopen
import json
import dash
from dash import Dash,dcc,html
import numpy as np

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

## GEN HOUSEHOLD INFO
df = pd.read_csv(r"datasets\UBAdata.csv")
trace2 = go.Histogram(
    x=df.age,
    opacity=0.75,
    marker=dict(color='rgba(12, 50, 196, 0.6)'))

data = [trace2]

layout = go.Layout(barmode='overlay',
                   xaxis=dict(title='Age ->'),
                   yaxis=dict( title='Count'),
)
fig = go.Figure(data=data, layout=layout)
##**********************************************************##

## GOVT SCHEMES

use_col = ['PM_jan_dhan_yojana', 'PM_ujjawala_yojana', 'PM_awas_yojana',
       'sukanya_samriddhi_yojana', 'mudra_yojana', 'PM_jivan_jyoti_yojana',
       'PM_suraksha_bima_yojana', 'atal_pension_yojana', 'fasal_bima_yojana',
       'kaushal_vikas_yojana', 'krishi_sinchai_yojana', 'jan_aushadhi_yojana',
       'SBM_toilet', 'soil_health_card', 'ladli_lakshmi_yojana',
       'janni_suraksha_yojana', 'kisan_credit_card']

schemes = pd.read_csv("datasets\schemes.csv", usecols = use_col)
schemes
index = schemes.sum().index.tolist()
val = schemes.sum().values.tolist()
schemes = schemes.apply(lambda x: x + 0.000001)
valc_type1 = schemes.sum()

index = valc_type1.index.tolist()
val = schemes.sum().values.tolist()

data = {'labels': index,
        'values': val}
df = pd.DataFrame(data)

go_scheme = px.treemap(df, path=['labels'],values='values', width=700, height=400)
go_scheme.update_layout(
    margin = dict(t=50, l=25, r=25, b=25))
##********************************************************/

##************************************************************
## LAND HOLDING
use_col = ['irrigated_area', 'barren_or_wasteland','cultivable_area', 'unirrigated_area', 'uncultivable_area']

land = pd.read_csv("datasets\land.csv", usecols = use_col)
index = land.sum().index.tolist()
val = land.sum().values.tolist()

landhold = px.pie(values = val, names=index,hole=0.5)

##************************************************************

##enerygy 
energy = pd.read_csv(r"datasets\energy.csv")
###########

## agri product
agri = pd.read_csv(r"datasets\agri_prod.csv")
agriproduct = px.scatter(agri, x="crop_area_prev_yr_acre", y="productivity_in_quintals_per_acre", color="crop_name",size="productivity_in_quintals_per_acre")

##***************************************************##

## Family Information
familydf = pd.read_csv(r"datasets\family.csv")

##**************************************##
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dcc.Markdown("""##  UBA STATISTICS VISUALISER"""),
                dbc.Col(
                    [
                        dcc.Markdown("""## GEN HOUSEHOLD INFO """),
                        dbc.Row(
                            [
                                dbc.Col(
                                    dcc.Dropdown(['Gender', 'Category', 'Poverty Status','House Type',
                                    'Sanitation','Drainage','Waste Collection'], 'Category', id='demo-dropdown'),
                                    #dcc.Markdown("""### Select the no of counties to visualize"""),
                                    width=8,
                                )
                            ]
                        ),
                        dcc.Graph(id="dd-output-container"),
                    ],
                    width=6,
                ),
                dbc.Col(
                    [
                        dcc.Markdown("""## GOVT SCHEME DISTRIBUTION"""),
                        dbc.Row(
                            [
                                dbc.Col(
                                )
                            ]
                        ),
                        dcc.Graph(id="govt_schemes",figure=go_scheme),
                    ],
                    width=6,
                ),
            ]
        ),
        html.Br(), # add a break between the graphs
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown("### LANDHOLDING DISTRIBUTION (in hectares)"),
                        dbc.Row(
                            [
                                dbc.Col(
                                    
                                ),
                            ]
                        ),
                        dcc.Graph(id="landholding",figure=landhold),
                    ],
                    width=6,
                ),
                dbc.Col(
                    [
                        dcc.Markdown("""## ENERGY AND POWER """),
                        dbc.Row(
                            [
                                dbc.Col(
                                    dcc.Dropdown(id='my_dropdown',options=[
                                    {'label': 'Connections', 'value': 'electricity_conn'},
                                    {'label': 'FElectricity Availability', 'value': 'elec_avail_perday_hour'},
                                    {'label': 'Lighting Means', 'value': 'lighting'},
                                    {'label': 'Cooking Medium', 'value': 'cooking'},
                                    {'label': 'Chullah', 'value': 'cook_chullah'}
                            ],                   #height/space between dropdown options
                            value='lighting',                   #dropdown value selected automatically when page loads
                            disabled=False,                     #disable dropdown value selection
                            multi=False,                        #allow multiple dropdown values to be selected
                            searchable=True,                    #allow user-searching of dropdown values
                            search_value='',                    #remembers the value searched in dropdown
                            placeholder='Please select...',     #gray, default text shown when no option is selected
                            clearable=True,                      #remembers dropdown value selected until...
                            ),width=8)
                            ]
                        ),
                        dcc.Graph(id="output_data"),
                    ]
                ),
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dcc.Markdown("""##  AGRI PRODUCTS """),
                dbc.Col(
                    [
                        dbc.Row(
                            []
                        ),
                        dcc.Graph(id="agriprod",figure=agriproduct),
                    ],
                    width=6,
                ),
                dbc.Col(
                    [
                        dcc.Markdown("""## FAMILY MEMBER INFO """),
                        dbc.Row(
                            [
                                dbc.Col(
                                    dcc.Dropdown(['sex', 'martial_status', 'education',
                                    'schooling_status', 'AADHAR_No', 'has_bank_acc', 'is_computer_literate',
                                    'has_SSP', 'health_prob', 'has_MNREGA', 'SHG', 'occupations'], 'sex', id='family-dropdown'),
                                    #dcc.Markdown("""### Select the no of counties to visualize"""),
                                    width=8,
                                )
                            ]
                        ),
                        dcc.Graph(id="family"),
                    ],
                    width=6,
                ),
            ]
        ),
        
    ],
    fluid=True,
    className="dbc",
)

## Energy and power
@app.callback(
    Output(component_id='output_data', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)

def build_graph(column_chosen):
    dff = energy
    fig = px.pie(dff,names=column_chosen,width=600, height=480)
    fig.update_traces(textinfo='percent+label')
    return fig

## family member information
@app.callback(
    Output(component_id='family', component_property='figure'),
    [Input(component_id='family-dropdown', component_property='value')]
)

def family_graph(chosen_column):
    fig = px.bar(familydf, x=chosen_column)
    return fig

if __name__ == "__main__":
    app.run(debug=True)