import logging
import os
from timeit import default_timer as timer

from sample_code.audio.sr import sr_audio_to_text

logger = logging.getLogger(__name__)

APIS = ["google"]


def convert_audio_to_text(wav_file: os.PathLike, api: str, write_result=True) -> str:
    """Converts *.wav audio file to text.

    Parameters
    ----------
    wav_file : os.PathLike
        Local path to the *.wav file to trascribe.
    api : str
        Recognition API to use.
    write_result : bool
        Whether to write transcription results to a file. Defaults to True.

    Returns
    -------
    str
        Transcription of the provided audio file.
    """
    if api not in APIS:
        raise ValueError(f"API {api} not yet supported!")

    logger.info(f"Converting speech to text for {wav_file}...")
    start = timer()
    audio_as_text = sr_audio_to_text(wav_file, write_result, api=api)
    end = timer()
    logger.info(f"Time: {end-start}")

    return audio_as_text
