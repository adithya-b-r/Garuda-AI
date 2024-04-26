import datetime
import webbrowser
import os
import time
import cv2
import requests
from bs4 import BeautifulSoup
import pyautogui


class ActionsHandler:
    def get_time(self, assistant):
        now = datetime.datetime.now()
        time_str = now.strftime("%I:%M %p")
        assistant.speak(f"The current time is {time_str}")

    def open_website(self, assistant):
        assistant.speak("Sure, what website would you like me to open?")
        website_query = assistant.listen().replace(" ", "").strip()
        if "college" in website_query:
            website_query = "canaracollege"
        webbrowser.open("https://" + website_query + ".com")

    def play_music(self, assistant):
        music_dir = "C:/Users/DELL/Music"
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, songs[0]))
            assistant.speak("Playing music")
        else:
            assistant.speak("No music found in the specified directory")

    def stop_music(self, assistant):
        try:
            os.system("taskkill /f /im Microsoft.Media.Player.exe")
            assistant.speak("Music stopped")
        except Exception as e:
            assistant.speak(f"Error in stopping music: {str(e)}")

    def search_web(self, query, assistant):
        search_query = query.replace(
            "garuda", "").replace("search for", "").strip()
        search_url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(search_url)

    def open_application(self, assistant):
        assistant.speak("Which application would you like me to open?")
        app_query = assistant.listen()
        os.startfile(app_query)

    def get_weather(self, assistant):
        assistant.speak(
            "Sure, for which city would you like to know the weather?")
        city_query = assistant.listen()
        if "current" in city_query:
            city_query = "Mangalore"
        weather_url = f"https://www.google.com/search?q=weather+in+{city_query}"
        response = requests.get(weather_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            temperature = soup.find(
                "div", class_="BNeawe iBp4i AP7Wnd").get_text()
            assistant.speak(f"The current temperature in {city_query} is {temperature}")
        else:
            assistant.speak(
                f"Sorry, I couldn't retrieve the weather information for {city_query}")

    def open_camera(self, assistant):
        assistant.speak("Opening camera")
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            cv2.imshow('webcam', img)
            k = cv2.waitKey(50)
            if k == 3:
                break
        cap.release()
        cv2.destroyAllWindows()

    def screen_size(self, assistant):
        width, height = pyautogui.size()
        assistant.speak(f"Your screen width is {width} and height {height}")

    def open_paint(self, assistant):
        assistant.speak("Opening Paint.")
        pyautogui.hotkey('win', 'r')
        time.sleep(0.5)

        pyautogui.write('mspaint')
        pyautogui.press('enter')
    def close_paint(self, assistant):
        try:
            os.system("taskkill /f /im mspaint.exe")
            assistant.speak("Closing paint")
        except Exception as e:
            assistant.speak(f"Error in closing paint: {str(e)}")