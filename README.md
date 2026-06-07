# 🐍 Python Mini Projects

A collection of fun Python mini projects — a love calculator GUI and a voice assistant.

---

## 📁 Projects

### 1. 💕 Love Calculator
A fun Tkinter GUI app that calculates a "love percentage" between two names. Same name pair always gives the same result!

**Features:**
- Clean GUI with input fields for two names
- Consistent results — same names always give the same percentage
- Fun compatibility messages based on the score
- Input validation — won't calculate with empty names

**Run:**
```bash
python love_calculator.py
```

**Requirements:** Only Python's built-in `tkinter` — no install needed.

---

### 2. 🎙️ Voice Assistant (Jarvis)
A voice-controlled assistant that responds to spoken commands using your microphone.

**Features:**
- Greets you based on the time of day
- Search Wikipedia by voice
- Open YouTube, Google, or Stack Overflow
- Tell you the current time
- Open VS Code
- Play music from your Music folder
- Say "stop", "exit", or "quit" to end the session
- Cross-platform — works on Windows, macOS, and Linux

**Run:**
```bash
python voice_assistant.py
```

**Setup — update these in `voice_assistant.py` if needed:**
```python
MUSIC_DIR = ""    # path to your music folder (defaults to ~/Music)
VSCODE_PATH = ""  # path to VS Code exe (auto-detected on Windows)
```

---

## ⚙️ Requirements

Install dependencies for the voice assistant:

```bash
pip install -r requirements.txt
```

> **Note on PyAudio (microphone support):**
> - **Windows:** `pip install pyaudio`
> - **Mac:** `brew install portaudio && pip install pyaudio`
> - **Linux:** `sudo apt-get install python3-pyaudio`

> **tkinter** is built into Python — no install needed.

---

## 🚀 How to Run

Clone the repository:

```bash
git clone https://github.com/Anjalee-29/random-small-projects.git
cd random-small-projects
pip install -r requirements.txt
```

Run either project:
```bash
python love_calculator.py     # Love Calculator GUI
python voice_assistant.py     # Voice Assistant
```

---

## 📁 Project Structure

```
├── love_calculator.py     # Love Calculator GUI app
├── voice_assistant.py     # Voice assistant (Jarvis)
├── requirements.txt       # Dependencies for voice assistant
└── README.md
```

---

## 📝 Notes

- `love_calculator.py` requires no external libraries
- `voice_assistant.py` requires a working microphone and internet connection for speech recognition and Wikipedia search
- The email feature from the original has been removed as Gmail no longer supports plain-password SMTP login
