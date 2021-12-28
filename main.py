import speech_recognition as sr 
import pyttsx3 
import wave  
import json  
import os  
commands = {
#("Ева Сворачиваемся", "Ева Stop", "exit", "Ева Заканчиваем"): play_stop,
#("Ева Найди в гугле", "Ева найди в гугл", "Ева найди"): search_on_google,
#("Найди в вики", "Ева Найди в википедии"): serch_on_wiki,
#("weather", "forecast", "Ева погода", "Ева прогноз"): get_weather_forecast
}

#Начнем с инициализации pytttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine,getPropety('volume')
engine.setProperty("voice", voices[0].id)

#Теперь speech_recognition 
r=sr.Recognizer()
m=sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)





engine.runAndWait()
