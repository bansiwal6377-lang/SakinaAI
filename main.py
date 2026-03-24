import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print("Sakina AI:", text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("Sun rahi hu...")
            audio = r.listen(source)

            text = r.recognize_google(audio)
            print("Tum:", text)

            if "hi" in text.lower():
                speak("Hello 😊 main Sakina AI hu")

            elif "kya haal" in text.lower():
                speak("Main badhiya hu, aap batao")

            elif "naam" in text.lower():
                speak("Mera naam Sakina AI hai")

            elif "exit" in text.lower():
                speak("Bye bye 👋")
                break

            else:
                speak("Samajh nahi aaya")

    except:
        print("Error...")