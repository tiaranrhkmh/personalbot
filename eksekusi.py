# rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
# jika menggunakan rasa shell tidak akan merespon untuk perintah open note,open camera,knowledge
# sudah terintegrasi dengan rasa chatbot
import requests

sender = input("HALO SAYA INDITA YANG SELALU SIAP MELAYANI ANDA")

bot_message = ""
while bot_message != "Bye":
    message = input("\nMe:")
    print("......")

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"sender": sender, "message":message})

    print("\nIndita:", end='')
    for i in r.json():
        bot_message = i['text']
        print(f"{ bot_message }")


