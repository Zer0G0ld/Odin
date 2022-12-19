#pip install pyttsx3
#Falando
import pyttsx3 
engine = pyttsx3.init()

engine.say("Python com Arduíno!")
engine.runAndWait()
engine.stop()
