import urllib.request
import threading
import requests

def thingspeak_send(valor):
    valor1 = valor
    if valor < 300:
        valor2 = 1
    else:
        valor2 = 0
    upload_thingspeak(valor1, valor2)

def upload_thingspeak(valor1, valor2):
    url = 'https://api.thingspeak.com/update?api_key='
    key = 'R8XEHQMC7RS54H86'
    header = '&field1={}&field2={}'.format(valor1, valor2)
    new_url = url + key + header
    print(f"url: {new_url}")
    data = urllib.request.urlopen(new_url)

def thingspeak_receive(field):
    channelid = '2244862'
    key = '4WSBEBXLNM7JDQAK'
    ultimos = 1
    url = f'https://api.thingspeak.com/channels/{channelid}/feeds.json?api_key={key}&results={ultimos}'
    print(f"url recepcion: {url}")
    data = requests.get(url).json()
    channel = data['channel']['id']
    descripcion = data['channel']['description']
    valor = data['feeds'][0][field]
    return int(valor)


