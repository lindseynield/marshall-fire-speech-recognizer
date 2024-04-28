from pathlib import Path

from sample_code.audio import convert_audio_to_text
from tests.constants import RESOURCES_PATH


def test_convert_audio_to_text():
    """Tests the method of converting an audio file to text using
    the google speech recognition API."""
    transcription = convert_audio_to_text(
        wav_file=Path(RESOURCES_PATH, "audio.wav"), api="google", write_result=False
    )
    transcription_string = ""
    for value in transcription.values():
        transcription_string = transcription_string + value
    assert (
        "1017 Turnberry Circle" in transcription_string
    ), "Audio not correctly converted!"
