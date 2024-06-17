import socketio
from listener import Listener

sio = socketio.Client()
sio.connection_url = "http://127.0.0.1:8000"
listener = Listener()


@sio.event
def connect():
    print("Connected to the server")

    result = listener.recognize_from_mic()
    sio.emit("message", result)


@sio.event
def disconnect():
    print("Disconnected from the server")


@sio.on("response")
def onResponse(data):
    print("response:", data)


sio.connect("http://127.0.0.1:8000")

sio.wait()
