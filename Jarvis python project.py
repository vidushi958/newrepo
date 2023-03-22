import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices) to check voices present in your system
print(voices[1].id) #at[0] DAVID name voice is present and at [1]ZIRA name voice is present
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait() 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How may i help you")

def takeCommand():   #it takes microphone input from the user and returns string output
    r = sr.Recognizer() #to rocognize voice
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1 #seconds of non=speaking audio before a phrase is considered complete
        audio = r.listen(source)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, Language='en=in')
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please.....")
        return "None"
    return query

if __name__ == "__main__":
    speak("Hi Yashleen, vipin, vidushi")
    wishMe()
    takeCommand()
