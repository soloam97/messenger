import requests


def send_message(username, text):
    '''
        Функия реализует отправку сообщения
    :param username: имя пользователя
    :param text: текст пользователя
    :return:
    '''
    message = {'username': username, 'text': text}  # Параметры сообщения
    response = requests.post('http://127.0.0.1:5000/send', json=message)
    return response.status_code == 200


username = input('Введите имя: ')

while True:
    text = input('Введите сообщение: ')
    result = send_message(username, text)
    if result is False:
        print('Error')
