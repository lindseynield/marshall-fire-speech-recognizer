# Mapping the Marshall Fire via Scanner Audio :fire:

## About

While the [Marshall Fire](https://en.wikipedia.org/wiki/Marshall_Fire) was raging in Boulder County in 2021, I was evacuated from my home and glued to all sources of media to try to put together where the fire was and how far it had spread. One of the most useful sources of information was public saftey audio feeds that police and fire departments used to communicate with each other in real time. If the addresses and places communicated over these channels were mapped out in real time, we would probably have a good idea of where the fire had spread within minutes of this information being communicated.

This project builds a speech recognizer using the [SpeechRecognition](https://github.com/Uberi/speech_recognition) library. Feeding in publicaly available police scanner audio from the day of the Marshall Fire, this recognizer has been able to pinpoint several home addresses mentioned by emergency crews that night. This repo contains a snippet of one of these audio files that correctly identifies a home address that was destroyed in the fire. This address is then used as a jumping off point to analyze changes in the landscape from before and after the fire using Sentinel-2 imagery.

This repo contains [source code](./sample_code/audio/) for the speech recognizer and a [notebook](./marshall_fire.ipynb) demoing the speech recognition tool + Sentinel-2 visual imagery comparisons. Note that the interactive follium maps [will not render](https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files#working-with-jupyter-notebook-files-on-github) in GitHub. See this [nbviewer](https://nbviewer.org/gist/lindseynield/82da24644c2a04b2ee137fc4b87d8004) to view rendered maps.

## Installation

Clone the repo:

```bash
git clone git@github.com:lindseynield/marshall-fire-speech-recognizer.git && cd marshall-fire-speech-recognizer
```

(Optional) Create and activate a local `pyenv virtualenv`:

```bash
pyenv virtualenv 3.8.12 my-venv
pyenv activate my-venv
```

Install the project dependencies using `pip`:

```bash
pip install .
```

In addition, to use all of the functionality of the project, you should have:

* **Python** 3.7+

## Tests
This repo uses [pytest](https://docs.pytest.org/en/7.1.x/) testing framework.

First install the test dependencies:
```
pip install -e .[test]
```

Use the `pytest` command to run the tests in your test environment: 
```
pytest
```
