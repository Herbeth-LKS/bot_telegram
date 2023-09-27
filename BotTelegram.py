import csv
import json
import requests
from sty import fg, bg, ef, rs
from time import sleep
from datetime import datetime
import telegram

api_key = 'you api key'
user_id = 'id do grupo ou contato de destino da msg'
bot = telegram.Bot(token=api_key)


def count(time, win: int, loss: int):
    with open('count.csv', 'a+') as file:
        writer = csv.writer(file)
        writer.writerow([f'{time}', win, f'{loss}\n'])

    # desktop notification settings


#def desktop_notification(message):
    #notification = Notify()
    #notification.message = message
    #notification.icon = '/blaze-icon.png'
    #notification.send()


# phone notifications
# API_KEY = 'o.9mKgLukDRUkGzzaWN9DIC0aqy3ixNHKj'
# pb = Pushbullet(API_KEY)

def request():
    req = requests.get('https://blaze.com/api/roulette_games/recent')
    output = json.loads(req.text)
    list_past_results = [{'cor': row['color'], 'numero': row['roll']} for row in output[:4]]
    return list_past_results


def main_request():
    while True:

        list_past_results = request()
        if list_past_results[0]['cor'] == list_past_results[1]['cor']: #and list_past_results[1]['cor'] == list_past_results[2]['cor'] and list_past_results[2]['cor'] == list_past_results[3]['cor']:

            return apostar(list_past_results)

        #Dprint(fg.li_yellow + 'request feito' + fg.rs, datetime.now())
        sleep(10)


def apostar(lista):
    if lista[0]['cor'] == 2:
        bot.send_message(chat_id=user_id, text='entrar vermelho e branco🔴️ + ⚪')

    if lista[0]['cor'] == 1:
        bot.send_message(chat_id=user_id, text='entrar preto e branco⚫ + ⚪')

    sleep(26)
    checagem()


def checagem():
    win = 0
    loss = 0

    list = request()
    if list[0]['cor'] != list[1]['cor']:
        bot.send_message(chat_id=user_id, text='WINN✅✅')
        win += 1
        print(fg.green + 'WIINN✅✅' + fg.rs)
    elif list[0]['cor'] == 1:
            
            bot.send_message(chat_id=user_id, text='Vamos para a primeira gale P.')
            
            sleep(28)

            list = request()
            if list[0]['cor'] != list[1]['cor']:
                #desktop_notification('WIIINNNN')
                win += 1
                bot.send_message(chat_id=user_id, text='WINN✅✅')
                print(fg.green + 'WIINN✅✅' + fg.rs)

            else:
                #desktop_notification('Loss')
                loss += 1

                bot.send_message(chat_id=user_id, text='LOSS❌')
                print(fg.red + 'LOSS❌' + fg.rs)

    
    elif list[0]['cor'] == 2:
        bot.send_message(chat_id=user_id, text='Vamos para a primeira gale V.')
        #desktop_notification('Vamos para a primeira gale. )
        #print('Primeira gale')
        sleep(28)
        list = request()
        if list[0]['cor'] != list[1]['cor']:
            #desktop_notification('WIIINNNN')
            win += 1
            bot.send_message(chat_id=user_id, text='WINN✅✅')
            print(fg.green + 'WIINN✅✅' + fg.rs)

        else:
            #desktop_notification('Loss')
            loss += 1

            bot.send_message(chat_id=user_id, text='LOSS❌')
            print(fg.red + 'LOSS❌' + fg.rs)

    if list[0]['cor'] == 0:

        print(fg.green + 'WINN NO BRANCO 14X ✅' + fg.rs)

        bot.send_message(chat_id=user_id, text='⚪⚪⚪WINN NO BRANCO 14X ✅✅✅✅')

    
  


    time = datetime.now()
    count(time, win, loss)

    sleep(36)
    main_request()


main_request()

# Cor 2 = Preto | Cor 1 = Vermelho | Cor 0 - Branco
