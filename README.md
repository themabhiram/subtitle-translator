# subtitle-translator
A Python tool to translate subtitle (.srt) files into multiple languages instantly.

# Subtitle Translator

A Python tool to translate subtitle (.srt) files into multiple languages instantly.

## Features

* Translate subtitle files automatically
* Supports multiple languages
* Telugu included
* Fast and simple
* Saves translated subtitle files automatically

## Supported Languages

* Hindi
* Telugu
* Spanish
* French
* German
* Japanese
* Chinese
* Arabic
* Russian
* Portuguese
* Italian

## Installation

Install requirements:

```bash id="1uxw5k"
pip install -r requirements.txt
```

## Run Tool

```bash id="hlx30l"
python main.py
```

## Build EXE

```bash id="f1sh04"
pyinstaller --onefile --console --name Subtitle_Translator main.py
```

## How To Use

1. Enter folder path containing subtitle files

2. Select subtitle file using index

Example:

```text id="3v1oyk"
[0] movie.srt
```

3. Tool automatically translates subtitles

4. Translated files are saved automatically

Example output:

```text id="qqk5qr"
movie_te.srt
movie_hi.srt
movie_fr.srt
```

## Notes

* Only `.srt` subtitle files are supported
* Internet connection is required
* Translation uses Google Translate

## Requirements

```text id="4j0f7x"
deep-translator
colorama
```

Created by **ABHIRAM**

Instagram: @themabhiram

