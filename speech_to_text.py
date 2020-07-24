# dapat membuat chatbot with voide assistant pada OS Linux, dan MacOS
# hambatan pada os
# link: https://github.com/ashus3868/RasaCustomerService
import subprocess

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Katakan Sesuatu:")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    print("Kamu bilang: {}".format(text))
except:
    print("Maaf ngga jelas")

subprocess.call(['mpyg321', "welcome.mp3", '--'])
