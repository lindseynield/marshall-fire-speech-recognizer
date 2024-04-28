import json
import os
from typing import Any, Dict, List, Union


def write_json(content: Union[List, Dict], dst):
    """Writes provided content to a JSON file.

    Parameters
    ----------
    content : Any
        Content to write to JSON file.
    dst : os.PathLike
        Local destination path to write to.
    """
    with open(dst, "w+") as f:
        f.write(json.dumps(content, indent=2))


def read_json(path: Union[str, os.PathLike]) -> Any:
    """Reads a JSON file from a local path.

    Parameters
    ----------
    path : Union[str, os.PathLike]
        Local path to the file to read.

    Returns
    -------
    Any
        JSON content from the file as a Python object.
    """
    with open(path, "r") as f:
        json_content = json.load(f)

    return json_content
