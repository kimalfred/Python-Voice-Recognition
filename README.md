#Voice Recognition

This is a basic Python voice assistant application. Users can use voice commands to communicate with their computer.

## Features

- **Voice Recognition:** The application recognizes user-spoken voice instructions by utilizing the SpeechRecognition library.
**Text-to-Speech:** Transforms text replies into spoken speech by using the pyttsx3 package.
**Weather Information:** Using the OpenWeatherMap API, this resource provides up-to-date meteorological information for a given city.
- **Web Search:** From the voice assistant, users may look up a variety of websites, including GitHub, Facebook, Instagram, YouTube, Twitter, Stack Overflow, Google, and ChatGPT.
- **fundamental System activities:** Able to launch programs like Notepad, Microsoft Word, File Manager, and Spotify, among other fundamental system activities.
- **Time and Date:** Upon request, provides the current time and date.
- **Jokes:** Tells a funny joke when asked.

## Usage

1. Make a local copy of the repository on your computer.
2. Use `pip install -r requirements.txt` to install the necessary dependencies.
3. Get an API key from [OpenWeatherMap](https://openweathermap.org/api) and use your real API key in lieu of `'YOUR_API_KEY'} in the code.
4. Enter the country and city codes that you desire.
5. Launch the file `main.py`.
6. When asked, speak your command and communicate with the voice assistant.

## Requirements

- Python 3.x
- SpeechRecognition
- pyttsx3
- requests


