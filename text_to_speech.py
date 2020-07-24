# dapat membuat chatbot with voide assistant pada OS Linux, dan MacOS
# hambatan pada os
# link: https://github.com/ashus3868/RasaCustomerService
import os

from gtts import gTTS

mytext = 'Halo'

language = 'en'

myobj = gTTS(text=mytext, lang=language)
myobj.save("welcome.mp3")
os.system("welcome.mp3")