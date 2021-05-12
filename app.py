import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from transformers import pipeline, Conversation
import numpy as np 


#cnvrg conversational pipeline "bot"    
cnvrg_bot = pipeline('conversational')

#dash app
app = dash.Dash(__name__)

app.layout = html.Div([
html.H1(children="cnvrg_bot Demo"),
html.H2(children="DialoGPT cnvrg Convo Bot "),
html.Tr([
html.Br(),
"Chat with the cnvrg_bot!",
html.H6('cnvrg.io/developers'),
html.Div(id='my-confirmation'),
html.Div(["Input: ",
html.Br(),
dcc.Input(id='my-input', value='', type='text'),
html.Button(id='submit-button-state', n_clicks=0, children='Submit')]),
html.Br(),
html.H6(id='my-answer'),
])
])


@app.callback(
    Output(component_id='my-answer', component_property='children'),
    Input(component_id='submit-button-state', component_property='n_clicks'),
    State(component_id='my-input', component_property='value')

)
def update_output_div(n_clicks, value):
        # loop on user's or prepared questions
        #generate response
        r = cnvrg_bot(Conversation(value))
        #respond!
        return r.generated_responses[0]


server = app.server