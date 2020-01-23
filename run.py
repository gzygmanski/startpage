from flask import Flask, render_template, jsonify
from flask_cors import CORS
from mpd import MPDClient

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/v1/resources/currentsong', methods=['GET'])
def api_current_song():
    client = MPDClient()

    client.timeout = 10
    client.idletimeout = None
    client.connect("localhost", 6600)

    current_song = client.currentsong()
    client.close()
    client.disconnect()

    return jsonify(current_song)

@app.route('/', defaults={'path': ''})

@app.route('/<path:path>')

def catch_all(path):
    return render_template("index.html")
