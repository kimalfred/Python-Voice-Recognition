# Simple Voice Recognition Using Python

Simple Python voice recognition that User can use voice command to communicate with their computer. 
## Features

- **Voice Recognition:** This system understands speech through the SpeechRecognition library.
- **Text to Speech:** Converting text responses to spoken speech by using the pyttsx3 package.
- **Weather information:** Using the OpenWeatherMap API, this resource provides up-to-date meteorological information for a specific city.
- **Web Search:** From the voice assistant, users can search various websites, including GitHub, Facebook, Instagram, YouTube, Twitter, Stack Overflow, Google, and ChatGPT.
- **OS Activity:** Capable of launching programs like Notepad, Microsoft Word, File Manager, and Spotify, among other basic system activities.
- **Time & Date:** Provides the current time and date.


## Usage/Examples
1. Install Voice Recognition:
```
pip install SpeechRecognition pyttsx3 requests

```
2. Get an API key from [OpenWeatherMap](https://openweathermap.org/api) and use your real API key in line of `{'YOUR_API_KEY'}` in the code.

```python
    api_key = "  " #use your own api key
    city = "  " #select different city
    country_code = "  "  #your country code
```
3. When asked, speak your command and communicate with the voice assistant.

## Requirements

- Python 3.x
- SpeechRecognition
- pyttsx3
- requests



