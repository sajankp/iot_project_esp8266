# import uwebsockets.client
import urequests
import ujson, time, machine, dht

def main():
	uri = 'http://35.244.13.244/post'
	# uri = 'http://192.168.225.201:8000/post'
	# uri = 'ws://echo.websocket.org/' #for websocket testing
	# websocket = uwebsockets.client.connect(uri) #for websocket use
	led = machine.Pin(16, machine.Pin.OUT)
	print("Connecting to {}:".format(uri))
	out = dht.DHT11(machine.Pin(12)) # d6 p
	while True:
		try:
			t = 900
			out.measure()
			ERROR_IN_MEASUREMENT = False
			mesg = ujson.dumps({'temp': out.temperature(), 'humidity': out.humidity(), 'ERROR_IN_MEASUREMENT': ERROR_IN_MEASUREMENT })
			print(mesg)
		except:
			ERROR_IN_MEASUREMENT = True
			mesg = ujson.dumps({'temp': out.temperature(), 'humidity': out.humidity(), 'ERROR_IN_MEASUREMENT': ERROR_IN_MEASUREMENT})
			print(mesg)
		try:
			req = urequests.post(uri,data = mesg)
			resp = req.text
			print("response : {}".format(resp))
		except Exception as e:
			print(e)
			print("Issue with Connecting to server")
			led.on()
			time.sleep(1)
			led.off()
			time.sleep(2)
			led.on()
			time.sleep(1)
			led.off()
			time.sleep(2)
			t -= 6
			#	websocket = uwebsockets.client.connect(uri) for reconnecting in case closed
		finally:
			print('-'*20)
			time.sleep(t)
	# websocket.close() #finally closing the websocket connection
