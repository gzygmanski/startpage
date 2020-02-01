from mpd import MPDClient
from time import sleep
from flask_socketio import SocketIO, emit
socket = SocketIO(message_queue = 'redis://')

def init_mpd_client(host='localhost', port=6600):
    client = MPDClient()
    client.timeout = 10
    client.idletimeout = None
    client.connect(host, port)
    return client

def emit_current_song():
    client = init_mpd_client()

    while True:
        client.idle("player", "sticker")
        currentsong = client.currentsong()

        try:
            ratingValue = client.sticker_get("song", currentsong["file"], "stars")
        except:
            ratingValue = 0
            print('Sticker not found')
        finally:
            currentsong["rate"] = ratingValue
            socket.emit('currentsong', currentsong, namespace='/api')
    # while True:
    #     client.idle("player")
    #     socket.emit('currentsong', client.currentsong(), namespace='/api')
    #     print('Emited song')
    client.close()
    client.disconnect()

