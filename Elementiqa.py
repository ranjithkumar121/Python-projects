# importing libraries
import mendeleev
import speech_recognition as sr
import pyttsx3
import pyaudio
import random
from playsound import playsound

# initializing
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
name = []
for i in range(1, 119):
    a = mendeleev.element(i)
    name.append(a.name.lower())


# input
def take_command():
    try:
        with sr.Microphone() as source:
            listener.pause_threshold = 0.8
            listener.energy_threshold = 300
            listener.adjust_for_ambient_noise(source, duration=1)
            print("say")
            voice = listener.listen(source, timeout=5, phrase_time_limit=5)
            command = listener.recognize_google(voice, language='en-In')
            command = command.lower()
            return command
    except:
        talk("cant hear you, say again")
        return take_command()


# output
def talk(text):
    rate = 130
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()


# learning
def learning():
    talk("What Element you want to know ?")
    s = take_command()
    if s in name:
        n = name.index(s) + 1
        el = mendeleev.element(n)
        talk("Symbol " + str(el.symbol))
        talk("atomic number " + str(el.atomic_number))
        talk("atomic weight " + str(el.atomic_weight))
        talk("Block " + str(el.block))
        talk("cas " + str(el.cas))
        talk("electrons " + str(el.electrons))
        talk("electronic configuration " + str(el.ec))
        talk("neutrons " + str(el.neutrons))
        talk("period " + str(el.period))
        talk("protons " + str(el.protons))
        talk("series " + str(el.series))
    else:
        talk("Give a valid Element Name please")
        return learning()


# Quiz
def quiz():
    q = random.choice(name)
    index = name.index(q) + 1
    el = mendeleev.element(index)
    talk(q)
    talk("symbol of " + q)
    symbol = take_command()
    if symbol == el.symbol.lower():
        talk("correct answer")
    else:
        talk("wrong answer, the correct answer is " + el.symbol)
    talk("atomic number of " + q)
    an = take_command()
    if an == str(el.atomic_number):
        talk("correct answer")
    else:
        talk("wrong answer, the correct answer is " + str(el.atomic_number))
    talk("Mass number of " + q)
    mn = take_command()
    if mn == str(round(el.atomic_weight)):
        talk("correct answer")
    else:
        talk("wrong answer, the correct answer is " + str(round(el.atomic_weight)))


# periodic table
def periodictable():
    playsound("music.mp3")


# main function
talk("Elementiqua is On")
while (True):
    talk("Hello Genius what do you want ?")
    command = take_command()
    if "properties" in command or "know" in command:
        learning()
    elif "quiz" in command or "take" in command:
        quiz()
    elif "periodic" in command or "table" in command:
        periodictable()
    elif "sleep" in command:
        talk("thank you for useing me, bye")
        break
    else:
        talk(
            "You can know any properties of an element or you can attend quiz or you can know the periodic table elements")
        print(command)



