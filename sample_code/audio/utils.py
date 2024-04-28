import os

import pydub


def convert_mp3_to_wav(mp3_file: os.PathLike, dst: os.PathLike):
    """Converts a *.mp3 audio file to a *.wav file.

    Parameters
    ----------
    mp3_file : os.PathLike
        Local path to the mp3 file to convert.
    dst : os.PathLike
        Local destination path to save the *.wav file to.
    """
    mp3_audio = pydub.AudioSegment.from_mp3(mp3_file)
    mp3_audio.export(dst, format="wav")


def write_text(text: str, dst: os.PathLike):
    """Writes provided text string to a file.

    Parameters
    ----------
    text : str
        Text to write to file.
    dst : os.PathLike
        Local destination path to write to.
    """
    f = open(dst, "w+")
    f.write(text)
    f.close()
