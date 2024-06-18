import edge_tts
from audioplayer import AudioPlayer


class TTS:

    def __init__(self):
        self.voice = "am-ET-MekdesNeural"
        self.output_file = "saved.mp3"

    async def __amain(self, text: str) -> None:
        communicate = edge_tts.Communicate(text, self.voice, rate="-10%", pitch="-5Hz")
        await communicate.save(self.output_file)

    async def play(self, text: str):
        await self.__amain(text)
        AudioPlayer(self.output_file).play(block=True)
