from flask import Flask
import threading
import time
from flask import Flask, send_from_directory
import os


app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/favicon.ico')
def favicon():
   return send_from_directory(os.getcwd(), 'favicon.ico', mimetype='image/x-icon') 


def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)


def start_flask_thread():
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True 
    flask_thread.start()
