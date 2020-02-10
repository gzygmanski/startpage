from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit, send
from flask_cors import CORS
from mpd import MPDClient
from time import sleep
import redis
import rq
from emit_current_song import emit_current_song, emit_with_rating, init_mpd_client
import json
from eventlet import monkey_patch as monkey_patch

monkey_patch()

app = Flask(__name__,
    static_folder = "./dist/static",
    template_folder = "./dist")


cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*", message_queue='redis://localhost:6379')

r = redis.Redis()
q = rq.Queue('test', connection=r)

@app.route('/api/v1/resources/bookmarks/')
def get_bookmarks():
    with open("bookmarks.json", "r") as read_file:
        data = json.load(read_file)
    return jsonify(data)

@app.route('/api/v1/resources/bookmarks/add/', methods = ['POST', 'DELETE'])
def bookmarks():
    if request.method == 'POST':
        req = request.get_json()
        
        with open('bookmarks.json', "r") as f:
            bookmarks = json.load(f)

        bookmarks.append(req)
        
        with open('bookmarks.json', "w") as f:
            json.dump(bookmarks, f)

        return jsonify(bookmarks)

@app.route('/api/v1/resources/playlists')
def api_playlists():
    client = init_mpd_client()
    playlistList = client.listplaylists() 
    client.close()
    client.disconnect()

    return jsonify(playlistList)

@app.route('/api/v1/resources/playlists/currentplaylist')
def api_playlists_currentlist():
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

@socketio.on('mpd_next', namespace='/api')
def on_mpd_next():
    client = init_mpd_client()
    client.next()
    client.close()
    client.disconnect()

@socketio.on('mpd_previous', namespace='/api')
def on_mpd_previous():
    client = init_mpd_client()
    client.previous()
    client.close()
    client.disconnect()

@socketio.on('play_pos', namespace='/api')
def on_playpos(data):
    client = init_mpd_client()
    client.play(data) 
    client.close()
    client.disconnect()

@socketio.on('remove_pos', namespace='/api')
def on_playpos(data):
    client = init_mpd_client()
    client.delete(data) 
    client.close()
    client.disconnect()

@socketio.on('load_playlist', namespace='/api')
def on_playpos(data):
    client = init_mpd_client()
    client.clear()
    client.load(data) 
    client.play(0)
    client.close()
    client.disconnect()



@app.route('/', defaults={'path': ''})

@app.route('/<path:path>')
def catch_all(path):
    client = init_mpd_client()
    currentsong = client.currentsong()
    
    emit_with_rating(client, currentsong)
    q.enqueue(emit_current_song, result_ttl=-1)
    return render_template("index.html")

if __name__ == '__main__':
    socketio.run(app, debug=True)
