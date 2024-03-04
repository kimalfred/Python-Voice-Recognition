import os
import requests
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-us')
        print("User said:", query)
        return query
    except Exception as e:
        print("Error:", str(e))
        return ""
    

def get_weather_data(api_key, city, country_code):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": f"{city},{country_code}",
        "APPID": api_key
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status() 
        weather_data = response.json()
        return weather_data  
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        print(response.content) 
        return None
    

def handle_command(command, weather_data):
    if "hello" in command.lower():
        speak("Hello! How can I help you?")

    elif "time" in command.lower():
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")

    elif "date" in command.lower():
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {today}")

    elif "thank you" in command.lower():
        speak("You're welcome! If you have any more questions, feel free to ask.")

    elif "search facebook" in command.lower():
        speak("Searching for Facebook...")
        webbrowser.open("https://www.facebook.com")
        
    elif "search twitter" in command.lower():
        speak("Searching for Twitter...")
        webbrowser.open("https://www.twitter.com")
    
    elif "search stack overflow" in command.lower():
        speak("Searching for Stackoverflow...")
        webbrowser.open("https://www.stackoverflow.com")

    elif "search youtube" in command.lower():
        speak("Searching for Youtube...")
        webbrowser.open("https://www.youtube.com")

    elif "search instagram" in command.lower():
        speak("Searching for Instagram...")
        webbrowser.open("https://www.instagram.com")

    elif "search github" in command.lower():
        speak("Searching for GitHub...")
        webbrowser.open("https://www.github.com")

    elif "search google" in command.lower():
        speak("Searching for Google...")
        webbrowser.open("https://www.google.com")

    elif "search chat gpt" in command.lower():
        speak("Searching for ChatGPT...")
        webbrowser.open("https://chat.openai.com")

    elif "weather" in command.lower():
        if weather_data:
            temperature_kelvin = weather_data['main']['temp']
            temperature_celsius = temperature_kelvin - 273.15
            description = weather_data['weather'][0]['description']
            speak(f"The current temperature in {city} is {temperature_celsius:.2f} degrees Celsius, with {description}.")
        else:
            speak("Failed to fetch weather data. Please try again later.")

    elif "news" in command.lower():
        speak("Sorry, I don't have news information right now.")

    elif "tell a joke" in command.lower():
        speak("Why do programmers prefer dark mode? Because light attracts bugs! HAHAHA")
    
    elif "open notepad" in command.lower():
        speak("Opening Notepad...")
        os.system("notepad.exe")    
    
    elif "open word" in command.lower():
        speak("Opening Microsoft Word...")
        os.system("start winword.exe")

    elif "open spotify" in command.lower():
        speak("Opening Spotify...")
        os.system("start spotify.exe")

    elif "open file manager" in command.lower():
        speak("Opening File Manager...")
        os.system("explorer.exe")

    elif "exit" in command.lower():
        speak("Goodbye!...")
        exit()
    else:
        speak("Sorry, I didn't understand that.")

def main():
    speak("Hello! How can I help you?")
    while True:
        command = recognize_speech()
        handle_command(command, weather_data)

if __name__ == "__main__":
    api_key = "3fba9763eaebb0eb2df0841c84029d15"
    city = "Taguig City"
    country_code = "ph"

    weather_data = get_weather_data(api_key, city, country_code)

    main()
