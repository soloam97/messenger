import time
from datetime import datetime

import requests

after = 0


def get_messages(after):
    '''
    Производит GET запрос на /messages
    Содержимое, которое она получит, - распарсит в виде json
    :return:
    '''
    response = requests.get('http://127.0.0.1:5000/messages',
                            params={'after': after}
                            )
    data = response.json()  # Тело ответа в виде питоновского словаря
    return data['messages']  # Ключ messages хранит список сообщений


def print_messages(message):
    '''
        Функция выводит одно конкретное сообщение
    :return:
    '''
    username = message['username']
    message_time = message['time']
    text = message['text']

    dt = datetime.fromtimestamp(message_time)
    dt_format = dt.strftime('%H:%M:%S')

    print(dt_format, username)
    print(text)
    print()

while True:
    messages = get_messages(after)
    print(messages)
    # Создаем отфильтрованное сообщение: значение по ключу time >  after
    for message in messages:
        print_messages(message)
        if message['time'] > after:
            after = message['time']

    time.sleep(1)

# Введем параметр гет запроса, в котором будем указывать время запроса, чтобы выводить только новые сообщения
