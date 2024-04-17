import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import requests


app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1("Cricket Status"),
    html.Div([
        html.Label("Enter Match ID:"),
        dcc.Input(id='match-id-input', type='text', value='4038', debounce=True),
    ]),
    html.Div(id='status-output')
])


@app.callback(
    Output('status-output', 'children'),
    [Input('match-id-input', 'value')]
)
def update_status(match_id):
    
    url = f"https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/{match_id}/scard"
    headers = {
        "X-RapidAPI-Key": "29c4f831cfmsh52dc9590010758dp119888jsn6df53e96b996",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    
    status = data.get('status', 'N/A')
    return html.P(f"Status: {status}")

if __name__ == '__main__':
    app.run_server(debug=True)
