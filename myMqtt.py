import paho.mqtt.client as mqtt
import time
import threading

broker_url = "10.20.44.169"
broker_port = 1883
class clMQTT():
    #def __init__(self, parent=None):

    def on_connect(client, userdata, flags, rc):
       print("Connected With Result Code " (rc))

    def on_message_from_kitchen(client, userdata, message):
       print("Message Recieved from Kitchen: "+message.payload.decode())

    def on_message_from_bedroom(client, userdata, message):
       print("Message Recieved from Bedroom: "+message.payload.decode())

    def on_message(client, userdata, message):
       print("Message Recieved from Others: "+message.payload.decode())

    def myMqttInit(self):
       self.client = mqtt.Client()
       self.client.on_connect = on_connect
       #To Process Every Other Message
       client.on_message = on_message
       client.connect(broker_url, broker_port)
       while(True):
          client.loop_start()
          client.subscribe("QMS/Display", qos=1)
          client.subscribe("QMS/Keypad", qos=1)
          client.message_callback_add("QMS/Display", on_message_from_kitchen)
          client.message_callback_add("QMS/Keypad", on_message_from_bedroom)
          time.sleep(4) # wait
          client.loop_stop()
#client.loop_forever()

d = threading.Thread(name='myMqttInit', target=myMqttInit)
d.start()


