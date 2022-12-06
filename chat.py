# coding=utf-8
import requests
while True:
    print('##' * 20)
    input_string = input('input:')   
    params = {
        'q': input_string,
    }
    ip = '43.155.173.103'
    response = requests.get(f'http://{ip}:5001/chat', params=params)
    print(response.text)

