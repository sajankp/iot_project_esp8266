# import uwebsockets.client
import urequests
import ujson
import time
import machine
import dht

with open('secret') as f:
    secret_key = f.read().strip()


def main():
    uri = 'http://35.244.13.244/iot/post'
    # uri = 'http://192.168.225.201:8000/iot/post' # for testing
    # uri = 'ws://echo.websocket.org/' # for websocket testing
    # websocket = uwebsockets.client.connect(uri) # for websocket use
    led = machine.Pin(16, machine.Pin.OUT)
    print("Connecting to {}:".format(uri))
    out = dht.DHT11(machine.Pin(12))
    # d6 p
    FIRST = True
    while True:
        try:
            t = 1799.3
            out.measure()
            ERROR_IN_MEASUREMENT = False
            mesg = ujson.dumps({'secretkey': secret_key,
                                'temp': out.temperature(),
                                'humidity': out.humidity(),
                                'ERROR_IN_MEASUREMENT': ERROR_IN_MEASUREMENT,
                                'FIRST': FIRST})
            print(mesg)
        except:
            ERROR_IN_MEASUREMENT = True
            mesg = ujson.dumps({'secretkey': secret_key,
                                'temp': out.temperature(),
                                'humidity': out.humidity(),
                                'ERROR_IN_MEASUREMENT': ERROR_IN_MEASUREMENT,
                                'FIRST': FIRST})
            print("error", mesg)
            led.off()
        try:
            req = urequests.post(uri, data=mesg)
            req = ujson.loads(req.content)
            resp = req['message']
            print("response : {}".format(resp))
            if not led.value():
                led.on()
            if FIRST:
                print("next reading will be taken in {} seconds".format(req['time']))
                t = req['time']
                if t > 100000:
                    led.off()
                FIRST = False
        except Exception as e:
            print(e)
            for x in range(3):
                led.on()
                time.sleep(2)
                led.off()
                time.sleep(2)
            t -= 6
            # websocket = uwebsockets.client.connect(uri)
            # for reconnecting in case it is closed
        finally:
            print('-'*20)
            time.sleep(t)
    # websocket.close() #finally closing the websocket connection
