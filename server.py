import time
import datetime
from flask import Flask, request

app = Flask(__name__)

# Создаем массив, куда будем складывать сообщения
messages = [
    # {'username': 'Nick', 'text': 'Hello', 'time': 0.0}
]

# @app - декоратор, позволяет обернуть функцию в другую функцию, чтобы
# зарегистрировать функцию в качестве HTTP метода, который выставляется на сервере
# обернуть вызов данной функции в другой код бибилиотеки flask
@app.route('/')
def hello():
    '''
        Функция выводит на главной страничке сообщение 'Hello, World'
    :return:
    '''
    return 'Hello, World!'


@app.route('/status')
def status():
    '''
        Функция по адресу /status выводит json статус, Название, текущую дату
    :return:
    '''
    return {
        'status': True,
        'name': 'Messenger',
        'time': datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    }


# Метод для помещения сообщения на сервер (чтобы его могли забрать остальные клиенты, которые подключились на сервер)
@app.route('/send', methods=['POST'])
def send():
    '''
        Функция для отправки сообщений, чтобы можно было послать имя, текст, время отправки
    :return:
    '''
    username = request.json['username']  # Узнаем, кто отправил сообщение
    text = request.json['text']  # Узнаем текст сообщения
    current_time = time.time()
    message = {'username': username, 'text': text, 'time': current_time}
    messages.append(message)

    print(messages)
    return {'ok': True}


# Выводит сообщение от других участников и наши
@app.route('/messages')
def messages_view():
    '''
        Функция реализована для того, чтобы клиенты могли забрать сообщения
    :return:
    '''
    after = float(request.args.get('after'))  # Запросить параметры get запроса
    # Необходимо вернуть спписок всех сообщений, которые есть на сервере
    # необходимо отфильтровать сообщения (вывод сообщения после метки after)
    filtered_messages = []
    for message in messages:
        if message['time'] > after:
            filtered_messages.append(message)

    return {
        'messages': filtered_messages
    }


app.run(debug=True)
