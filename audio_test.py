from pathlib import Path
import wave

from audio.tts import TTSManager
from audio.subtitles import SubtitleGenerator


class AudioTest:

    def run(self):

        # =========================
        # TEST SCRIPT
        # =========================

        script = (
            "Hello everyone! "
            "I am Midoriya. "
            "Today, we will learn about arrays. "
            "An array stores multiple values in a single variable. "
            "Each value can be accessed using its index."
        )

        output_dir = Path("output/audio")
        output_dir.mkdir(parents=True, exist_ok=True)

        audio_path = output_dir / "speech.wav"
        subtitle_path = output_dir / "subtitles.srt"

        # =========================
        # GENERATE SPEECH
        # =========================

        tts = TTSManager(rate=165, volume=1.0)

        print("\nAvailable voices:")

        for voice in tts.get_voices():
            print(
                f"{voice['index']}: {voice['name']}"
            )

        print("\nGenerating speech...")

        tts.generate_speech(
            script,
            audio_path
        )

        print("Audio generated:", audio_path)

        # =========================
        # CHECK AUDIO DURATION
        # =========================

        with wave.open(str(audio_path), "rb") as audio_file:

            frames = audio_file.getnframes()
            sample_rate = audio_file.getframerate()

            duration = frames / sample_rate

        print(
            f"Audio duration: {duration:.2f} seconds"
        )

        # =========================
        # GENERATE SUBTITLES
        # =========================

        subtitle_generator = SubtitleGenerator(
            max_words=8
        )

        subtitle_generator.generate_srt(
            text=script,
            duration=duration,
            output_path=subtitle_path
        )

        print("Subtitles generated:", subtitle_path)

        # =========================
        # FINAL VERIFICATION
        # =========================

        print("\n--- Audio Test Results ---")

        print("Audio exists:", audio_path.exists())
        print("Audio size:", audio_path.stat().st_size, "bytes")

        print(
            "Subtitles exist:",
            subtitle_path.exists()
        )

        print("Audio and subtitle generation completed!")


if __name__ == "__main__":

    AudioTest().run()