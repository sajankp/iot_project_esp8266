import server
import time

import network
import machine

sta_if = network.WLAN(network.STA_IF)
sta_if.ifconfig()
sta_if.active(True)
sta_if.connect('SKP','sajan.kp')
if sta_if.isconnected():
    out = machine.Pin(16, machine.Pin.OUT)
    out.off()
    time.sleep(3)
    out.on()
    time.sleep(5)
if not sta_if.isconnected():
    out = machine.Pin(16, machine.Pin.OUT)
    for x in range(5):
        out.off()
        time.sleep(2)
        out.on()
        time.sleep(2)

time.sleep(5)

server.main()
