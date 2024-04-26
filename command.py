from actions import ActionsHandler as AcH

class Actions:
    def __init__(self):
        self.actions_functions = AcH()

    def perform_action(self, query, assistant):
        if "hello" in query:
            assistant.speak("Hi there! How can I assist you?")
        elif "time" in query:
            self.actions_functions.get_time(assistant)
        elif "open website" in query:
            self.actions_functions.open_website(assistant)
        elif "play music" in query:
            self.actions_functions.play_music(assistant)
        elif "stop music" in query:
            self.actions_functions.stop_music(assistant)
        elif "search for" in query:
            self.actions_functions.search_web(query, assistant)
        elif "open" in query and "application" in query:
            self.actions_functions.open_application(assistant)
        elif "weather" in query:
            self.actions_functions.get_weather(assistant)
        elif "bye" in query or "exit" in query:
            assistant.speak("Goodbye!, have a good day")
            exit()
        elif "open camera" in query:
            self.actions_functions.open_camera(assistant)
        elif "screen size" in query:
            self.actions_functions.screen_size(assistant)
        elif "open paint" in query:
            self.actions_functions.open_paint(assistant)
        elif "close paint" in query:
            self.actions_functions.close_paint(assistant)
        else:
            if "garuda" in query and len(query) < 8:
                assistant.speak("Yes sir, I can hear you.")
            else:  
                assistant.speak("I'm sorry, I didn't understand that. Can you please repeat?")