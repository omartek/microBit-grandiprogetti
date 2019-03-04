import paho.mqtt.client as mqtt #import the client1
import random

broker_address="192.168.1.119" 
#broker_address="iot.eclipse.org" #use external broker

client = mqtt.Client("P1") #create new instance
client.connect(broker_address) #connect to broker

num = 0

for i in range(10):
    num = random.randint(0,10)
    client.publish("home.luci",str(num))#publish
