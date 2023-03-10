import requests
import pprint
import json
import pandas as pd

BASE_URL = "https://ubaformapi-qyaec74aq-fastapis-build.vercel.app"


def get_access_token(data):
    url = BASE_URL + '/login'
    headers = {
        "accept": "application/json",
    }
    response = requests.post(url, params=data, headers=headers)
    access_token = response.json()['access_token']
    return access_token


def test_get_fromdb_owner(village_name):
    url = BASE_URL + "/api/get_data"
    signincred = {
        "AADHAR_NO": "EDA",
        "password": "string",
        "village_name": "None",
        "role": "GOVTOff"
    }
    params = {"village_name": f"{village_name}"}
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {get_access_token(signincred)}",
        "Content-Type": "application/json",
    }
    response = requests.get(url=url, params=params, headers=headers)
    return response.json()


data = test_get_fromdb_owner("Sehore") # ["Aastha", "Sehore", "string"]
data_json = json.dumps(data['data'])
df = pd.DataFrame(data["data"]["fam_info"])
#pprint.pprint(data)


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
import plotly.graph_objects as go
import plotly.graph_objects as go

import pandas as pd

# load dataset
#df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/volcano.csv")

# create figure
fig = go.Figure()

# Add surface trace
fig.add_trace(go.Surface(z=df.values.tolist(), colorscale="Viridis"))

# Update plot sizing
fig.update_layout(
    width=800,
    height=900,
    autosize=False,
    margin=dict(t=0, b=0, l=0, r=0),
    template="plotly_white",
)

# Update 3D scene options
fig.update_scenes(
    aspectratio=dict(x=1, y=1, z=0.7),
    aspectmode="manual"
)

from dash import dcc


# Add dropdown
fig.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    args=["type", "surface"],
                    label="3D Surface",
                    method="restyle"
                ),
                dict(
                    args=["type", "heatmap"],
                    label="Heatmap",
                    method="restyle"
                )
            ]),
            direction="down",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.1,
            xanchor="left",
            y=1.1,
            yanchor="top"
        ),
    ]
)

# Add annotation
fig.update_layout(
    annotations=[
        dict(text="Trace type:", showarrow=False,
        x=0, y=1.085, yref="paper", align="left")
    ]
)

fig.show()