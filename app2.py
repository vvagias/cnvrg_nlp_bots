import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import http.client
import json

#dash app
app = dash.Dash(__name__)

app.layout = html.Div([
html.H1(children="Bert QA App"),
html.H2(children="huggingface / pytorch / dash "),
html.Tr([
html.Br(),
"Ask bot a question",

html.Div(id='my-confirmation'),
html.Div([dcc.Input(id='my-input', value='what is cnvrg?', type='text'),
html.Button(id='submit-button-state', n_clicks=0, children='Submit')]),
html.Br(),
html.H2(id='my-answer'),
html.H6('https://cnvrg.io/developers'),
])
])


@app.callback(
    Output(component_id='my-answer', component_property='children'),
    Input(component_id='submit-button-state', component_property='n_clicks'),
    State(component_id='my-input', component_property='value')

)
def update_output_div(n_clicks, input_value):
    # loop on user's or prepared questions
    #generate response

    conn = http.client.HTTPSConnection("bert-qa-bot-1.prod.cnvrg.io")

    payload = "{\"input_params\": \"" + input_value + "\"}"

    headers = {
    'Cnvrg-Api-Key': "w6zTVi8A9mGwA31nqkMPra9s",
    'Content-Type': "application/json"
    }

    conn.request("POST", "/api/v1/endpoints/xld8pojmcgej8tesugw8", payload, headers)

    res = conn.getresponse()
    
    data = res.read()
    data = json.loads(data)
    
    return data['prediction']


server = app.server