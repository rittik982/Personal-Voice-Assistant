# Importing Libraries
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests, json, sys
from newsapi import NewsApiClient
import pycountry
import webbrowser
import os
import shutil
import time

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate + 10)
volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0.05)


def engine_talk(text):
    engine.say(text)
    engine.runAndWait()


def weather(city):
    api_key = "Your API key here"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        return str(current_temperature)

def user_commands():
    try:
        with sr.Microphone() as source:
            print("Listening!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'aurora' in command:
                command = command.replace('aurora', '')
                print(command)
    except:
        print("No Command given!")
        pass
    return command


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        engine_talk("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        engine_talk("Good Afternoon Sir !")  
  
    else:
        engine_talk("Good Evening Sir !") 
  
    assname =("Aurora")
    engine_talk("I am your Assistant")
    engine_talk(assname)

def username():
    engine_talk("What should i call you sir")
    uname = user_commands()
    engine_talk("Welcome Mister")
    engine_talk(uname)
    columns = shutil.get_terminal_size().columns
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
    engine_talk("How can i Help you, Sir")

def news():
    url="https://newsapi.org/v2/top-headlines?country=in&from=2023-03-02&apiKey=c059e65451074577a3529fbe26f6f63d"
    #url = ('https://newsapi.org/v2/top-headlines?'
     #      'country = in&'
      #     'apiKey =your api key here')
    try:
        response = requests.get(url)
    except:
        engine_talk("can, t access link, plz check you internet ")
    news = json.loads(response.text)
    for new in news['articles']:
        print("##############################################################\n")
        print(str(new['title']), "\n\n")
        engine_talk(str(new['title']))
        print('______________________________________________________\n')
        engine.runAndWait()
        print(str(new['description']), "\n\n")
        engine_talk(str(new['description']))
        engine.runAndWait()
        print("..............................................................")
        time.sleep(2)    
    
    
def run_alexa():
    command = user_commands()
    if 'play' in command:
        song = command.replace('play', '')
        engine_talk('Playing' + song)
        pywhatkit.playonyt(song)
        print('Playing Song')
    elif 'search' in command:
        find = command.replace('search', '')
        engine_talk('Searching' + find)
        pywhatkit.search(find)
        print('Searching')
    elif 'send' in command:
        send = command.replace('send', '')
        engine_talk('Sending' + send)
        pywhatkit.sendwhatmsg("+919079692552", "Hey Trilok!", 16, 47)
        print("Successfully Sent!")
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        engine_talk('The current time is' + time)
    elif 'day' in command:
        day = datetime.datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday',
                    3: 'Wednesday', 4: 'Thursday',
                    5: 'Friday', 6: 'Saturday',
                    7: 'Sunday'}
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            print(day_of_the_week)
            engine_talk("The day is " + day_of_the_week)
 
    elif 'who is' in command:
        name = command.replace('who is', '')
        info = wikipedia.summary(name, 3)
        print(info)
        engine_talk(info)
    elif 'news' in command:
        news()
    elif 'temperature' in command:
        engine_talk('Please tell the name of the city')
        city = user_commands()
        weather_api = weather(city)
        engine_talk(weather_api + 'kelvin')
    elif "where is" in command:
        command = command.replace("where is", "")
        location = command
        engine_talk("User asked to Locate")
        engine_talk(location)
        webbrowser.open("https://www.google.nl / maps / place/" + location + "")
    elif 'joke' in command:
        engine_talk(pyjokes.get_joke())
    elif "will you be my gf" in command or "will you be my bf" in command:  
        engine_talk("I'm not sure about, may be you should give me some time")
    elif "i love you" in command:
        engine_talk("It's hard to understand")
    elif "who i am" in command:
        engine_talk("If you talk then definitely your human.")
    elif "why you came to world" in command:
        engine_talk("Thanks to Rittik. further It's a secret")
    elif 'is love' in command:
        engine_talk("It is 7th sense that destroy all other senses")
    elif "who are you" in command:
        engine_talk("I am your virtual assistant Aurora created by Hrithik")
    elif 'reason for you' in command:
        engine_talk("I was created as a Minor project by Mister Hrithik ")
    elif 'how are you' in command:
        engine_talk("I am fine, Thank you")
        engine_talk("How are you, Sir")
    elif 'fine' in command or "good" in command:
        engine_talk("It's good to know that your fine")
    elif "don't listen" in command or "stop listening" in command:
            engine_talk("for how much time you want to stop alexa from listening commands")
            a = int(user_commands())
            time.sleep(a)
            print(a)
    elif 'stop' in command:
        engine_talk("Thanks for giving me your time")
        sys.exit()
    else:
        engine_talk('I am not getting you properly. Please try again!')

if __name__ == '__main__':
    clear = lambda: os.system('cls')
  
    clear()
    wishMe()
    username()
    while True:
        run_alexa()


