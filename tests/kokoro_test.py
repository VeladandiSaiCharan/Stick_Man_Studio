from pathlib import Path

import soundfile as sf
from kokoro_onnx import Kokoro

#Configuration

MODEL_PATH = Path("assets/kokoro/kokoro-v1.0.onnx")
VOICES_PATH = Path("assets/kokoro/voices-v1.0.bin")

OUTPUT_PATH = Path("output/audio/speech_bakugo_test.wav")

VOICE = "am_fenrir"
SPEED = 0.95

#Test Script 

script = (
    "Hey everyone! "
    "Today, let's understand arrays. "
    "Imagine you want to store several values together. "
    "That's exactly where an array comes in! "
    "Each value has its own index, which helps us access it easily."
)

def main():

    #Check model files

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Kokoro model not found: {MODEL_PATH}"
        )

    if not VOICES_PATH.exists():
        raise FileNotFoundError(
            f"Kokoro voice file not found: {VOICES_PATH}"
        )

    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    print("Loading Kokoro model...")

    tts = Kokoro(
        str(MODEL_PATH),
        str(VOICES_PATH)
    )

    try:

        print("Generating natural-voice sample...")

        audio, sample_rate = tts.create(
            script,
            voice=VOICE,
            speed=SPEED,
            lang="en-us"
        )

        sf.write(
            str(OUTPUT_PATH),
            audio,
            sample_rate,
            subtype="PCM_16"
        )

        duration = len(audio) / sample_rate

        print("\n--- Kokoro Test Results ---")
        print("VOICE:", VOICE)
        print("Sample rate:", sample_rate)
        print(f"Duration: {duration:.2f} seconds")
        print("Output:", OUTPUT_PATH.resolve())
        print("File size:", OUTPUT_PATH.stat().st_size, "bytes")
        print("Kokoro speech generation successful!")

    finally:
        tts.voices.close()

if __name__ == "__main__":
    main()