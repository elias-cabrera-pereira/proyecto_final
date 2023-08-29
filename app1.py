import json
import time
from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_shims_grove.grove_led import GroveLed
import paho.mqtt.client as mqtt

id = 'saile_'
client_name = id + 'nightlight_client'
client_telemetry_topic = id + '/telemetry'

mqtt_client = mqtt.Client(client_name)
mqtt_client.connect('test.mosquitto.org')
mqtt_client.loop_start()
print("MQTT connected!")

CounterFitConnection.init('127.0.0.1', 5000)
light_sensor = GroveLightSensor(0)
led = GroveLed(5)

server_command_topic = id + '/commands'

def handle_command(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)
    if payload['led_on']:
        led.on()
    else:
        led.off()

mqtt_client.subscribe(server_command_topic)
mqtt_client.on_message = handle_command

while True:
    if CounterFitConnection.is_connected:
        luz = light_sensor.light
        telemetry = json.dumps({'light' : luz})
        print("Sending telemetry ", telemetry)
        mqtt_client.publish(client_telemetry_topic, telemetry)
    else:
        print("No esta conectado Counterfit...")
        break

    time.sleep(5)