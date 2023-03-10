import dash   
import numpy as np
import plotly.express as px
import dash_core_components as dcc  
import dash_html_components as html
from dash.dependencies import Input, Output

df = px.data.gapminder()

app = dash.Dash()

app.layout = html.Div(id = 'parent', children = [
    
    # creating a slider within a html component 
   html.Div(id = 'slider-div', children = 
            [ dcc.Slider(id = 'year-slider',
               min = df['year'].min(),
               max = df['year'].max(),
               value = df['year'].min(),
               marks = { str(year) : str(year) for year in df['year'].unique() },
               step = None
               )], style = {'width':'50%', 'display':'inline-block'}), 
           # inline-block : to show slider and dropdown in the same line
           # 
    
    # creating a dropdown within a html component 
    html.Div( id = 'dropdown-div', children = 
             [dcc.Dropdown(id = 'continent-dropdown',
                 options = [{'label':i, 'value':i} for i in np.append(['All'],df['continent'].unique()) ],
                 value = 'All'
                 )], style = {'width':'50%', 'display':'inline-block'} ),
            # inline-block : to show slider and dropdown in the same line
            
    # setting the graph component 
    dcc.Graph(id = 'scatter-plot') 
    ])

@app.callback(Output(component_id='scatter-plot', component_property= 'figure'),
              [Input(component_id='year-slider', component_property= 'value'),
               Input(component_id='continent-dropdown', component_property= 'value')])
def graph_update(slider_value, continent_value):
    # filtering based on the slide and dropdown selection
    if continent_value == 'All':
        filtered_df = df.loc[df['year']==slider_value]
    else:
        filtered_df = df.loc[(df['year']==slider_value) & (df['continent'] == continent_value)]
    
    # the figure/plot created using the data filtered above 
    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp", 
        size="pop", color="continent", hover_name="country",
        log_x=True, 
        size_max=55, 
        range_x=[100,100000], range_y=[25,90]
        )

      
    return fig

if __name__== '__main__':
    app.run_server()