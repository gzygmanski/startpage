from mpd import MPDClient
from time import sleep

def init_mpd_client(host='localhost', port=6600):
    client = MPDClient()
    client.timeout = 10
    client.idletimeout = None
    client.connect(host, port)
    return client

def emit_with_rating(client, currentsong, socket):
    try:
        ratingValue = client.sticker_get("song", currentsong["file"], "stars")
    except:
        print('Sticker not found')
        ratingValue = 0
    finally:
        currentsong["rate"] = ratingValue
        socket.emit('currentsong', currentsong, namespace='/api')

def emit_current_song(socket):
    client = init_mpd_client()

    while True:
        client.idle("player", "sticker")
        currentsong = client.currentsong()
        emit_with_rating(client, currentsong, socket)

    client.close()
    client.disconnect()

