import uwebsockets.client
import ujson, time, machine, dht

def main():
	uri = 'ws://35.244.13.244/ws/post'
	websocket = uwebsockets.client.connect(uri)
	print("Connecting to {}:".format(uri))
	out = dht.DHT11(machine.Pin(12)) # d6 pin
	count = 0
	while True:
		try:
			out.measure()
			print("temp :",out.temperature())
			mesg = ujson.dumps({'temp' : out.temperature()})
			websocket.send(mesg)
			resp = websocket.recv()
			print("response : {}".format(resp))
		except AssertionError:
			print("connection issue")
			websocket = uwebsockets.client.connect(uri)
			print("Connecting to {}: and status is {}".format(uri,websocket.open))
		except:
			count += 1
			print(count)
		finally:
			print('-'*20)
			time.sleep(20)
	websocket.close()
