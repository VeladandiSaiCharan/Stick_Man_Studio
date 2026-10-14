from pathlib import Path
import re


class SubtitleGenerator:

    def __init__(self, max_words=8):

        if not isinstance(max_words, int) or max_words < 1:
            raise ValueError(
                "max_words must be a positive integer."
            )

        self.max_words = max_words

    def _format_timestamp(self, seconds):

        milliseconds = round(seconds * 1000)

        hours = milliseconds // 3_600_000
        milliseconds %= 3_600_000

        minutes = milliseconds // 60_000
        milliseconds %= 60_000

        secs = milliseconds // 1000
        milliseconds %= 1000

        return (
            f"{hours:02}:"
            f"{minutes:02}:"
            f"{secs:02},"
            f"{milliseconds:03}"
        )

    def _split_text(self, text):

        words = re.findall(r"\S+", text.strip())

        if not words:
            raise ValueError(
                "Subtitle text cannot be empty."
            )

        return [
            " ".join(words[index:index + self.max_words])
            for index in range(0, len(words), self.max_words)
        ]

    def generate_srt(
        self,
        text,
        duration,
        output_path
    ):

        if not isinstance(duration, (int, float)):
            raise TypeError(
                "Duration must be a number."
            )

        if duration <= 0:
            raise ValueError(
                "Duration must be positive."
            )

        chunks = self._split_text(text)

        total_words = sum(
            len(chunk.split())
            for chunk in chunks
        )

        output_path = Path(output_path)

        if output_path.suffix.lower() != ".srt":
            raise ValueError(
                "Subtitle output must use the .srt extension."
            )

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        entries = []
        current_time = 0.0

        for index, chunk in enumerate(chunks, start=1):

            word_count = len(chunk.split())

            segment_duration = (
                duration * word_count / total_words
            )

            start_time = current_time

            if index == len(chunks):
                end_time = float(duration)
            else:
                end_time = (
                    current_time + segment_duration
                )

            entries.append(
                f"{index}\n"
                f"{self._format_timestamp(start_time)} --> "
                f"{self._format_timestamp(end_time)}\n"
                f"{chunk}\n"
            )

            current_time = end_time

        output_path.write_text(
            "\n".join(entries),
            encoding="utf-8"
        )

        return output_path