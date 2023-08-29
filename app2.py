import time
import thingspeak1
from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_shims_grove.grove_led import GroveLed

CounterFitConnection.init('127.0.0.1', 5000)
light_sensor = GroveLightSensor(0)
led = GroveLed(5)

def read_comando():
    valor = thingspeak1.thingspeak_receive("field2")
    if valor == 1:
        led.on()
    else:
        led.off()

while True:
    if CounterFitConnection.is_connected:
        luz = light_sensor.light
        thingspeak1.thingspeak_send(luz)
        read_comando()
        time.sleep(15)    
    else:
        print("No esta conectado Counterfit...")
        break

