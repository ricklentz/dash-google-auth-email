#! /usr/bin/env python

# Example app

import os

import dash_core_components as dcc
import dash_html_components as html

from dash import Dash
from flask import Flask

from dash_google_auth import GoogleOAuth

# configure app
server = Flask(__name__)
app = Dash(
    __name__,
    server=server,
    url_base_pathname='/',
    auth='auth',
)

# configure google oauth using environment variables
server.secret_key = os.environ.get("FLASK_SECRET_KEY", "supersekrit")
server.config["GOOGLE_OAUTH_CLIENT_ID"] = os.environ["GOOGLE_OAUTH_CLIENT_ID"]
server.config["GOOGLE_OAUTH_CLIENT_SECRET"] = os.environ["GOOGLE_OAUTH_CLIENT_SECRET"]

# allow for insecure transport for local testing (remove in prod)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# designate list of authorized emails
authorized_emails = [
    "lucas.chapin@gmail.com",
    "1234@example.com",
]

auth = GoogleOAuth(
    app,
    authorized_emails,
)


@server.route("/")
def MyDashApp():
    return app.index()


app.layout = html.Div(children=[
    html.H1(children="Hello Dash"),

    html.Div(children='''
    Dash: A web application framework for Python
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 6], 'type': 'bar', 'name': 'Montreal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server()
