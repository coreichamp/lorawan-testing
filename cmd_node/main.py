from network import LoRa
import socket
import time
import pycom
import utime
from machine import Pin

# btn_pin = Pin('P16', mode=Pin.IN, pull=Pin.PULL_UP)

pycom.heartbeat(False)
pycom.rgbled(0x000000)
lora = LoRa(mode=LoRa.LORA, frequency=868300000, bandwidth=LoRa.BW_125KHZ, tx_power=14, sf=7)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

def req_data():
	start_time = utime.ticks_us()
	print("start conversation, tick: {}".format(start_time))
	# s.setblocking(True)
	s.send(b"001")
	
	# time.sleep(1)	
	# s.setblocking(True)
	while True:
		time.sleep(1)
		# print("reciving..")
		recv_data = s.recv(128)
		# s.setblocking(False)
		if len(recv_data) > 0:
			stop_time = utime.ticks_us()
			print("stop conversation, tick: {}".format(stop_time))
			print("used time: {}".format(utime.ticks_diff(start_time, stop_time)))
			print(recv_data)		
			break
		# time.sleep(0.01)


def req_data_with_img():
	start_time = utime.ticks_us()
	print("start conversation, tick: {}".format(start_time))
	# s.setblocking(True)
	s.send(b"002")
	
	# time.sleep(1)	
	# s.setblocking(True)
	
	time.sleep(1)
	# print("reciving..")
	while True:
		recv_data = s.recv(255)		
		if recv_data == b'end':
			stop_time = utime.ticks_us()
			print("stop conversation")
			used_time = utime.ticks_diff(start_time, stop_time)
			print("st")
			print("start_time: {}, stop_time: {}, used_time: {}".format(start_time, stop_time, used_time))
			break
		elif len(recv_data) > 0:
			print(recv_data)

		
		
	# s.setblocking(False)
	# if len(recv_data) > 0:
	# 	stop_time = utime.ticks_us()
	# 	print("stop conversation, tick: {}".format(stop_time))
	# 	print("used time: {}".format(utime.ticks_diff(start_time, stop_time)))
	# 	print(recv_data)		
	# 	break
	# # time.sleep(0.01)


req_data_with_img()
# if (btn_pin()):
# 	start_time
# 	s.setblocking(True)
# 	s.send(b'001')
# 	s.setblocking(False)

# print("Start Read File.")
# f = open("img01.txt")
# data = f.read()
# print("File size")
# print(len(data))
# pycom.rgbled(0x000000)

# print("Start Sending.")
# for x in range(0,100):
# 	s.setblocking(True)
# 	print("Window size {}".format(x+200))
# 	s.send(data[0:200+x])
# 	s.setblocking(False)
# 	print("End Sending.")	


