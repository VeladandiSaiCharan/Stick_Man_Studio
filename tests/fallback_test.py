from pathlib import Path
import sys
import wave

# Add the project root to Python's module search path.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from audio.tts import TTSManager


def main():
    output_path = Path("output/audio/fallback_test.wav")

    tts = TTSManager(
        backend="pyttsx3",
        rate=165,
        volume=1.0,
        voice_index=0,
    )

    try:
        print("Testing pyttsx3 fallback...")

        tts.generate_speech(
            text=(
                "Hello! This is a test of the "
                "StickMan Studio fallback voice."
            ),
            output_path=output_path,
        )

        with wave.open(str(output_path), "rb") as audio:
            duration = audio.getnframes() / audio.getframerate()

        if duration <= 0:
            raise RuntimeError("Audio duration must be positive.")

        print("Fallback test: PASSED")
        print("Output:", output_path.resolve())
        print(f"Duration: {duration:.2f} seconds")
        print("File size:", output_path.stat().st_size, "bytes")

    finally:
        tts.close()


if __name__ == "__main__":
    main()