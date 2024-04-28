#!/usr/bin/env python

from setuptools import find_packages

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md") as readme_file:
    readme = readme_file.read()

test_requirements = ["pytest"]

extras = {
    "test": test_requirements,
}

setup(
    name="marshall-fire-speech-recognizer",
    version="0.1.0",
    author="Lindsey Nield",
    author_email="lindsey.g.nield@gmail.com",
    description="Speech recognizer for Marashall fire response scanner audio.",
    long_description=readme,
    url="https://github.com/lindseynield/marshall-fire-speech-recognizer",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.7,<3.9",
    install_requires=[
        "folium",
        "geopandas",
        "matplotlib",
        "numpy",
        "pydub",
        "rasterio",
        "sentinelsat",
        "shapely",
        "SpeechRecognition",
        "tifffile",
        "typing_extensions",
    ],
    tests_require=test_requirements,
    extras_requires=extras,
    packages=find_packages(exclude=["*.tests", "*tests.*", "tests.*", "tests"]),
    include_package_data=True,
)
