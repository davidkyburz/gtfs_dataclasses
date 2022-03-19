from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gtfs_dataclasses",
    author="David Kyburz",
    author_email="davidkyburz@users.noreply.github.com ",
    version="0.1.0",
    description="Python data classes mapping Google's static General Transit Feed Specification (GTFS)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/davidkyburz/gtfs_dataclasses",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
