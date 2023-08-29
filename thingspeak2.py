import urllib.request
import requests

def thingspeak_send(luz,temperatura):
    if luz > 300:
        luz_comando = 1
    else:
        luz_comando = 0
    if temperatura > 40:
        temperatura_comando=1
    else:
        temperatura_comando=0
    upload_thingspeak(luz,luz_comando,temperatura,temperatura_comando)

def upload_thingspeak(luz,luz_comando,temperatura,temperatura_comando):
    url = 'https://api.thingspeak.com/update?api_key='
    key = 'R8XEHQMC7RS54H86'
    header = '&field1={}&field2={}&field3={}&field4={}'.format(luz,temperatura,luz_comando,temperatura_comando)
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


