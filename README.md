# Dash Google Auth Email

Dash Google Auth Email is a simple library using Google OAuth to authenticate and
view a [Dash](https://dash.plot.ly/) app.  This project is almost entirely sourced from the parernt project [dash-google-auth](https://github.com/lchapo/dash-google-auth)

This Library uses [Flask Dance](https://github.com/singingwolfboy/flask-dance)
and a modified version of Plotly's own [dash auth](https://github.com/plotly/dash-auth)
for authentication.

## Basic Use

Authentication can be added to your Dash application using the `GoogleOAuth`
class, i.e.

```python
from dash import Dash
from flask import Flask
from dash_google_auth_email import GoogleOAuth

server = Flask(__name__)
server.config.update({
  'GOOGLE_OAUTH_CLIENT_ID': ...,
  'GOOGLE_OAUTH_CLIENT_SECRET': ...,
})

app = Dash(__name__, server=server, url_base_pathname='/', auth='auth')

authorized_emails = [...]
additional_scopes = [...]
auth = GoogleOAuth(app, authorized_emails, additional_scopes)

# your Dash app here :)
...
```

## Example
Steps to try this out yourself:

1. Install the `dash-google-auth-email` library using `pip`:

    ```bash
    $ pip install dash-google-auth-email
    ```

2. Follow the [Flask Dance Guide](http://flask-dance.readthedocs.io/en/latest/quickstarts/google.html)
   to create an app on the google admin console

3. Make a copy of [app.py](https://github.com/ricklentz/dash-google-auth-email/blob/master/app.py)
   and set the variables (or set the corresponding environment variables):
    ```python
    server.config["GOOGLE_OAUTH_CLIENT_ID"] = ...
    server.config["GOOGLE_OAUTH_CLIENT_SECRET"] = ...
    ```
   with values from the Google OAuth 2 client you should have set up in step 1.
   If you've set these up properly, you can find them at
   [APIs & Services > Credentials](https://console.developers.google.com/apis/credentials)
   under the section **OAuth 2.0 client IDs**.

4. Replace `authorized_emails` in `app.py` with whatever
   Google emails you want to grant access to your app. It is recommended that you getting these from a persistance layer.

5. Run `python app.py` and open [localhost](http://localhost:8050/) in a
   browser window to try it out! If the app loads automatically without
   prompting a Google login, that means you're already authenticated -- try
   using an incognito window in this case if you want to see the login
   experience for a new user.
