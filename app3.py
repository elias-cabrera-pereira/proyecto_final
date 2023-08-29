import time
import thingspeak2
from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_shims_grove.grove_relay import GroveRelay

CounterFitConnection.init('127.0.0.1', 5000)
luz_sensor = GroveLightSensor(0)
toldo_relay=GroveRelay(5)
bomba_relay=GroveRelay(6)


def read_comando():
    luz_comando = thingspeak2.thingspeak_receive("field3")
    temperatura_comando = thingspeak2.thingspeak_receive("field4")
    if luz_comando == 1:
        toldo_relay.on()
    else:
        toldo_relay.off()
    if temperatura_comando>1:
        bomba_relay.on()
    else:
        bomba_relay.off()

while True:
    if CounterFitConnection.is_connected:
        modo_boton=CounterFitConnection.get_sensor_boolean_value(2)
        if(modo_boton==False):
            luz = luz_sensor.light
            temperatura=CounterFitConnection.get_sensor_int_value(1)
            thingspeak2.thingspeak_send(luz,temperatura)
            read_comando()
            time.sleep(15)    
        else:
            toldo_boton=CounterFitConnection.get_sensor_boolean_value(3)
            bomba_boton=CounterFitConnection.get_sensor_boolean_value(4)
            if(toldo_boton==True):
                toldo_boton=1
            else:
                toldo_boton=0
            if(bomba_boton==True):
                bomba_boton=1
            else:
                bomba_boton=0
            luz= luz_sensor.light
            temperatura=CounterFitConnection.get_sensor_int_value(1)
            thingspeak2.upload_thingspeak(luz,toldo_boton,temperatura,bomba_boton)
            read_comando()
            time.sleep(15)  

    else:
        print("No esta conectado Counterfit...")
        break

