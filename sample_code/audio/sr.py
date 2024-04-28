import logging
import os
import time
from pathlib import Path
from typing import Dict, List, Union

import pydub
import speech_recognition as sr
from pydub.silence import split_on_silence

from sample_code.utils import write_json

logger = logging.getLogger(__name__)


def sr_audio_to_text(
    wav_file: os.PathLike, write_result: bool, api: str
) -> Union[List, Dict, str]:
    """Convert audio to test using Speech Recognition package.

    Parameters
    ----------
    wav_file : os.Pathlike
        Local path to the *.wav file to transcribe.
    write_result : bool
        Whether to write transcription results to a file.
    api : str
        The Speech Recognition-supported recognizer API to use.

    Returns
    -------
    Union[List, Dict, str]
        The transcribed audio file.
    """
    # Initialize the recognizer
    speech_rec = sr.Recognizer()

    recognizer_apis = {
        "google": speech_rec.recognize_google,
    }

    # Recognizers with special installations
    if api == "sphinx":
        recognizer_apis["sphinx"] = speech_rec.recognize_sphinx
    if api == "vosk":
        recognizer_apis["vosk"] = speech_rec.recognize_vosk

    # Split audio file into chunks if not already done so
    audio_id = Path(wav_file).stem
    chunk_dst = Path(Path(wav_file).parents[0], audio_id)
    if not chunk_dst.exists() or not any(Path(chunk_dst).iterdir()):
        logger.info("Chunkifying...")
        chunks = audio_chunkify(wav_file, chunk_dst)
    else:
        chunks = chunk_dst.glob("*.wav")

    # Process each chunk
    whole_text = {}
    text_dst = chunk_dst / f"{audio_id}_{api}_{time.strftime('%Y%m%d-%H%M%S')}.json"
    for audio_chunk in sorted(
        chunks, key=lambda path: int(path.stem.rsplit("_", 1)[1])
    ):
        # Speech to text
        with sr.AudioFile(str(audio_chunk)) as source:
            # Calibrate the energy threshold for ambient noise levels
            speech_rec.adjust_for_ambient_noise(source, duration=0.35)
            audio_data = speech_rec.record(source)
            # Try converting it to text
            try:
                audio_as_text = recognizer_apis[api](
                    audio_data, language="en-US", show_all=True
                )
            except TypeError:
                audio_as_text = recognizer_apis[api](audio_data, language="en")
            except sr.UnknownValueError as e:
                logger.warning("Error:", str(e))
            else:
                if audio_as_text:
                    if "confidence" in audio_as_text["alternative"]:
                        # return alternative with highest confidence score
                        best_hypothesis = max(
                            audio_as_text["alternative"],
                            key=lambda alternative: alternative["confidence"],
                        )["transcript"]
                    else:
                        # when there is no confidence available, we arbitrarily choose the first hypothesis.
                        best_hypothesis = audio_as_text["alternative"][0]["transcript"]

                whole_text[audio_chunk.stem] = best_hypothesis if audio_as_text else ""

                if write_result:
                    # Write text to file
                    write_json(whole_text, text_dst)

    return whole_text


def audio_chunkify(wav_path: os.PathLike, dst_dir: os.PathLike) -> List:
    """Splits large audio files into chunks and takes out the silent bits.

    Parameters
    ----------
    wav_path : os.PathLike
        Local path to the *.wav file to chunkify.
    dst_dir : os.PathLike
        Destination directory to save chunks to.

    Returns
    -------
    List
        List of paths to the audio chunks.
    """
    # Open the audio file using pydub
    sound = pydub.AudioSegment.from_wav(wav_path)

    # Split audio sound on silence and get chunks
    # TODO: Experiment with the input params
    audio_chunks = split_on_silence(
        sound,
        min_silence_len=1500,
        silence_thresh=sound.dBFS - 14,
        keep_silence=500,
    )

    # Save the chunks
    if not Path.exists(dst_dir):
        Path.mkdir(dst_dir)

    chunk_files = []
    for i, audio_chunk in enumerate(audio_chunks, start=1):
        chunk_file = Path(dst_dir, f"chunk_{i}.wav")
        audio_chunk.export(str(chunk_file), format="wav")
        chunk_files.append(chunk_file)

    return chunk_files
