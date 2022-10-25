#pyttsx3 module
import pyttsx3
engine = pyttsx3.init()
for voice in engine.getProperty("voices"):
    print(voice)
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[10].id)
def speak(Audio):
    engine.say(Audio)
    engine.runAndWait()
text=input("enter your text now: ")
speak(text)
