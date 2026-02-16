import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import os
import subprocess

# Initialize recognizer and speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif "open gemini" in c:
        webbrowser.open("https://gemini.google.com")
    elif c.startswith("play"):
        song = c.split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak_old("Sorry, I couldn't find that song.")
    elif "open notepad" in c:
        subprocess.Popen(["notepad.exe"])
    elif "open camera" in c:
        os.system("start microsoft.windows.camera:")
    elif "open calculator" in c:
        subprocess.Popen(["calc.exe"])
    elif "open paint" in c:
        subprocess.Popen(["mspaint.exe"])
    elif "open command prompt" in c or "open cmd" in c:
        subprocess.Popen(["cmd.exe"])
    else:
        speak_old("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak_old("Initializing Marcus...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
                word = recognizer.recognize_google(audio)
                print(f"Heard: {word}")

                if word.lower() == "marcus":
                    speak_old("Yes")
                    print("Marcus is active...")

                    with sr.Microphone() as source:
                        print("Listening for command...")
                        recognizer.adjust_for_ambient_noise(source, duration=1)
                        audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
                        command = recognizer.recognize_google(audio)
                        print(f"Command: {command}")
                        processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")