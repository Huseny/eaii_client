import speech_recognition as sr


class Listener:
    def __init__(self) -> None:
        pass

    def __add_white_spaces(self, text: str) -> str:
        return " ".join(text)

    def recognize_from_mic(self) -> str:
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Say something in Amharic...")
            audio_data = recognizer.listen(source, timeout=10)

        try:
            text = recognizer.recognize_google(audio_data, language="am-ET")
            print("You said:", self.__add_white_spaces(text))
            return text
        except sr.UnknownValueError:
            print("could not understand the audio.")
        except sr.RequestError as e:
            print(f"Error with the request: {e}")
