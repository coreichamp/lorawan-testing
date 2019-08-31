from network import LoRa
import socket
import time
import pycom
from machine import Pin
import utime
from machine import I2C
from SI7021 import SI7021

#setup 
pycom.heartbeat(False)
pycom.rgbled(0x000000)

pin_motion = Pin('P18', mode=Pin.IN,pull=Pin.PULL_UP)
pin_infrared = Pin('P17', mode=Pin.IN)

echo = Pin('P16', mode=Pin.IN)
trigger = Pin('P20', mode=Pin.OUT)
trigger.value(0)

i2c = I2C(0, I2C.MASTER) 
tempHumidSensor = SI7021(i2c)

lora = LoRa(mode=LoRa.LORA, frequency=868300000, bandwidth=LoRa.BW_125KHZ, tx_power=14, sf=7)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)



def readMotion():
	return pin_motion()

def readInfrared():
	return pin_infrared()

def readUltrasonic():
    trigger.value(0)
    utime.sleep_us(2)
    trigger.value(1)
    utime.sleep_us(10)
    trigger.value(0)
    protectInfinity = utime.ticks_us()+0
    while echo.value() == 0:
		if (utime.ticks_us() - protectInfinity) > 5000:
			break
    start = utime.ticks_us()    
    while echo.value() == 1:
        pass
    finish = utime.ticks_us()
    distance = ((utime.ticks_diff(start, finish) * .034)/2)
    utime.sleep_ms(20)
    return distance

def readTemp():
    return tempHumidSensor.readTemp()

def readHumidity():
    return tempHumidSensor.readRH()


while True:
    time.sleep(1)
    # s.setblocking(True)
    recv_data = s.recv(64)
    # s.setblocking(False)
    if recv_data == b'001':
        print("Start sending sensor value")
        # s.setblocking(True)
        s.send("temp:xx.xx, humid: xx.xx, motion: 0, infrared: 0, ultrasonic: xxx.xx, battery: xxx")
        # s.setblocking(False)
        print("Stop sending sensor value")
    else:
        pass   
    # utime.sleep_ms(1000)
    # print("*******************************************")
    # print("Temp: {}".format(readTemp()))
    # print("Humid: {}".format(readHumidity()))
    # print("Ultrasonic: {}".format(readUltrasonic()))
    # print("Infrared: {}".format(readInfrared()))
    # print("Motion: {}".format(readMotion()))
    # print("*******************************************")