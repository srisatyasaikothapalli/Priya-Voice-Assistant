# 🧠 Priya - Your Smart Voice Assistant

Priya is a Python-based voice assistant with a sleek GUI built using `ttkbootstrap`. It can answer questions, tell the time/date, play YouTube videos, search the web, tell jokes, sing songs, and even shut down or restart your system — all via voice commands!

## ✨ Features

- 🎙 Voice recognition with `speech_recognition`
- 🔊 Text-to-speech with `pyttsx3`
- 🎵 YouTube playback using `pywhatkit`
- 📚 Wikipedia info fetching
- 😂 Jokes with `pyjokes`
- 🌐 Web search and site opening
- 🕒 Date and time reporting
- 💻 System control (shutdown/restart)
- 💬 Simple and intuitive GUI using `ttkbootstrap`

## 🚀 Getting Started

### Prerequisites

Install the following Python libraries:

```bash
pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes ttkbootstrap
````

On some systems, you may also need:

```bash
pip install pyaudio
```

> If `pyaudio` gives installation errors, follow platform-specific steps to install it. On Windows, try:
>
> ```
> pip install pipwin
> pipwin install pyaudio
> ```

### Running the App

1. Clone the repository:

```bash
git clone https://github.com/yourusername/priya-assistant.git
cd priya-assistant
```

2. Run the Python file:

```bash
python main.py
```

## 🗣 Sample Voice Commands

* "Priya hello"
* "Priya what is the time"
* "Priya play \[song name]"
* "Priya who is \[person]"
* "Priya tell me a joke"
* "Priya search Python programming"
* "Priya shut down" or "Priya restart"
* "Priya sing a song"
* "Priya stop"

## 📁 Project Structure

```
priya-assistant/
│
├── main.py               # Main app file
├── assets/               # Icons, audio, images (if any)
├── README.md             # This file
└── requirements.txt      # (Optional) List of dependencies
```

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**K. Sri Satya Sai**
Feel free to fork, contribute, and suggest improvements!

