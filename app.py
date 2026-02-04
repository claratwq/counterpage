from flask import Flask, request, render_template_string
import urllib.parse
from datetime import datetime
import csv
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Redirecting…</title>
    <meta http-equiv="refresh" content="1;url={{ target }}">
    <style>
        body {
            font-family: sans-serif;
            text-align: center;
            padding-top: 40px;
        }
    </style>
</head>
<body>
    <p>Place holder for forsg link, Redirecting you to Google Maps…</p>
</body>
</html>
"""

@app.route("/")
def track_redirect():
    target = request.args.get("url")
    if not target:
        return "Missing URL", 400

    decoded_target = urllib.parse.unquote(target)

    # log click here...

    return render_template_string(HTML_TEMPLATE, target=decoded_target)
