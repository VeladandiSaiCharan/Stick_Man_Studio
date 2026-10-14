from pathlib import Path
import wave

import numpy as np
import pyttsx3
import soundfile as sf
from kokoro_onnx import Kokoro


class TTSManager:
    """
    Text-to-speech manager for StickMan Studio.

    Kokoro is the primary engine.
    pyttsx3 is available as a fallback.
    """

    CHARACTER_VOICES = {
        "Midoriya": "am_michael",
        "Bakugo": "am_fenrir",
    }

    def __init__(
        self,
        backend="kokoro",
        rate=165,
        volume=1.0,
        voice_index=0,
        speed=0.95,
        fallback_to_pyttsx3=True,
        model_path="assets/kokoro/kokoro-v1.0.onnx",
        voices_path="assets/kokoro/voices-v1.0.bin",
    ):

        if backend not in ("kokoro", "pyttsx3"):
            raise ValueError(
                "Backend must be 'kokoro' or 'pyttsx3'."
            )

        if rate <= 0:
            raise ValueError(
                "Speech rate must be positive."
            )

        if not 0.0 <= volume <= 1.0:
            raise ValueError(
                "Volume must be between 0.0 and 1.0."
            )

        if speed <= 0:
            raise ValueError(
                "Kokoro speed must be positive."
            )

        self.backend = backend
        self.rate = rate
        self.volume = volume
        self.speed = speed
        self.fallback_to_pyttsx3 = fallback_to_pyttsx3

        self.model_path = Path(model_path)
        self.voices_path = Path(voices_path)

        self.kokoro = None
        self.engine = None
        self.voices = []

        # Initialize Kokoro only when it is needed.
        if self.backend == "kokoro":
            print("TTS engine: Kokoro")

        else:
            self._initialize_pyttsx3(voice_index)

    # --------------------------------------------------
    # KOKORO INITIALIZATION
    # --------------------------------------------------

    def _initialize_kokoro(self):

        if self.kokoro is not None:
            return

        if not self.model_path.exists():
            raise FileNotFoundError(
                f"Kokoro model not found: {self.model_path}"
            )

        if not self.voices_path.exists():
            raise FileNotFoundError(
                f"Kokoro voices file not found: {self.voices_path}"
            )

        self.kokoro = Kokoro(
            str(self.model_path),
            str(self.voices_path)
        )

        print("Kokoro model loaded successfully.")

    # --------------------------------------------------
    # PYTTSX3 INITIALIZATION
    # --------------------------------------------------

    def _initialize_pyttsx3(self, voice_index=0):

        if self.engine is not None:
            return

        self.engine = pyttsx3.init()

        self.engine.setProperty(
            "rate",
            self.rate
        )

        self.engine.setProperty(
            "volume",
            self.volume
        )

        self.voices = self.engine.getProperty("voices")

        if self.voices:

            if not 0 <= voice_index < len(self.voices):
                raise ValueError(
                    f"voice_index must be between 0 and "
                    f"{len(self.voices) - 1}."
                )

            self.engine.setProperty(
                "voice",
                self.voices[voice_index].id
            )

    # --------------------------------------------------
    # VOICE INFORMATION
    # --------------------------------------------------

    def get_voices(self):

        return [
            {
                "index": index,
                "id": voice.id,
                "name": voice.name,
            }
            for index, voice in enumerate(self.voices)
        ]

    def set_voice(self, voice_index):

        self._initialize_pyttsx3()

        if not 0 <= voice_index < len(self.voices):
            raise ValueError(
                "Invalid voice index."
            )

        self.engine.setProperty(
            "voice",
            self.voices[voice_index].id
        )

    def get_character_voice(self, character):

        if character not in self.CHARACTER_VOICES:
            raise ValueError(
                f"Unknown character: {character}. "
                f"Available characters: "
                f"{', '.join(self.CHARACTER_VOICES)}"
            )

        return self.CHARACTER_VOICES[character]

    # --------------------------------------------------
    # PYTTSX3 SETTINGS
    # --------------------------------------------------

    def set_rate(self, rate):

        if rate <= 0:
            raise ValueError(
                "Speech rate must be positive."
            )

        self.rate = rate

        if self.engine is not None:
            self.engine.setProperty("rate", rate)

    def set_volume(self, volume):

        if not 0.0 <= volume <= 1.0:
            raise ValueError(
                "Volume must be between 0.0 and 1.0."
            )

        self.volume = volume

        if self.engine is not None:
            self.engine.setProperty("volume", volume)

    # --------------------------------------------------
    # SPEECH GENERATION
    # --------------------------------------------------

    def generate_speech(
        self,
        text,
        output_path,
        character="Midoriya",
        voice=None,
    ):

        if not isinstance(text, str) or not text.strip():
            raise ValueError(
                "Speech text must be a non-empty string."
            )

        output_path = Path(output_path)

        if output_path.suffix.lower() != ".wav":
            raise ValueError(
                "This version supports WAV output only."
            )

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if self.backend == "kokoro":

            selected_voice = (
                voice
                if voice is not None
                else self.get_character_voice(character)
            )

            try:

                self._initialize_kokoro()

                print(
                    f"Generating Kokoro speech "
                    f"for {character} using {selected_voice}..."
                )

                audio, sample_rate = self.kokoro.create(
                    text,
                    voice=selected_voice,
                    speed=self.speed,
                    lang="en-us",
                )

                audio = np.asarray(audio)

                if audio.size == 0:
                    raise RuntimeError(
                        "Kokoro generated empty audio."
                    )

                sf.write(
                    str(output_path),
                    audio,
                    sample_rate,
                    subtype="PCM_16",
                )

            except Exception as error:

                # Remove a potentially incomplete output file.
                if output_path.exists():
                    output_path.unlink()

                if not self.fallback_to_pyttsx3:
                    raise RuntimeError(
                        f"Kokoro speech generation failed: {error}"
                    ) from error

                print(
                    f"WARNING: Kokoro failed: {error}"
                )

                print(
                    "Switching to pyttsx3 fallback."
                )

                self.backend = "pyttsx3"
                self._initialize_pyttsx3()

                self._generate_pyttsx3(
                    text,
                    output_path
                )

        else:

            self._initialize_pyttsx3()

            self._generate_pyttsx3(
                text,
                output_path
            )

        self._validate_audio(output_path)

        return output_path

    # --------------------------------------------------
    # PYTTSX3 SPEECH GENERATION
    # --------------------------------------------------

    def _generate_pyttsx3(
        self,
        text,
        output_path
    ):

        try:

            self.engine.save_to_file(
                text,
                str(output_path)
            )

            self.engine.runAndWait()

        except Exception as error:

            raise RuntimeError(
                f"pyttsx3 speech generation failed: {error}"
            ) from error

    # --------------------------------------------------
    # AUDIO VALIDATION
    # --------------------------------------------------

    def _validate_audio(self, output_path):

        if not output_path.exists():
            raise RuntimeError(
                "The speech engine did not create the file."
            )

        if output_path.stat().st_size == 0:
            raise RuntimeError(
                "The generated audio file is empty."
            )

        try:

            with wave.open(str(output_path), "rb") as audio:

                if audio.getnframes() == 0:
                    raise RuntimeError(
                        "The audio contains no frames."
                    )

                if audio.getframerate() <= 0:
                    raise RuntimeError(
                        "Invalid audio sample rate."
                    )

        except (wave.Error, EOFError) as error:

            raise RuntimeError(
                "The generated file is not a readable WAV file."
            ) from error

    # --------------------------------------------------
    # CLEANUP
    # --------------------------------------------------

    def close(self):

        if self.engine is not None:

            self.engine.stop()
            self.engine = None

        if self.kokoro is not None:

            voices = getattr(self.kokoro, "voices", None)

            if voices is not None and hasattr(voices, "close"):
                voices.close()

            self.kokoro = None