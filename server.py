import uwebsockets.client
import ujson, time, machine, dht

def main():
	uri = 'ws://35.244.13.244/ws/post'
	# uri = 'ws://echo.websocket.org/'
	websocket = uwebsockets.client.connect(uri)
	print("Connecting to {}:".format(uri))
	out = dht.DHT11(machine.Pin(12)) # d6 pin
	count = 0
	while True:
		try:
			out.measure()
			print("temp :",out.temperature())
			mesg = ujson.dumps({'temp' : out.temperature()})
		except:
			count += 1
			print(count)
		try:
			websocket.send(mesg)
			resp = websocket.recv()
			print("response : {}".format(resp))
		except Exception as e:
			print(e)
			print("connection part")
		finally:
			print('-'*20)
			time.sleep(900)
	websocket.close()
