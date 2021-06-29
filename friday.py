import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import os
import smtplib, ssl
import requests, json
from pprint import pprint
from selenium import webdriver
from PyDictionary import PyDictionary
import time
import wolframalpha
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()  

def wishMe():
    speak("Welcome back sir")
    hour = int(datetime.datetime.now().hour)
    print(hour)
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    print(Time)
    print(date)
    print(month)
    print(year)
    speak("the current Time is")
    speak(Time)
    speak("the current Date is")
    speak(date)
    speak(month)
    speak(year)
    if hour>=6 and hour<12:
        speak("Good Morning Mr. Stark!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Mr. Stark!")

    elif hour>=18 and hour<24:
        speak("Good Evening Mr. Stark!")

    else:
        speak("Good Night Mr. Stark!")

    speak("Friday at your Service. Please tell me how can I help You ")
#wishMe()
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Mr. Stark Said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again Please...")
        speak("Say that again Please...")
        query = "Get Lost"
    return query
   
def code():
    try:
        speak("Enter a passcode")
        codes = int(input("Enter a passcode sir/ma'am:"))
        if codes == 1256:
            speak("Recognizing person")
            if __name__ == "__main__":
                wishMe()
                while True:
                    query = takeCommand().lower()


                    if 'wikipedia' in query:
                        speak('Searching Wikipedia...')
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=3)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)

                    elif "who made you" in query:
                        speak("I have been created by Ashirwad Mishra.")

                    elif 'search in google' in query:
                        speak("what should i search?")
                        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

                        r = sr.Recognizer()

                        with sr.Microphone() as source:
                            print('say something!')
                            audio = r.listen(source)
                        try:
                            text = r.recognize_google(audio)
                            print('google think you said:\n' +text)
                            speak("Should I search?")
                            rock = takeCommand().lower()
                            if rock == 'yes':
                                speak("Done")
                                wb.get(chrome_path).open(text)
                            elif rock == 'no':
                                speak("OK Sir")
                        except Exception as e:
                            print(e)


                    elif 'wait' in query:
                        try:
                            speak("Waiting Sir!!!")
                            time.sleep(30)
                            speak("Should I finish the waiting period")
                            druck = takeCommand().lower()
                            if druck == 'no':
                                speak("OK Sir, Incresing the waiting period")
                                time.sleep(300)
                            elif druck == 'yes':
                                speak("OK Sir, continuing the tasks")
                        except Exception as e:
                            print(e)
                       

                    elif "calculate" in query:
                        try:
                            app_id = "W54KPK-T5RAEJT6H9"
                            client = wolframalpha.Client(app_id)
                 
                            indx = query.split().index('calculate')
                            query = query.split()[indx + 1:]
                            res = client.query(' '.join(query))
                            answer = next(res.results).text
                            print("The answer is " + answer)
                            speak("The answer is " + answer)

                        except:
                            speak("Sorry! Sir")

                    elif 'element' in query:
                        url = "rsc.org/periodic-table"
                        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                        wb.get(chrome_path).open(url)

                    elif 'meaning' in query:
                        try:
                            speak("Say a word")
                            searchWord = takeCommand().lower()
                            myDict = PyDictionary(searchWord)
                            speak(myDict.getMeanings())

                        except:
                            speak("Sorry sir cannot find the meaning")

                    elif 'how is the weather' and 'weather' in query:
                        api_key = "20f7ce2507e0d0b804f47c4fc5ffec28"
                        base_url = "http://api.openweathermap.org/data/2.5/weather?"
                        print("What is the name of your city")
                        speak("What is the name of your city")
                        city_name = takeCommand().lower()
                        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                        response = requests.get(complete_url)
                        x = response.json()
                        if x["cod"] != "404":
                            y = x["main"]
                            current_temperature = y["temp"]
                            current_pressure = y["pressure"]
                            current_humidiy = y["humidity"]
                            z = x["weather"]
                            weather_description = z[0]["description"]
                            print("Temperature (in kelvin unit) = " +
                                            str(current_temperature) +
                                  "\n atmospheric pressure (in hPa unit) = " +
                                            str(current_pressure) +
                                  "\n humidity (in percentage) = " +
                                            str(current_humidiy) +
                                  "\n description = " +
                                            str(weather_description))
                            speak("Temperature (in kelvin unit) = " +
                                            str(current_temperature) +
                                  "\n atmospheric pressure (in hPa unit) = " +
                                            str(current_pressure) +
                                  "\n humidity (in percentage) = " +
                                            str(current_humidiy) +
                                  "\n description = " +
                                            str(weather_description))
                        else:
                            speak(" City Not Found ")


                    elif 'time' in query:
                        strTime = datetime.datetime.now().strftime("%I:%M:%S")    
                        speak(f"Sir, the time is {strTime}")
                   
                    elif 'date' in query:
                        year = int(datetime.datetime.now().year)
                        month = int(datetime.datetime.now().month)
                        date = int(datetime.datetime.now().day)
                        speak("the current Date is")
                        speak(date)
                        speak(month)
                        speak(year)


                    elif 'send email' in query:
                        try:
                            sender_email = input("What is your email: ")
                            speak("Whom should I write to?")
                            rec_email = input(str("Enter reciever's address: "))
                            password = input(str("Enter your password: "))
                            speak("What should I write?")
                            message = takeCommand()
                            server = smtplib.SMTP('smtp.gmail.com', 587)
                            server.starttls()
                            server.login(sender_email, password)
                            print("Login success")
                            server.sendmail(sender_email, rec_email, message)
                            print("Email has been sent to", rec_email)
                        except Exception as e:
                            print(e)
                            speak("Sorry my friend . I am not able to send this email")      

                    elif 'open code' in query:
                        codePath = "C:\\Microsoft VS Code\\Code.exe"
                        os.startfile(codePath)


                    elif 'open' in query:
                        os.system('explorer C://{}'.format(query.replace('Open','')))

                    elif 'set volume' in query:
                        speak("what should i set it to")
                        trump = float(input("Enter a volume number: "))
                        devices = AudioUtilities.GetSpeakers()
                        interface = devices.Activate(
                            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                        volume = cast(interface, POINTER(IAudioEndpointVolume))
                        volume.GetMute()
                        volume.GetMasterVolumeLevel()
                        volume.GetVolumeRange()
                        volume.SetMasterVolumeLevel(trump, None)




                    elif 'go offline' in query:
                        speak("ok sir shutting down the system")
                        quit()
        else:
            speak("You are not in my system..Sorry!!")
            speak("If you wish to be added. Enter your name and I will contact my boss")
            name = input("Please enter you name: ")
            if name == 'tony stark':
                if __name__ == "__main__":
                    wishMe()
                    while True:
                        query = takeCommand().lower()


                        if 'wikipedia' in query:
                            speak('Searching Wikipedia...')
                            query = query.replace("wikipedia", "")
                            results = wikipedia.summary(query, sentences=3)
                            speak("According to Wikipedia")
                            print(results)
                            speak(results)

                        elif "who made you" in query:
                            speak("I have been created by Ashirwad Mishra.")

                        elif 'search in google' in query:
                            speak("what should i search?")
                            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

                            r = sr.Recognizer()

                            with sr.Microphone() as source:
                                print('say something!')
                                audio = r.listen(source)
                            try:
                                text = r.recognize_google(audio)
                                print('google think you said:\n' +text)
                                speak("Should I search?")
                                rock = takeCommand().lower()
                                if rock == 'yes':
                                    speak("Done")
                                    wb.get(chrome_path).open(text)
                                elif rock == 'no':
                                    speak("OK Sir")
                            except Exception as e:
                                print(e)
                       
                        elif 'team' in query:
                            url = "https://teams.microsoft.com/_#/school//?ctx=teamsGrid"
                            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                            wb.get(chrome_path).open(url)

                        elif 'wait' in query:
                            try:
                                speak("Waiting Sir!!!")
                                time.sleep(30)
                                speak("Should I finish the waiting period")
                                druck = takeCommand().lower()
                                if druck == 'no':
                                    speak("OK Sir, Incresing the waiting period")
                                    time.sleep(300)
                                elif druck == 'yes':
                                    speak("OK Sir, continuing the tasks")
                            except Exception as e:
                                print(e)
                           

                        elif 'play movie' in query:
                            movie = "C:\\Users\\jpmishra\\Desktop\\a movie"
                            movies = os.listdir(movie)
                            os.startfile(os.path.join(movie, movies[0]))

                        elif "calculate" in query:
                            try:
                                app_id = "W54KPK-T5RAEJT6H9"
                                client = wolframalpha.Client(app_id)
                     
                                indx = query.split().index('calculate')
                                query = query.split()[indx + 1:]
                                res = client.query(' '.join(query))
                                answer = next(res.results).text
                                print("The answer is " + answer)
                                speak("The answer is " + answer)

                            except:
                                speak("Sorry! Sir")

                        elif 'element' in query:
                            url = "rsc.org/periodic-table"
                            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                            wb.get(chrome_path).open(url)

                        elif 'meaning' in query:
                            try:
                                speak("Say a word")
                                searchWord = takeCommand().lower()
                                myDict = PyDictionary(searchWord)
                                speak(myDict.getMeanings())

                            except:
                                speak("Sorry sir cannot find the meaning")

                        elif 'how is the weather' and 'weather' in query:
                            api_key = "20f7ce2507e0d0b804f47c4fc5ffec28"
                            base_url = "http://api.openweathermap.org/data/2.5/weather?"
                            city_name = takeCommand().lower()
                            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                            response = requests.get(complete_url)
                            x = response.json()
                            if x["cod"] != "404":
                                y = x["main"]
                                current_temperature = y["temp"]
                                current_pressure = y["pressure"]
                                current_humidiy = y["humidity"]
                                z = x["weather"]
                                weather_description = z[0]["description"]
                                print("Temperature (in kelvin unit) = " +
                                                str(current_temperature) +
                                      "\n atmospheric pressure (in hPa unit) = " +
                                                str(current_pressure) +
                                      "\n humidity (in percentage) = " +
                                                str(current_humidiy) +
                                      "\n description = " +
                                                str(weather_description))
                                speak("Temperature (in kelvin unit) = " +
                                                str(current_temperature) +
                                      "\n atmospheric pressure (in hPa unit) = " +
                                                str(current_pressure) +
                                      "\n humidity (in percentage) = " +
                                                str(current_humidiy) +
                                      "\n description = " +
                                                str(weather_description))
                            else:
                                speak(" City Not Found ")


                        elif 'the time' in query:
                            strTime = datetime.datetime.now().strftime("%I:%M:%S")    
                            speak(f"Sir, the time is {strTime}")
                       
                        elif 'the date' in query:
                            year = int(datetime.datetime.now().year)
                            month = int(datetime.datetime.now().month)
                            date = int(datetime.datetime.now().day)
                            speak("the current Date is")
                            speak(date)
                            speak(month)
                            speak(year)


                        elif 'send email' in query:
                            try:
                                sender_email = "ashirwadmishra05@gmail.com"
                                speak("Whom should I write to?")
                                rec_email = input(str("Enter reciever's address: "))
                                password = input(str("Enter your password: "))
                                speak("What should I write?")
                                message = takeCommand()
                                server = smtplib.SMTP('smtp.gmail.com', 587)
                                server.starttls()
                                server.login(sender_email, password)
                                print("Login success")
                                server.sendmail(sender_email, rec_email, message)
                                print("Email has been sent to", rec_email)
                            except Exception as e:
                                print(e)
                                speak("Sorry my friend . I am not able to send this email")      

                        elif 'open code' in query:
                            codePath = "C:\\Microsoft VS Code\\Code.exe"
                            os.startfile(codePath)


                        elif 'open' in query:
                            os.system('explorer C://{}'.format(query.replace('Open','')))

                        elif 'set volume' in query:
                            speak("what should i set it to")
                            trump = float(input("Enter a volume number: "))
                            devices = AudioUtilities.GetSpeakers()
                            interface = devices.Activate(
                                IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                            volume = cast(interface, POINTER(IAudioEndpointVolume))
                            volume.GetMute()
                            volume.GetMasterVolumeLevel()
                            volume.GetVolumeRange()
                            volume.SetMasterVolumeLevel(trump, None)




                        elif 'go offline' in query:
                            speak("ok sir shutting down the system")
                            quit()
            elif name == 'Tony Stark':
                if __name__ == "__main__":
                    wishMe()
                    while True:
                        query = takeCommand().lower()


                        if 'wikipedia' in query:
                            speak('Searching Wikipedia...')
                            query = query.replace("wikipedia", "")
                            results = wikipedia.summary(query, sentences=3)
                            speak("According to Wikipedia")
                            print(results)
                            speak(results)

                        elif "who made you" in query:
                            speak("I have been created by Ashirwad Mishra.")

                        elif 'search in google' in query:
                            speak("what should i search?")
                            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

                            r = sr.Recognizer()

                            with sr.Microphone() as source:
                                print('say something!')
                                audio = r.listen(source)
                            try:
                                text = r.recognize_google(audio)
                                print('google think you said:\n' +text)
                                speak("Should I search?")
                                rock = takeCommand().lower()
                                if rock == 'yes':
                                    speak("Done")
                                    wb.get(chrome_path).open(text)
                                elif rock == 'no':
                                    speak("OK Sir")
                            except Exception as e:
                                print(e)
                       
                        elif 'team' in query:
                            url = "https://teams.microsoft.com/_#/school//?ctx=teamsGrid"
                            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                            wb.get(chrome_path).open(url)

                        elif 'wait' in query:
                            try:
                                speak("Waiting Sir!!!")
                                time.sleep(30)
                                speak("Should I finish the waiting period")
                                druck = takeCommand().lower()
                                if druck == 'no':
                                    speak("OK Sir, Incresing the waiting period")
                                    time.sleep(300)
                                elif druck == 'yes':
                                    speak("OK Sir, continuing the tasks")
                            except Exception as e:
                                print(e)
                           

                        elif 'play movie' in query:
                            movie = "C:\\Users\\jpmishra\\Desktop\\a movie"
                            movies = os.listdir(movie)
                            os.startfile(os.path.join(movie, movies[0]))

                        elif "calculate" in query:
                            try:
                                app_id = "W54KPK-T5RAEJT6H9"
                                client = wolframalpha.Client(app_id)
                     
                                indx = query.split().index('calculate')
                                query = query.split()[indx + 1:]
                                res = client.query(' '.join(query))
                                answer = next(res.results).text
                                print("The answer is " + answer)
                                speak("The answer is " + answer)

                            except:
                                speak("Sorry! Sir")

                        elif 'element' in query:
                            url = "rsc.org/periodic-table"
                            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                            wb.get(chrome_path).open(url)

                        elif 'meaning' in query:
                            try:
                                speak("Say a word")
                                searchWord = takeCommand().lower()
                                myDict = PyDictionary(searchWord)
                                speak(myDict.getMeanings())

                            except:
                                speak("Sorry sir cannot find the meaning")

                        elif 'how is the weather' and 'weather' in query:
                            api_key = "20f7ce2507e0d0b804f47c4fc5ffec28"
                            base_url = "http://api.openweathermap.org/data/2.5/weather?"
                            city_name = takeCommand().lower()
                            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                            response = requests.get(complete_url)
                            x = response.json()
                            if x["cod"] != "404":
                                y = x["main"]
                                current_temperature = y["temp"]
                                current_pressure = y["pressure"]
                                current_humidiy = y["humidity"]
                                z = x["weather"]
                                weather_description = z[0]["description"]
                                print("Temperature (in kelvin unit) = " +
                                                str(current_temperature) +
                                      "\n atmospheric pressure (in hPa unit) = " +
                                                str(current_pressure) +
                                      "\n humidity (in percentage) = " +
                                                str(current_humidiy) +
                                      "\n description = " +
                                                str(weather_description))
                                speak("Temperature (in kelvin unit) = " +
                                                str(current_temperature) +
                                      "\n atmospheric pressure (in hPa unit) = " +
                                                str(current_pressure) +
                                      "\n humidity (in percentage) = " +
                                                str(current_humidiy) +
                                      "\n description = " +
                                                str(weather_description))
                            else:
                                speak(" City Not Found ")
                               
                        elif 'the time' in query:
                            strTime = datetime.datetime.now().strftime("%I:%M:%S")    
                            speak(f"Sir, the time is {strTime}")
                       
                        elif 'the date' in query:
                            year = int(datetime.datetime.now().year)
                            month = int(datetime.datetime.now().month)
                            date = int(datetime.datetime.now().day)
                            speak("the current Date is")
                            speak(date)
                            speak(month)
                            speak(year)


                        elif 'send email' in query:
                            try:
                                sender_email = "ashirwadmishra05@gmail.com"
                                speak("Whom should I write to?")
                                rec_email = input(str("Enter reciever's address: "))
                                password = input(str("Enter your password: "))
                                speak("What should I write?")
                                message = takeCommand()
                                server = smtplib.SMTP('smtp.gmail.com', 587)
                                server.starttls()
                                server.login(sender_email, password)
                                print("Login success")
                                server.sendmail(sender_email, rec_email, message)
                                print("Email has been sent to", rec_email)
                            except Exception as e:
                                print(e)
                                speak("Sorry my friend . I am not able to send this email")      

                        elif 'open code' in query:
                            codePath = "C:\\Microsoft VS Code\\Code.exe"
                            os.startfile(codePath)


                        elif 'open' in query:
                            os.system('explorer C://{}'.format(query.replace('Open','')))

                        elif 'set volume' in query:
                            speak("what should i set it to")
                            trump = float(input("Enter a volume number: "))
                            devices = AudioUtilities.GetSpeakers()
                            interface = devices.Activate(
                                IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                            volume = cast(interface, POINTER(IAudioEndpointVolume))
                            volume.GetMute()
                            volume.GetMasterVolumeLevel()
                            volume.GetVolumeRange()
                            volume.SetMasterVolumeLevel(trump, None)




                        elif 'go offline' in query:
                            speak("ok sir shutting down the system")
                            quit()
            else:
                speak("Contacting mister stark")
                print("Contacting...")
                time.sleep(7)
                speak("Sorry sir/ma'am he denied your request")
    except Exception as e:
        speak("Sorry sir")
code()

