import gradio as gr
from urllib.parse import unquote
from datetime import datetime
import csv
import os

LOG_FILE = "click_log.csv"
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "target_url"])

def redirect(url):
    decoded_url = unquote(url)
    
    # log click
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.utcnow().isoformat(), decoded_url])
    
    return f'<meta http-equiv="refresh" content="1; url={decoded_url}"><p>Redirecting…</p>'

iface = gr.Interface(
    fn=redirect,
    inputs=gr.Textbox(label="URL", visible=False),
    outputs=gr.HTML()
)

# Simply launch — no allow_flagging argument
iface.launch(server_name="0.0.0.0", server_port=7860)
