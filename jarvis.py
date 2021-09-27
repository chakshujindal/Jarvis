import datetime
import webbrowser
import pyttsx3
import os
import subprocess
import speech_recognition as sr
import wikipedia
import smtplib

engine = pyttsx3.init('nsss') #Speech API
voices = engine.getProperty('voices')
# for i in range(0, len(voices)):
#     print(f"{i} = {voices[i].id}\n")

engine.setProperty('voice', voices[40].id) #Voice of Veena

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour) # typecasted to int
    if hour >= 0 and hour <= 12:
        speak("Good Morning!")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    '''
    It takes microphone input from the user and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('chakshujindal247@gmail.com', 'Lamptable@321')
    server.sendmail('chakshujindal247@gmail.com', to, body)
    server.close()

if __name__ == "__main__":
    # wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = "/Users/chakshujindal/Downloads/songs"
            songs = os.listdir(music_dir)
            action = "open"
            print(songs)
            subprocess.call([action, os.path.join(music_dir, songs[0])])
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        # elif 'open code' or 'visual studio code' or 'v s code' in query:
        #     codePath = "/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code"
        #     action = "open"
        #     subprocess.call([action, codePath])
        elif 'email' in query:
            try:
                speak("What should I say?")
                body: takeCommand()
                speak("Whom should I send to?") #Chakshu dot Jindal 2015 at the rate vit.ac.in
                to: takeCommand()
                sendEmail(to, body)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry! I am unable to send the email.")