import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys

# ── TTS Engine setup (cross-platform) ─────────────────────────────────────
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)

# ── CONFIG — update these to your own values ──────────────────────────────
MUSIC_DIR = os.path.join(os.path.expanduser("~"), "Music")  # default Music folder
VSCODE_PATH = ""  # leave empty to auto-detect, or set full path manually

def speak(audio):
    print(f"Jarvis: {audio}")
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. Please tell me how may I help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            return "None"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except sr.UnknownValueError:
        print("Say that again please...")
        return "None"
    except sr.RequestError:
        print("Network error. Check your internet connection.")
        return "None"
    return query

def openVSCode():
    """Open VS Code cross-platform."""
    if VSCODE_PATH and os.path.exists(VSCODE_PATH):
        os.startfile(VSCODE_PATH)
        return

    # Auto-detect by OS
    if sys.platform == "win32":
        paths = [
            os.path.join(os.environ.get("LOCALAPPDATA", ""), "Programs", "Microsoft VS Code", "Code.exe"),
            "C:\\Program Files\\Microsoft VS Code\\Code.exe"
        ]
        for p in paths:
            if os.path.exists(p):
                os.startfile(p)
                return
        speak("Could not find VS Code. Please set the path in the config.")
    else:
        os.system("code .")  # works on Mac/Linux if VS Code is in PATH

def playMusic():
    """Play first song from Music folder."""
    if not os.path.exists(MUSIC_DIR):
        speak("Music folder not found. Please update the MUSIC_DIR in the config.")
        return
    songs = [f for f in os.listdir(MUSIC_DIR) if f.endswith(('.mp3', '.wav', '.m4a'))]
    if not songs:
        speak("No music files found in the Music folder.")
        return
    if sys.platform == "win32":
        os.startfile(os.path.join(MUSIC_DIR, songs[0]))
    elif sys.platform == "darwin":
        os.system(f"open '{os.path.join(MUSIC_DIR, songs[0])}'")
    else:
        os.system(f"xdg-open '{os.path.join(MUSIC_DIR, songs[0])}'")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if query == "none":
            continue

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "").strip()
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception:
                speak("Sorry, I couldn't find anything on Wikipedia for that.")

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")

        elif 'play music' in query:
            playMusic()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            openVSCode()

        elif 'stop' in query or 'exit' in query or 'quit' in query:
            speak("Goodbye!")
            break

        else:
            speak("Sorry, I didn't understand that. Please try again.")
