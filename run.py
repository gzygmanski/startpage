from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit, send
from flask_cors import CORS
from mpd import MPDClient
from time import sleep
import redis
import rq
from emit_current_song import emit_current_song

from eventlet import monkey_patch as monkey_patch
monkey_patch()

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")


cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*", message_queue='redis://localhost:6379')

r = redis.Redis()
q = rq.Queue('test', connection=r)

def init_mpd_client(host='localhost', port=6600):
    client = MPDClient()
    client.timeout = 10
    client.idletimeout = None
    client.connect(host, port)
    return client

@app.route('/api/v1/resources/playlist', methods=['GET'])
def api_playlist():
    client = init_mpd_client()
    playlist = client.playlistinfo()
    client.close()
    client.disconnect()

    return jsonify(playlist)

@socketio.on('connect', namespace='/api')
def on_connect():
    print('Client connected')

@socketio.on('disconnect', namespace='/api')
def on_disconnect():
    print('Client disconnected')

@app.route('/', defaults={'path': ''})

@app.route('/<path:path>')
def catch_all(path):
    q.enqueue(emit_current_song, result_ttl=-1)
    return render_template("index.html")

if __name__ == '__main__':
    socketio.run(app, debug=True)
