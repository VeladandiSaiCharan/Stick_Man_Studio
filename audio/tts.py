from pathlib import Path
import pyttsx3


class TTSManager:

    def __init__(self, rate=165, volume=1.0, voice_index=0):

        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", rate)
        self.engine.setProperty("volume", volume)

        voices = self.engine.getProperty("voices")

        if voices:
            if not 0 <= voice_index < len(voices):
                raise ValueError(
                    f"voice_index must be between 0 and {len(voices) - 1}."
                )

            self.engine.setProperty(
                "voice",
                voices[voice_index].id
            )

    def get_voices(self):

        voices = self.engine.getProperty("voices")

        return [
            {
                "index": index,
                "id": voice.id,
                "name": voice.name,
            }
            for index, voice in enumerate(voices)
        ]

    def set_rate(self, rate):

        if rate <= 0:
            raise ValueError("Speech rate must be positive.")

        self.engine.setProperty("rate", rate)

    def set_volume(self, volume):

        if not 0.0 <= volume <= 1.0:
            raise ValueError("Volume must be between 0.0 and 1.0.")

        self.engine.setProperty("volume", volume)

    def generate_speech(self, text, output_path):

        if not text or not text.strip():
            raise ValueError("Speech text cannot be empty.")

        output_path = Path(output_path)
        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.engine.save_to_file(
            text,
            str(output_path)
        )

        self.engine.runAndWait()

        if not output_path.exists():
            raise RuntimeError(
                "TTS engine did not create the output file."
            )

        if output_path.stat().st_size == 0:
            raise RuntimeError(
                "Generated audio file is empty."
            )

        return output_path