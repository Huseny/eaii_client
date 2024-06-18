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
            audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=5)

        try:
            text = recognizer.recognize_google(audio_data, language="am")
            print("You said:", self.__add_white_spaces(text))
            return text
        except Exception as e:
            print("Error:", e)
            return ""
