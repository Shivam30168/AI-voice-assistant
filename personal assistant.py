import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import time
import wikipedia
import pywhatkit
from googletrans import Translator
import subprocess
import requests
import os
import json
import cv2
import screen_brightness_control as s

language='hi'
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir!")

    elif hour>=12 and hour<18:
        speak("good aternoon sir!")

    else:
        speak("Good Evening sir!")
    print('"I am your desktop assistant . Tell me how may I help you')

    speak("I am your desktop assistant . Tell me how may I help you")
    

def takeCommand():

        r = sr.Recognizer()

        
        with sr.Microphone() as source:
                print('Listening')
                
                
                r.pause_threshold = 0.7
                audio = r.listen(source)
                
                
                try:
                        print("Recognizing")
                        
                        Query = r.recognize_google(audio, language='en-in')
                        print(Query)
                        
                except Exception as e:
                        print(e)
                        
                        return "None"
                
                return Query

def speak(audio):
        
        engine = pyttsx3.init()
        
        voices = engine.getProperty('voices')
        
        # setter method .[0]=male voice and
        # [1]=female voice in set Property.
        engine.setProperty('voice', voices[0].id)
        
        # Method for the speaking of the the assistant
        engine.say(audio)
        
        
        engine.runAndWait()

def tellDay():
        
        
        day = datetime.datetime.today().weekday() + 1
        
        
        Day_dict = {1: 'Monday', 2: 'Tuesday',
                                3: 'Wednesday', 4: 'Thursday',
                                5: 'Friday', 6: 'Saturday',
                                7: 'Sunday'}
        
        if day in Day_dict.keys():
                day_of_the_week = Day_dict[day]
                print(day_of_the_week)
                speak("The day is " + day_of_the_week)


def tellTime():
        
        # This method will give the time
        time = str(datetime.datetime.now())
        
        # the time will be displayed like
        # this "2020-06-05 17:50:14.582630"
        #nd then after slicing we can get time
        print(time)
        hour = time[11:13]
        min = time[14:16]
        speak("The time is sir" + hour + "Hours and" + min + "Minutes")
def Take_query():

        wishme()
        
        
        
        
        while(True):
                
                try:
                    query = takeCommand().lower()
                    if "how are you" in query:
                            speak("i am fine . what about you")
                            continue
                    
                    
                    if "open google" in query:
                            speak("Opening Google ")
                            webbrowser.open("www.google.com")
                            continue
                            
                    if "the day " in query:
                            tellDay()
                            continue
                    
                    if "the time" in query:
                            tellTime()
                            continue
                    
                    if "close" in query:
                            speak("ok Bye sir . have a good day ")
                            break
                    
                    if "from wikipedia" in query:
                            speak("Checking the wikipedia ")
                            query = query.replace("wikipedia", "")
                            result = wikipedia.summary(query, sentences=3)
                            speak("According to wikipedia")
                            speak(result)
                            print(result)
                    
                    if " your name" in query:
                            speak("I am Jarvis. Your deskstop Assistant")
                            
                    if "open youtube" in query:
                            speak("opening youtube")
                            webbrowser.open("www.youtube.com")
                            time.sleep(5)
                           
                            continue
                    if 'sing a song' in query:
                            speak('i cannot sing because my voice is not good')
                    if 'play' in query:
                            song = query.replace('play', '')
                            speak('playing ' + song)
                            pywhatkit.playonyt(song)
                            time.sleep(30)
                            
                    if 'what can you do' in query:
                            speak('i can do many things like play any song and i can tell u time also')
                    if 'speak' in query:
                            speak(query.lstrip('speak'))
                    if 'translate' in query:
                            translator = Translator()
                            translation = translator.translate(query.lstrip('translate'))
                            print(f"{translation.text} ")
                            speak(f"{translation.text} ")
                            
                            
                    if 'gmail' in query:
                        webbrowser.open_new_tab("gmail.com")
                        speak("Google mail is open now")
                        time.sleep(5)
                    if 'news' in query:
                        news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                        speak('Here are some headlines from the Times of India,Happy reading')
                        time.sleep(6)
                    if 'click photo' in query:
                            speak('clicking photo please say cheese and give an awesome pose')
                            camera = cv2.VideoCapture(0)
                            for i in range(1):
                                return_value, image = camera.read()
                                cv2.imwrite('pic'+str(i)+'.png', image)
                            del(camera)
                            time.sleep(5)
                    if 'minimum brightness' in query:
                        s.set_brightness(20)
                        speak('done sir')
                    if 'medium brightness' in query:
                        s.set_brightness(50)
                        speak('done sir')
                    if 'maximum brightness' in query:
                        s.set_brightness(100)
                        speak('done sir')
                    if "get brightness" in query:
                        speak("Current brightness is"+ str(s.get_brightness()))
                        print(s.get_brightness())
                    if 'thank you' in query :
                        print("your welcome")
                        speak('your welcome')
                    if 'open github' in query:
                        print('opening git hub ...')
                        speak('opening git hub...')
                        webbrowser.open_new('https://github.com/')
                        time.sleep(10)
                    if 'open instagram' in query :
                        print('opening instagram ...')
                        speak('opening insta gram...')
                        webbrowser.open_new('https://www.instagram.com/')
                        time.sleep(5)
                    if 'open stack overflow' in query :
                        print('opening stackoverflow ...')
                        speak('opening stack overflow...')
                        webbrowser.open_new('https://stackoverflow.com/')
                        time.sleep(5)
                    if 'bootcamps' in query :
                        search = 'http://tathastu.twowaits.in/index.html#courses'
                        v('opening boot camps')
                        webbrowser.open(search)
                    if 'boot camps' in query :
                        search = 'http://tathastu.twowaits.in/index.html#courses'
                        speak('opening boot camps')
                        webbrowser.open(search)
                    if 'python bootcamp' in query :
                        search = 'http://tathastu.twowaits.in/kickstart_python.html'
                        speak('showing pythonboot camp')
                        webbrowser.open(search)
                    if 'data science bootcamp' in query :
                        search = 'http://tathastu.twowaits.in/kickstart_data_science.html'
                        speak('showing data science and ml bootcamp')
                        webbrowser.open(search)
                    if 'where is ' or 'location of' in query :
                        speak('locating ...')
                        loc = query.replace('where is', '')
                        url = 'https://google.nl/maps/place/'+loc+'/&amp;'
                        webbrowser.get().open(url)
                        print('Here is the location of '+loc)
                        speak('Here is the location of '+loc)
                        time.sleep(10)                                
                                    
                    if 'whatsapp' in query:
                            d=time.asctime()
                            e=d.split()
                            f=e[3].split(':')
                            g=int(f[0])
                            h=int(f[1])+2
                            msg=query.replace('send whatsapp message', '')
                            speak('sending'+msg)
                            pywhatkit.sendwhatmsg("+919690300295",msg,g, h)
                                    
                    if  'turn off'in query:
                        speak("Ok , your pc will log off in 5 seconds make sure you exit from all applications")
                        subprocess.call(["shutdown", "/l"])        
                except Exception as ex:
                        speak('sorry cannot process that request')
                
                

if __name__ == '__main__':
        
        
        Take_query()
        


