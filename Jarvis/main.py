import pyttsx3
import datetime
import speech_recognition as sr  # installed pyaudio using pipwin

# main logic modules
import pickle
import wikipedia
import webbrowser
import os
import smtplib
import requests
import json

browserPath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"


def speak(speechStr):
    """
    Universal voice of our assistant
    :param speechStr: The string to speak
    :return: None
    """
    engine = pyttsx3.init('sapi5')  # MS Speech API
    voices = engine.getProperty('voices')  # getting all the voices on this system
    # print(voices[0].id)  # gives the path to the installed speech API
    engine.setProperty('voice', voices[1].id)  # setting voice as male voice

    engine.say(speechStr)
    print(speechStr)
    engine.runAndWait()  # necessary for audibility


def wishMe():
    with open("config.pkl", "r") as data:
        dict_data = dict(pickle.load(data))
    str_name = dict_data.get("name")
    """
    Wishes the user on start of the program
    :return:None
    """
    hour = datetime.datetime.now().hour  # getting the current hour
    if 0 <= hour < 12:
        speak(f"Good Morning {str_name}")
    elif 12 <= hour < 18:
        speak(f"Good Afternoon {str_name}")
    else:
        speak(f"Good Evening {str_name}")
    speak("Hoya, I am Jarvista, your personal assistant")


def listenCommand():
    """
    Listens to the mic via Speech_recognition module and converts it to string
    :return:The command string spoken by the user if the recognition is successful otherwise "None"
    """
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Listening...")
        # r.pause_threshold = 1  # gives more pause time to the user in speaking his speech
        audio = r.listen(mic)  # listens to the mic opened by with block
    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language="en-in")  # converts the audio from sr to string via google
        # services
        print(f"You said: {command}\n")  # extra \n for better formatting
    except Exception as e:
        print(e)
        print("Sorry, Pls speak that again")
        return "None"
    return command


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", port=587)
    server.ehlo()
    server.starttls()
    server.login("email", "pwd")
    server.sendmail("satvikmittal638@gmail.com", to, content)
    server.close()


def tellAJoke():
    API_URL = "https://official-joke-api.appspot.com/random_joke"
    joke_json = requests.get(API_URL).text
    parsed_joke = json.loads(joke_json)
    fullJoke = f'{parsed_joke["setup"]}\n{parsed_joke["punchline"]}'
    speak(fullJoke)


def setup():
    name = "user"
    email, password = "", ""
    browserPath = ""

    speak("Hello, I am Jarvista, A Desktop Assistant. By what name should I call you sir ?")
    # taking name
    while 1:
        name = listenCommand()
        if name != "None":
            speak(f"{name}, is that correct ?")
            if "yes" in listenCommand().lower():
                speak(f"Ok great! I will greet you {name} from now !")
                break
            else:
                speak("Sorry, can you repeat your name ?")
                name = listenCommand()

    data = {"name": name, "email": email, "password": password, "browserPath": browserPath}
    saveConfigData(data)


def saveConfigData(data):
    """
    Pickles user info in form of pkl object
    """
    with open("config.pkl", "wb") as f:
        pickle.dump(data, f)


if __name__ == '__main__':
    if not os.path.exists("config.pkl"):
        setup()
    # f = open("config.pkl", "rb")
    # data = pickle.load(f)
    wishMe()
    while 1:
        query = listenCommand().lower()
        # Main execution logic begins here:

        if "wikipedia" in query:
            try:
                speak("Searching wikipedia for results..")
                results = wikipedia.summary(query.replace("wikipedia", ""),
                                            2)  # removes wikipedia word from the query and
                # gives a summarised info in 2 sentences
                speak(f"According to wikipedia {results}")
            except Exception as e:
                print("Sorry an error occurred while searching wikipedia")

        elif "youtube" in query:

            speak("Opening youtube")
            # changing default browser for python
            webbrowser.register("google-chrome",
                                None,
                                webbrowser.BackgroundBrowser(browserPath))
            webbrowser.get('google-chrome').open(
                f"www.youtube.com/results?search_query={query.replace('youtube', '')}")  # TODO-open link with chrome

        elif "play music" in query:
            path = "C:\\Users\\dmitt\\OneDrive\\Desktop\\Projects\\Jarvis\\Musics"
            music_files = os.listdir(path)
            os.startfile(os.path.join(path, music_files[0]))

        elif "time" in query:
            mTime = datetime.datetime.now().strftime("%H:%M")  # format specifier in time
            speak(mTime)  # TODO- Add location with timing

        elif "open browser" in query:
            speak("Opening Browser")
            os.startfile(browserPath)

        elif "send email to" in query:
            try:
                speak("What should I send ? ")
                content = listenCommand()
                # to = contacts[query.replace("send email to", "")]
                sendEmail(to, content)
                speak("Email sent successfully")
            except Exception as e:
                print(e)
                speak("Email cannot be sent")

        elif "quit" in query or "exit" in query:
            speak("Thank you sir for using me")
            exit()

        elif "tell me a joke" in query:
            try:
                speak("Ok sir, give me a moment")
                tellAJoke()
            except Exception as e:
                speak("Sorry, i couldn't get a joke at this moment")

        elif query == "what can you do":
            things = "You can ask me to do various tasks such as:\n" \
                     "Play music\n" \
                     "Open youtube\n" \
                     "Tell a joke\n" \
                     "Send an email\n"
            speak(things)

        elif query is not None:
            speak(f"Showing internet results for {query}")
            webbrowser.get('google-chrome').open(f"https://www.google.com/search?q={query}")
