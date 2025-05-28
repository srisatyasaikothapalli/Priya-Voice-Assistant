import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit as pk
import wikipedia as wiki
import os
import pyjokes
import webbrowser
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText

listener = sr.Recognizer()
engine = pyttsx3.init()
name = 'priya'
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# GUI Setup
app = ttk.Window(themename="cyborg")
app.title("🧠 Priya - Your Smart Assistant")
app.geometry("650x550")

# GUI Widgets
ttk.Label(app, text="🤖", font=("Helvetica", 40)).pack(pady=(10, 0))
ttk.Label(app, text="Priya Voice Assistant", font=("Helvetica", 22, "bold"), bootstyle="info").pack()
status_label = ttk.Label(app, text="Status: Idle", font=("Helvetica", 10), bootstyle="secondary")
status_label.pack(pady=5)

chat_output = ScrolledText(app, height=20, font=("Consolas", 12), autohide=True, wrap='word')
chat_output.pack(padx=15, pady=10, fill=BOTH, expand=True)

def talk(text):
    chat_output.insert('end', f"Priya: {text}\n")
    chat_output.see('end')
    status_label.config(text="Status: Speaking...")
    app.update()
    engine.say(text)
    engine.runAndWait()
    status_label.config(text="Status: Idle")

def take_command():
    try:
        with sr.Microphone() as source:
            status_label.config(text="Status: Listening...")
            app.update()
            voice = listener.listen(source, timeout=5, phrase_time_limit=5)
            status_label.config(text="Status: Processing...")
            command = listener.recognize_google(voice).lower()
            if name in command:
                command = command.replace(name + ' ', '')
                chat_output.insert('end', f"You: {command}\n")
                chat_output.see('end')
                return command
    except Exception as e:
        # Optionally print(e) for debugging
        pass
    return ''

def process_command(command):
    if not command:
        return

    if 'hello' in command:
        talk("Hi! How can I help you?")
    elif 'how are you' in command:
        talk("I am fine. What about you?")
    elif 'fine' in command:
        talk("Okay, how can I help you?")
    elif 'time' in command:
        talk("The time is " + datetime.datetime.now().strftime('%I:%M %p'))
    elif 'date' in command:
        talk("Today's date is " + datetime.datetime.now().strftime('%B %d, %Y'))
    elif 'play' in command:
        song = command.replace('play', '').strip()
        talk(f"Playing {song}")
        pk.playonyt(song)
    elif 'youtube' in command:
        talk("Opening YouTube.")
        webbrowser.open('https://www.youtube.com')
    elif 'search' in command or 'open' in command:
        term = command.replace('search', '').replace('open', '').strip()
        talk(f"Searching {term}")
        pk.search(term)
    elif 'who is' in command or 'what is' in command:
        person = command.replace('who is', '').replace('what is', '').strip()
        try:
            info = wiki.summary(person, sentences=2)
            talk(info)
        except:
            talk("Sorry, I couldn't find that.")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'sing a song' in command:
        lyrics = [
            "Twinkle, twinkle, little star,",
            "How I wonder what you are!",
            "Up above the world so high,",
            "Like a diamond in the sky."
        ]
        talk("Okay boss, here's a song!")
        for line in lyrics:
            talk(line)
    elif 'shutdown' in command or 'shut down' in command:
        talk("Shutting down the system. Goodbye!")
        os.system("shutdown /s /t 1")
    elif 'restart' in command:
        talk("Restarting now.")
        os.system("shutdown /r /t 1")
    elif 'stop' in command or 'exit' in command or 'bye' in command:
        talk("Okay, goodbye!")
        app.destroy()
    else:
        talk("Sorry, I don't know that yet.")

# Control flags
listening = True

def toggle_listening():
    global listening
    listening = not listening
    if listening:
        status_label.config(text="Status: Resumed Listening")
        listen_button.config(text="⏸️ Pause Listening", bootstyle="warning")
    else:
        status_label.config(text="Status: Paused")
        listen_button.config(text="▶️ Start Listening", bootstyle="success")

def exit_app():
    talk("Okay, shutting down. Bye!")
    app.destroy()

def listen_loop():
    if listening:
        command = take_command()
        process_command(command)
    app.after(1000, listen_loop)

# Control Buttons
button_frame = ttk.Frame(app)
button_frame.pack(pady=10)

listen_button = ttk.Button(button_frame, text="⏸️ Pause Listening", bootstyle="warning", command=toggle_listening)
listen_button.pack(side=LEFT, padx=10)

exit_button = ttk.Button(button_frame, text="❌ Close App", bootstyle="danger", command=exit_app)
exit_button.pack(side=LEFT, padx=10)

# Initial Greeting
talk("Hi! I am your assistant " + name + ", tell me boss.")

# Start listening loop
app.after(1000, listen_loop)

app.mainloop()
