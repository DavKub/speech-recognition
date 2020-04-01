import speech_recognition as sr
import webbrowser
import time
import random
import os
import playsound
from gtts import gTTS

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            alexis_speak(ask)
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alexis_speak("Sorry, I did not understand that.")
        except sr.RequestError:
            alexis_speak("Sorry, my speech service is down.")
        return voice_data


def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    rnd = random.randint(1, 10000000)
    audio_file = "audio-" + str(rnd) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if "what is your name" in voice_data:
        alexis_speak("My name is Friday")

    if "what time is it" in voice_data:
        print(time.ctime())

    if 'search' in voice_data:
        search = record_audio("What do you want to search for?")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        alexis_speak("Here is what I found on " + search)

    if 'find location' in voice_data:
        location = record_audio("What location do you want me to search for?")
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        alexis_speak("Here is what I found on " + location)
    if 'exit' in voice_data:
        alexis_speak("Goodbye for now.")
        exit()


time.sleep(1)
alexis_speak("How can I help you?")
while 1:
    voice_data = record_audio()
    respond(voice_data)
    print(voice_data)
