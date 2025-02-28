# Project: Python Talking Friend
import pyttsx3

def initialize_tts():
    friend = pyttsx3.init()
    return friend

def set_rate(friend):
    rate = friend.getProperty('rate')   # getting details of current speaking rate
    print("Current speaking rate: {rate}")
    new_rate = int(input("Enter new speaking rate (default is 125):") or 125)
    friend.setProperty('rate', new_rate)     # setting up new voice rate

def set_volume(friend):
    volume = friend.getProperty('volume')   # getting to know current volume level
    print("Current volume level: {volume}")
    new_volume = int(input("Enter new volume level (0 to 1, default is 1)") or 1)
    friend.setProperty('volume', new_volume)        # setting up volume level  between 0 and 1

def set_voice(friend):
    voices = friend.getProperty('voices')       # getting details of current voice
    print("Available voices:")
    for index, voice in enumerate(voices):
        print("{index}: {voice.name}")
    voice_index = int(input("Enter voice index (o for male, 1 for female): ") or 0)
    friend.setProperty('voice', voices[voice_index].id)  # changing voice

def speak(friend):
    speech = input("Type something and I will say it: ")
    friend.say(speech)
    friend.runAndWait()

def main_menu():
    friend = initialize_tts()

    while True:
        print("--- Python Talking Friend ---")
        print("1. Set speaking rate")
        print("2. Set volume level")
        print("3. Set Voice")
        print("4. Speak text")
        print("5. Exit")

        choice == input("Choose an option (1-5): ")

        if choice == '1':
            set_rate(friend)
        elif choice == '2':
            set_volume(friend)
        elif choice == '3':
            set_voice(friend)
        elif choice == '4':
            speak(friend)
        elif choice == '5':
            print("Thank you for being my friend. See you again!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()