#!/usr/bin/env python3

import random
import os
import requests

def get_random_curiosity():
    url = "https://raw.githubusercontent.com/xelagorilla/telegramdogcuriosity/c77955b19fb1e30dedb5cd485f1d519c5fe5a095/lista"

    response = requests.get(url)
    curiosities = response.text.splitlines()
    random_curiosity = random.choice(curiosities)
    return random_curiosity

def send_curiosity_to_telegram():
    chat_id = "@doggposting"  # Sostituisci con il nome del tuo canale su Telegram
    bot_token = "6080666668:AAEnAScnUzcGoFnftYz50V1hDzegr18IZ60"  # Sostituisci con il token del tuo bot su Telegram
    curiosity = get_random_curiosity()
    message = "La curiosità sui cani di oggi è:\n" + curiosity
    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    response = requests.post(telegram_url, json=payload)
    if response.status_code == 200:
        print("Curiosità inviata con successo su Telegram!")
    else:
        print("Si è verificato un errore durante l'invio della curiosità su Telegram.")

if __name__ == '__main__':
    send_curiosity_to_telegram()
