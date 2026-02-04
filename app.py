from flask import Flask, request, redirect
from datetime import datetime
import urllib.parse
import csv
import os

app = Flask(__name__)

LOG_FILE = "click_log.csv"

# Create log file with header if it doesn't exist
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "target_url", "referrer", "user_agent"])

@app.route("/")
def track_redirect():
    url = request.args.get("url")
    if not url:
        return "Missing URL parameter", 400

    decoded_url = urllib.parse.unquote(url)

    # Log click
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.utcnow().isoformat(),
            decoded_url,
            request.referrer,
            request.headers.get("User-Agent")
        ])

    # Redirect user
    return redirect(decoded_url)

if __name__ == "__main__":
    # Listen on all interfaces, port 5000 for Render/Heroku
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
