from flask import Flask
import requests

app = Flask(__name__)

REPLIT_URL = "https://5b23b15c-265d-4760-bf8b-01f9335f88ce-00-2m3gi84pg9q5z.sisko.repl.co/"

@app.route('/')
def home():
    try:
        requests.get(REPLIT_URL)
        return "Pinged your Replit bot!"
    except:
        return "Failed to ping Replit bot."

if __name__ == "__main__":
    app.run()
