import socketio
import asyncio
from listener import Listener
from reader import TTS

import face_recognition
import cv2
import asyncio
from reader import TTS

video_capture = cv2.VideoCapture(0)

# known_face_encodings = []
# known_face_names = []

face_locations = []
face_encodings = []
face_name = None
process_this_frame = True
tts = TTS()


while len(face_locations) == 0:
    ret, frame = video_capture.read()

    if process_this_frame:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        # face_encodings = face_recognition.face_encodings(
        #     rgb_small_frame, face_locations
        # )

        # for face_encoding in face_encodings:
        #     matches = face_recognition.compare_faces(
        #         known_face_encodings, face_encoding
        #     )
        #     face_name = "Unknown"

        #     # use the known face with the smallest distance to the new face
        #     face_distances = face_recognition.face_distance(
        #         known_face_encodings, face_encoding
        #     )
        #     best_match_index = np.argmin(face_distances)
        #     if matches[best_match_index]:
        #         name = known_face_names[best_match_index]

        #     face_names = name
        #     break

    process_this_frame = not process_this_frame
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
asyncio.run(tts.play("ሰላም ሁሴን, እንዴት ላግዞት እችላለው?"))


listener = Listener()
sio = socketio.Client()
sio.connection_url = "http://127.0.0.1:8000"


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
    asyncio.run(tts.play(data))
    result = listener.recognize_from_mic()
    sio.emit("message", result)


sio.connect("http://127.0.0.1:8000")

sio.wait()
