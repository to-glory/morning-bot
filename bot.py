import requests
from time import sleep
import datetime
import schedule
import time


url = "https://api.telegram.org/bot462632843:AAHvKhUuEhsEkONvokBSEtaiEXKu14E9uVQ/"
now = datetime.datetime.now()

def get_updates_json(request):  
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()


def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response
def goodMorning():
    send_mess(get_chat_id(last_update(get_updates_json(url))), 'Good morning, my dear Katya')

def goodNight():
    send_mess(get_chat_id(last_update(get_updates_json(url))), 'Gute Nacht, lieber Katya')

def main():  
    new_offset = None
    today = now.day
    hour = now.hour
    minutes = now.minute
    update_id = last_update(get_updates_json(url))['update_id']
    last_chat_text = last_update(get_updates_json(url))['message']['text']
    schedule.every().day.at("08:30").do(goodMorning)
    schedule.every().day.at("00:00").do(goodNight)
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           send_mess(get_chat_id(last_update(get_updates_json(url))), 'Hello from Andrew!')
           update_id += 1
        schedule.run_pending()
    sleep(1)

if __name__ == '__main__':  
    main()
