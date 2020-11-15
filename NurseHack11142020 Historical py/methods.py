# Simple logic on how things work


# Text to speech portion of code, using Microsoft Zira/Alex
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# engine.say("Hi, please be patient, your nurse is on their way")
engine.runAndWait()


# SMTP method to send an email (Markdown to make typing easier)
#* <- are really the 2 symbols you'd need to learn
import mdmail

FormSender = "Yuchen <wang.yuchen@dhs.sg>"

sender = "Yuchen Wang <ywang@connexall.com>"
receiver = FormSender

subject = "Notes 401B 14Nov2020"

message = """

# This is a sample email

- that is written in markdown
- and can be made/used fairly easily

Note that you want input in between...

1. This is an mvp
2. This does not need to be difficult
3. This just needs to work...


_that_ **is** all.
"""

smtp = {
  'host': 'smtp.mailtrap.io',
  'port': 2525,
  'tls': False,
  'ssl': False,
  'user': '865682b2d753ed',
  'password': '',
}

mdmail.send(message, subject=subject, from_email=sender, to_email=receiver, smtp=smtp)


# Speech to text
#Note that even if it's not imported, you need pyaudio & sphinx
#They both require C++ build tools on windows https://visualstudio.microsoft.com/downloads/
#pip install pyaudio 
#python -m pip install --upgrade pip setuptools wheel
#pip install --upgrade pocketsphinx

import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

print(r.recognize_sphinx(audio))