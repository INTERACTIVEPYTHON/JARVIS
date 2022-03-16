import pyttsx3  # pip install pyttsx3
import datetime  # module
import speech_recognition as sr
import wikipedia
from googlesearch import *
import pywhatkit
import time as t
import smtplib
import webbrowser as wb
import os  # inbuilt
import pyautogui
import re
import psutil  # pip install psutil
import pyjokes  # pip install pyjokes
import requests, json  # inbuilt

engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('volume', 2)


# change voice
def voice_change(v):
    x = int(v)
    engine.setProperty('voice', voices[x].id)
    speak("done sir")


# speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# time function
def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)


# date function
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)


def checktime(tt):
    hour = datetime.datetime.now().hour
    if ("morning" in tt):
        if (hour >= 6 and hour < 12):
            speak("Good morning sir")
        else:
            if (hour >= 12 and hour < 18):
                speak("it's Good afternoon sir")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening sir")
            else:
                speak("it's Goodnight sir")
    elif ("afternoon" in tt):
        if (hour >= 12 and hour < 18):
            speak("Good afternoon sir")
        else:
            if (hour >= 6 and hour < 12):
                speak("Good morning sir")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening sir")
            else:
                speak("it's Goodnight sir")
    else:
        speak("it's night sir!")


# welcome function
def wishme():
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning sir!")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon sir")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening sir")
    else:
        speak("Goodnight sir")

    speak("Jarvis at your service, Please tell me how can i help you?")


def wishme_end():
    speak("signing off")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening")
    else:
        speak("Goodnight.. Sweet dreams")
    quit()


def tellDay():
    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        #print(day_of_the_week)
        speak("The day is " + day_of_the_week)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("ask...")
        r.pause_threshold = 0.9
        audio = r.listen(source)

    try:
        speak("ok!")
        query = r.recognize_google(audio, language="en-in")
        speak('you said' + query)
    except Exception as e:
        print(e)
        speak("Repeate please...")

        return "None"

    return query


# screenshot function
def screenshot():
    img = pyautogui.screenshot()
    img.save("S:/ss.png")


# battery and cpu usage
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    #print('CPU usage is at ' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    #print("battery is at:" + str(battery.percent))


# joke function
def jokes():
    j = pyjokes.get_joke()
    #print(j)
    speak(j)


def personal():
    speak(
        "I am Javis , I am an AI assistent, I am developed by Sriyut kumar singh INDIA"
    )
    speak("Now i hope you know me")


if __name__ == "__main__":
    wishme()
    while (True):
        query = takeCommand().lower()

        # time

        if ('tell time' in query):
            time()

        # date

        elif ('tell date' in query):
            date()

        # personal info
        elif ("tell me about yourself" in query):
            personal()
        elif ("about you" in query):
            personal()
        elif ("who are you" in query):
            personal()
        elif ("yourself" in query):
            personal()

            # searching on wikipedia

        elif ('what' in query or 'who' in query
              or 'when' in query or 'where' in query or 'is' in query or 'from ' in query or 'about' in query):
            speak("searching...")
            query = query.replace("search", "")
            query = query.replace("what", "")
            query = query.replace("when", "")
            query = query.replace("where", "")
            query = query.replace("who", "")
            query = query.replace("is", "")
            query = query.replace("from", "")
            query = query.replace("about", "")
            result = wikipedia.summary(query, sentences=15)
            print(result)
            result = wikipedia.summary(query, sentences=2)
            speak(result)
            speak("For your convineance i am printing it on the screen")

        elif "day" in query or "tell me day" in query:
            tellDay()

        elif ("find" in query or "open website" in query):
            speak("What should i search or open?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search)
            print(search)

        elif ('search on youtube' in query or 'youtube' in query):
            speak("what to search on youtube")
            sea = takeCommand().lower()
            you = "https://www.youtube.com/results?search_query=" + sea
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            wb.get(chromepath).open_new_tab(you)
            speak('Done')

        elif ('location' in query or 'map' in query):
            speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + (location) + '/&amp;'
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            speak('Here is the location ' + location)
            wb.get(chromepath).open_new_tab(url)

        # sysytem logout/ shut down etc
        elif ("shutdown" in query):
            os.system("shutdown /s /t 0")

        # play songs

        elif ("play song" in query):
            speak("Playing...")
            songs_dir = "C:/Users/delll1/Music"
            songs = os.listdir(songs_dir)
            os.startfile((songs_dir))
            quit()

        # reminder function

        elif ("create a reminder list" in query or "reminder" in query):
            speak("What is the reminder?")
            data = takeCommand()
            speak("You said to remember that" + data)
            reminder_file = open("data.txt", 'a')
            reminder_file.write('\n')
            reminder_file.write(data)
            reminder_file.close()

        # reading reminder list

        elif ("do you know anything" in query or "remember" in query):
            reminder_file = open("data.txt", 'r')
            speak("You said me to remember that: " + reminder_file.read())

        # screenshot
        elif ("screenshot" in query):
            screenshot()
            speak("Done!")

        # cpu and battery usage
        elif ("cpu and battery" in query or "battery" in query
              or "cpu" in query):
            cpu()

        # jokes
        elif ("tell me a joke" in query or "joke" in query):
            jokes()

        # weather
        elif ("weather" in query or "temperature" in query):
            weather()

        # javis features
        elif ("what can you do" in query or 'features' in query):
            features = ''' i can help to do lot many things like..
            i can tell you the current time and date,
            i can tell you the current weather,
            i can tell you battery and cpu usage,
            i can create the reminder list,
            i can take screenshots,
            i can shut down or logout or hibernate your system,
            i can tell you non funny jokes,
            i can open any website,
            i can search the thing on wikipedia,
            i can change my voice from male to female and vice-versa
            i can tell you the location which you want
            '''
            speak(features)

        elif ("hii" in query or "hello" in query or "goodmorning" in query
              or "goodafternoon" in query or "goodnight" in query
              or "morning" in query or "noon" in query or "night" in query):
            query = query.replace("jarvis", "")
            query = query.replace("hi", "")
            query = query.replace("hello", "")
            if ("morning" in query or "night" in query or "goodnight" in query
                    or "afternoon" in query or "noon" in query):
                checktime(query)
            else:
                speak("what can i do for you")

        # changing voice
        elif ("voice" in query):
            speak("for female say female and, for male say male")
            q = takeCommand()
            if ("female" in q):
                voice_change(1)
            elif ("male" in q):
                voice_change(0)
        elif ("male" in query or "female" in query):
            if ("female" in query):
                voice_change(1)
            elif ("male" in query):
                voice_change(0)

        elif 'tell me news' in query or 'tell news' in query:
            speak('opening')
            wb.open("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")

        elif 'open meet' in query or 'google meet' in query:
            speak('ok...opening')
            wb.open("https://meet.google.com")

        elif 'whatsapp' in query:
            speak('to whom sir /n pleas tell m the number')
            a = takeCommand()
            speak("sir tell me what i have to send")
            d = takeCommand()
            speak('Sir pleas tell me the time in hour')
            b = takeCommand()
            speak('And sir at how much minute')
            c = takeCommand()
            speak("ok sir. I will send it.")
            pywhatkit.sendwhatmsg('+91 '+ a, d, b, c)

        elif (
                'exit' in query or 'bye jarvis' in query or 'go offline jarvis' in query or 'bye' in query or 'nothing' in query or 'close' in query):
            wishme_end()
            break
