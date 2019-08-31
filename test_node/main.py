from network import LoRa
import socket
import time
import pycom
import champ
from busio import I2C
from board import SCL, SDA
import adafruit_si7021

pycom.heartbeat(False)
pycom.rgbled(0x000000)
lora = LoRa(mode=LoRa.LORA, frequency=868300000, bandwidth=LoRa.BW_125KHZ, tx_power=14, sf=12)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

print("Start Read File.")
f = open("img01.txt")
data = f.read()
print("File size")
print(len(data))
pycom.rgbled(0x000000)

print("Start Sending.")
for x in range(0,100):
	s.setblocking(True)
	print("Window size {}".format(x+200))
	s.send(data[0:200+x])
	s.setblocking(False)
	print("End Sending.")	


