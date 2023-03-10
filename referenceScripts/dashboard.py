import calendar
from datetime import date

import referenceScripts.dropdown as dropdown

import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import dcc, html
from dash.dependencies import Input, Output
from dash_extensions import Lottie
from wordcloud import WordCloud

df_cnt = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Analytic_Web_Apps/Linkedin_Analysis/Connections.csv")
df_cnt["Connected On"] = pd.to_datetime(df_cnt["Connected On"])
df_cnt["month"] = df_cnt["Connected On"].dt.month
df_cnt['month'] = df_cnt['month'].apply(lambda x: calendar.month_abbr[x])

df_invite = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Analytic_Web_Apps/Linkedin_Analysis/Invitations.csv")
df_invite["Sent At"] = pd.to_datetime(df_invite["Sent At"])

df_react = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Analytic_Web_Apps/Linkedin_Analysis/Reactions.csv")
df_react["Date"] = pd.to_datetime(df_react["Date"])

df_msg = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Analytic_Web_Apps/Linkedin_Analysis/messages.csv")
df_msg["DATE"] = pd.to_datetime(df_msg["DATE"])

url_connections = "https://assets10.lottiefiles.com/packages/lf20_mhdn5srg.json"
url_companies = "https://assets6.lottiefiles.com/packages/lf20_cmaqoazd.json"
url_msg_in = "https://assets3.lottiefiles.com/packages/lf20_4alionps.json"
url_msg_out = "https://assets4.lottiefiles.com/packages/lf20_u25cckyh.json"
url_reactions = "https://assets8.lottiefiles.com/packages/lf20_nxwrzdo2.json"

options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.layout = dbc.Container([

            dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardImg(src="assets\download.png"),
                    
                ],style={
                    'margin-bottom':'3px'
                }),
                dbc.Card([
                    dbc.CardBody(
                        children=[html.H3(children='This will act as next button',className="text-center"),
                                  dbc.Row([dbc.Col(dbc.Button("Next", href="dropdown",color="primary"),
                                                        className="mt-3"),
                                                ], justify="center")
                                        ],
                    )
                ],style={
                    'textAlign':'center'
                })
            ],
            style={
            'margin' : '10px',
            }),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.DatePickerSingle(
                            id="mydatepickerstart",
                            date = date(2018,1,1)
                        ),
                        dcc.DatePickerSingle(
                            id="mydatepickerend",
                            date=date(2021,4,4)
                        )
                    ])
                ],color="info")
            ],
            style={
            'textAlign':'center',
            'margin-top' : '10px',
            })   
        ]),
        dbc.Row([
            dbc.Col([ 
                dbc.Card([
                    dbc.CardHeader(Lottie(options=options,width="67%",height="67%",url=url_connections)),
                    dbc.CardBody([
                        html.H6("Connections"),
                        html.H2(id="connections",children="000")
                    ])
                ])
            ],style={
            'margin' : '10px',
            'textAlign':'center'
            }),
            dbc.Col([ 
                dbc.Card([
                    dbc.CardHeader(Lottie(options=options,width="67%",height="67%",url=url_companies)),
                    dbc.CardBody([
                        html.H6("Companies"),
                        html.H2(id="companies",children="000")
                    ])
                ])
            ],style={
            'margin-top' : '10px',
            'textAlign':'center'
            }),
            dbc.Col([ 
                dbc.Card([
                    dbc.CardHeader(Lottie(options=options,width="67%",height="67%",url=url_msg_in)),
                    dbc.CardBody([
                        html.H6("Invitation Received"),
                        html.H2(id="received",children="000")
                    ])
                ])
            ],style={
            'margin-top' : '10px',
            'textAlign':'center'
            }),
            dbc.Col([ 
                dbc.Card([
                    dbc.CardHeader(Lottie(options=options,width="67%",height="67%",url=url_msg_out)),
                    dbc.CardBody([
                        html.H6("Invitation Sent"),
                        html.H2(id="sent",children="000")
                    ])
                ])
            ],style={
            'margin-top' : '10px',
            'textAlign':'center'
            }),
            dbc.Col([ 
                dbc.Card([
                    dbc.CardHeader(Lottie(options=options,width="67%",height="67%",url=url_reactions)),
                    dbc.CardBody([
                        html.H6("Total Reactions"),
                        html.H2(id="reactions",children="000")
                    ])
                ])
            ],style={
            'margin-top' : '10px',
            'textAlign':'center'
            })
        ]),
        dbc.Row([
            dbc.Col([ 
                dbc.Card([
                    html.P("Total Connections"),
                    dbc.CardBody([
                    dcc.Graph(id='line-chart', figure={}),
                   ])
                ])
            ],width=6,
            style={
            'margin' : '10px',
            }),
            dbc.Col([ 
                dbc.Card([
                    html.H6("Connections by Company"),
                    dbc.CardBody([
                    dcc.Graph(id='bar-chart', figure={}),
                  ])
                ])
            ],style={
            'margin-top' : '10px'
            })
        ]),
        dbc.Row([ 
            dbc.Col([ 
                dbc.Card([
                    dbc.CardBody(html.P("Total Reactions By Type")),
                    dcc.Graph(id='TBD',figure={})
                ])
            ],style={
            'margin' : '10px',
            'textAlign':'center'
            }),
            dbc.Col([ 
                dbc.Card([
                    dbc.CardBody(html.P("Messages Received vs Sent")),
                    dcc.Graph(id='pie-chart', figure={}),
                ])
            ],style={
            'margin-top' : '10px',
            'textAlign':'center'
            }),
            dbc.Col([ 
                dbc.Card([
                    dbc.CardBody(html.P("Connections Position-Wise")),
                    dcc.Graph(id='wordcloud', figure={}),
                ])
            ],style={
            'margin-top' : '10px',
            'textAlign':'center'
            })
        ])
],fluid=True)

@app.callback(
    Output('connections','children'),
    Output('companies','children'),
    Output('received','children'),
    Output('sent','children'),
    Output('reactions','children'),
    Input('mydatepickerstart','date'),
    Input('mydatepickerend','date')
)



def update_small_cards(start_date, end_date):
    # Connections
    dff_c = df_cnt.copy()

    dff_c = dff_c[(dff_c['Connected On']>=start_date) & (dff_c['Connected On']<=end_date)]
    conctns_num = len(dff_c)
    compns_num = len(dff_c['Company'].unique())

    # Invitations
    dff_i = df_invite.copy()
    dff_i = dff_i[(dff_i['Sent At']>=start_date) & (dff_i['Sent At']<=end_date)]
    # print(dff_i)
    in_num = len(dff_i[dff_i['Direction']=='INCOMING'])
    out_num = len(dff_i[dff_i['Direction']=='OUTGOING'])

    # Reactions
    dff_r = df_react.copy()
    dff_r = dff_r[(dff_r['Date']>=start_date) & (dff_r['Date']<=end_date)]
    reactns_num = len(dff_r)

    return conctns_num, compns_num, in_num, out_num, reactns_num


# Line Chart ***********************************************************
@app.callback(
    Output('line-chart','figure'),
    Input('mydatepickerstart','date'),
    Input('mydatepickerend','date'),
)
def update_line(start_date, end_date):
    dff = df_cnt.copy()
    dff = dff[(dff['Connected On']>=start_date) & (dff['Connected On']<=end_date)]
    dff = dff[["month"]].value_counts()
    dff = dff.to_frame()
    dff.reset_index(inplace=True)
    dff.rename(columns={0: 'Total connections'}, inplace=True)

    fig_line = px.line(dff, x='month', y='Total connections', template='ggplot2',
                  title="Total Connections by Month Name")
    fig_line.update_traces(mode="lines+markers", fill='tozeroy',line={'color':'blue'})
    fig_line.update_layout(margin=dict(l=20, r=20, t=30, b=20))

    return fig_line


# Bar Chart ************************************************************
@app.callback(
    Output('bar-chart','figure'),
    Input('mydatepickerstart','date'),
    Input('mydatepickerend','date'),
)
def update_bar(start_date, end_date):
    dff = df_cnt.copy()
    dff = dff[(dff['Connected On']>=start_date) & (dff['Connected On']<=end_date)]

    dff = dff[["Company"]].value_counts().head(6)
    dff = dff.to_frame()
    dff.reset_index(inplace=True)
    dff.rename(columns={0:'Total connections'}, inplace=True)
    # print(dff_comp)
    fig_bar = px.bar(dff, x='Total connections', y='Company', template='ggplot2',
                      orientation='h', title="Total Connections by Company")
    fig_bar.update_yaxes(tickangle=45)
    fig_bar.update_layout(margin=dict(l=20, r=20, t=30, b=20))
    fig_bar.update_traces(marker_color='blue')

    return fig_bar


# Pie Chart ************************************************************
@app.callback(
    Output('pie-chart','figure'),
    Input('mydatepickerstart','date'),
    Input('mydatepickerend','date'),
)
def update_pie(start_date, end_date):
    dff = df_msg.copy()
    dff = dff[(dff['DATE']>=start_date) & (dff['DATE']<=end_date)]
    msg_sent = len(dff[dff['FROM']=='Adam Schroeder'])
    msg_rcvd = len(dff[dff['FROM'] != 'Adam Schroeder'])
    fig_pie = px.pie(names=['Sent','Received'], values=[msg_sent, msg_rcvd],
                     template='ggplot2', title="Messages Sent & Received"
                     )
    fig_pie.update_layout(margin=dict(l=20, r=20, t=30, b=20))
    fig_pie.update_traces(marker_colors=['red','blue'])

    return fig_pie


# Word Cloud ************************************************************
@app.callback(
    Output('wordcloud','figure'),
    Input('mydatepickerstart','date'),
    Input('mydatepickerend','date'),
)
def update_pie(start_date, end_date):
    dff = df_cnt.copy()
    dff = dff.Position[(dff['Connected On']>=start_date) & (dff['Connected On']<=end_date)].astype(str)

    my_wordcloud = WordCloud(
        background_color='white',
        height=275
    ).generate(' '.join(dff))

    fig_wordcloud = px.imshow(my_wordcloud, template='ggplot2',
                              title="Total Connections by Position")
    fig_wordcloud.update_layout(margin=dict(l=20, r=20, t=30, b=20))
    fig_wordcloud.update_xaxes(visible=False)
    fig_wordcloud.update_yaxes(visible=False)

    return fig_wordcloud

    

if __name__ == "__main__":
    app.run(debug=True)

