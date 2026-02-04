from flask import Flask, request, redirect, render_template_string
from datetime import datetime
import urllib.parse
import csv
import os

app = Flask(__name__)

LOG_FILE = "click_log.csv"

# Ensure log file exists
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "target_url", "referrer", "user_agent"])

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Redirecting...</title>
    <meta http-equiv="refresh" content="1;url={{ target }}">
</head>
<body>
    <p>Redirecting you to Google Maps…</p>
</body>
</html>
"""

@app.route("/track")
def track():
    target = request.args.get("url")

    if not target:
        return "Missing target URL", 400

    decoded_target = urllib.parse.unquote(target)

    # Log click
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.utcnow().isoformat(),
            decoded_target,
            request.referrer,
            request.headers.get("User-Agent")
        ])

    # Redirect
    return render_template_string(HTML_TEMPLATE, target=decoded_target)

@app.route("/")
def home():
    return "Dummy for.sg click tracker is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
