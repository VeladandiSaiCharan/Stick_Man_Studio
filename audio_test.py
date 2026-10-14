from pathlib import Path
import wave

from audio.tts import TTSManager
from audio.subtitles import SubtitleGenerator


def get_audio_duration(audio_path):

    with wave.open(str(audio_path), "rb") as audio:

        frames = audio.getnframes()
        sample_rate = audio.getframerate()

        if sample_rate <= 0:
            raise ValueError(
                "Invalid audio sample rate."
            )

        return frames / sample_rate


def main():

    output_dir = Path("output/audio")

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    generator = SubtitleGenerator(
        max_words=8
    )

    tts = TTSManager(
        backend="kokoro",
        speed=0.95,
        fallback_to_pyttsx3=True,
    )

    test_scripts = {
        "Midoriya": (
            "Hello everyone! "
            "I am Midoriya. "
            "Today, we will learn about arrays. "
            "An array stores multiple values in a single variable. "
            "Each value can be accessed using its index."
        ),

        "Bakugo": (
            "Wait a second! "
            "How do we access a particular value in an array? "
            "Is it possible to retrieve a value directly "
            "using its index?"
        ),
    }

    try:

        for character, script in test_scripts.items():

            print("\n" + "=" * 40)
            print(f"Testing character: {character}")
            print("=" * 40)

            audio_path = (
                output_dir / f"speech_{character.lower()}.wav"
            )

            subtitle_path = (
                output_dir / f"subtitles_{character.lower()}.srt"
            )

            # Generate speech.
            tts.generate_speech(
                text=script,
                output_path=audio_path,
                character=character,
            )

            # Calculate audio duration.
            duration = get_audio_duration(
                audio_path
            )

            # Generate subtitles.
            generator.generate_srt(
                text=script,
                duration=duration,
                output_path=subtitle_path,
            )

            # Validate outputs.
            if not audio_path.exists():
                raise FileNotFoundError(
                    f"Audio missing: {audio_path}"
                )

            if not subtitle_path.exists():
                raise FileNotFoundError(
                    f"Subtitles missing: {subtitle_path}"
                )

            if audio_path.stat().st_size == 0:
                raise RuntimeError(
                    f"Audio is empty: {audio_path}"
                )

            if subtitle_path.stat().st_size == 0:
                raise RuntimeError(
                    f"Subtitles are empty: {subtitle_path}"
                )

            print("\nResults:")
            print("Character:", character)
            print("Audio:", audio_path)
            print("Subtitles:", subtitle_path)
            print(f"Duration: {duration:.2f} seconds")
            print(
                "Audio size:",
                audio_path.stat().st_size,
                "bytes"
            )
            print("Audio validation: PASSED")
            print("Subtitle validation: PASSED")

        print("\n" + "=" * 40)
        print("DAY 29 TEST RESULTS")
        print("=" * 40)
        print("Midoriya voice: TESTED")
        print("Bakugo voice: TESTED")
        print("Audio generation: PASSED")
        print("Subtitle generation: PASSED")

    finally:

        tts.close()


if __name__ == "__main__":
    main()