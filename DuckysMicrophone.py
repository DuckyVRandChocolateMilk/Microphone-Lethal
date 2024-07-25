import speech_recognition as sr
import pyttsx3
import time
from threading import Thread
import keyboard


# Initialize the recognizer 
r = sr.Recognizer() 

def SpeakText(command):
    if "e" in command:
        engine = pyttsx3.init()
        engine.setProperty('rate', 120)
        engine.say("You said E")
        engine.runAndWait()
        keyboard.press_and_release("3")


while True:  # making a loop
            try:
                # use the microphone as source for input.
                with sr.Microphone() as source2:
                    # wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level 
                    r.adjust_for_ambient_noise(source2, duration=0.2)
                    #listens for the user's input 
                    audio2 = r.listen(source2)
                    # Using google to recognize audio
                    print("Changing Audio to Text")
                    MyText = r.recognize_google(audio2)
                    MyText = MyText.lower()
                    print("User: " + MyText)
                    SpeakText(MyText)
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
            except sr.UnknownValueError:
                print("unknown error occurred")