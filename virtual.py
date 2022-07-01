import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
import cv2
import subprocess
import requests
import pyautogui

print('Loading your AI personal assistant G-11')

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)

def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")
        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your AI personal assistant G-11")
wishMe()

if __name__ == '__main__':
    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement == 0:
            continue
        if "good bye" in statement or "bye" in statement or "stop" in statement:
            speak('your personal assistant G-11 is shutting down,Good bye')
            print('your personal assistant G-11 is shutting down,Good bye')
            break
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'best friend' in statement:
            speak("My best friend is Ramesh Rathod from CSE B Section")
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open now")
            time.sleep(5)
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Gmail open now")
            time.sleep(5)
        elif 'google' in statement:
            statement = statement.replace("google", "")
            webbrowser.open_new_tab("https://google.com/search?q=" + statement)
            time.sleep(5)
        elif "weather" in statement:
            api_key = ""
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak("Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print("Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
            else:
                speak("City Not Found ")
        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am G-11 version 1 point O your persoanl assistant. I am programmed to minor tasks like opening youtube, google chrome, gmail, predict time, take a photo, search wikipedia, predict weather in different cities, get top headline news from times of india, taking screenshots, capturing photos from your webcam.')
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Group 11 of CSE B section")
            print("I was built by Group 11 of CSE B section")
        elif 'news' in statement:
            news = webbrowser.open_new_tab(
                "https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)
        elif "camera" in statement or "take a photo" in statement:
            camera_port = 0
            camera = cv2.VideoCapture(camera_port)
            time.sleep(1.0)
            return_value, image = camera.read()
            cv2.imwrite("capturedbyvirtualassistant.jpg", image)
            del(camera)
        elif "screenshot" in statement:
            image = pyautogui.screenshot()
            image.save('screenshot.png')
            speak('Screenshot taken and saved in current working directory')
        elif "shut down my pc" in statement or "sign out" in statement:
            speak(
                "Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
time.sleep(3)
