import speech_recognition as sr
import pyttsx3
from command import Actions

class Assistant:
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voices', self.voices[1].id)
        self.engine.setProperty('rate', 190)
        self.actions = Actions()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            recognizer.pause_threshold = 0.6
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"You said: {query}")
            return query.lower()
        except Exception as e:
            print(e)
            return ""

    def run(self):
        self.speak("Hello! I'm Garuda, your AI assistant. How can I help you today?")

        while True:
            query = self.listen()

            if "garuda" in query:
                self.actions.perform_action(query, self)

if __name__ == "__main__":
    assistant = Assistant()
    assistant.run()