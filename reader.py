import asyncio
import edge_tts
from audioplayer import AudioPlayer


class TTS:
    def __init__(self, text, voice, output_file):
        self.text = text
        self.voice = voice
        self.output_file = output_file

    async def amain(self) -> None:
        communicate = edge_tts.Communicate(
            self.text, self.voice, rate="-10%", pitch="-5Hz"
        )
        await communicate.save(self.output_file)

    async def run(self):
        # loop = asyncio.get_event_loop_policy().get_event_loop()
        # try:
        #     loop.run_until_complete(self.amain())
        # finally:
        #     loop.close()
        await self.amain()


if __name__ == "__main__":
    TEXT = """የዚህች ከተማ, ማህበረሰብ የከተማው አንበሳ, ይሉኛል።  """
    VOICE = "am-ET-MekdesNeural"
    OUTPUT_FILE = "saved.mp3"
    
    tts = TTS(TEXT, VOICE, OUTPUT_FILE)
    asyncio.run(tts.run())
    AudioPlayer(OUTPUT_FILE).play(block=True)
