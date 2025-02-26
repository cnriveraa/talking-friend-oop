# Project: Python Talking Friend
import pyttsx3
friend = pyttsx3.init()

"""RATE"""
rate = friend.getProperty('rate')   # getting details of current speaking rate
friend.setProperty('rate', 125)     # setting up new voice rate

"""VOLUME"""
volume = friend.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
friend.setProperty('volume', 1)        # setting up volume level  between 0 and 1

"""VOICE"""
voices = friend.getProperty('voices')       # getting details of current voice
friend.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
#friend.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female

speech = input("Type something and I will say it: ")
friend.say(speech)
friend.runAndWait()