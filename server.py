import uwebsockets.client
import ujson,time,machine

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
			print(resp)
			time.sleep(60)
		except:
			count += 1
			print(count)

	websocket.close()
