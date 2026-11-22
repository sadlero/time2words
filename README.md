# time2words 🕒

A simple Python program that converts the current time into words.

## Features

- Converts 24-hour time into 12-hour spoken time.
- Converts numbers into words.
- Uses "oh" for single-digit minutes (e.g. 1:05 → "one oh five").
- Recognizes a quarter past, half past, and a quarter to.
- Includes a special a "Make a wish!" message for matching-digit times.

## Requirements

- Python 3
- [num2words](https://pypi.org/project/num2words/)

## Installation

Install the required library:

```bash
pip install num2words
```

## Usage

Run the Python script:

```bash
python time2words.py
```

The program automatically reads your computer's current local time and converts it into words in standard American English.

## Example output

```text
The time is one oh six.
The time is a quarter past three.
The time is five fifty-five. Make a wish!
It's midnight.
```

## Built with

- Python
- [num2words](https://pypi.org/project/num2words/). 
