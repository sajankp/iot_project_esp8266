import uwebsockets.client
import ujson,time,machine

def main():
	uri = 'ws://35.244.13.244/ws/post'
	websocket = uwebsockets.client.connect(uri)
	print("Connecting to {}:".format(uri))

	#mesg = ujson.dumps({'value' : 1})
	#websocket.send(mesg)
	#resp = websocket.recv()
	#print(resp)

	out = machine.Pin(16, machine.Pin.IN)

	while True:
		value = out.value()
		print(value)
		mesg = ujson.dumps({'value' : value})
		websocket.send(mesg)
		resp = websocket.recv()
		print(resp)
		time.sleep(10)

	websocket.close()
