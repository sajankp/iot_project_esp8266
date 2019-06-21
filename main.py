import server
import time
import network
import machine

sta_if = network.WLAN(network.STA_IF)
sta_if.ifconfig()
sta_if.active(True)

with open('wifi_secret') as f:
    a = f.readlines()
    wifi_name = a[0].strip()
    wifi_password = a[1].strip()

sta_if.connect(wifi_name, wifi_password)
out = machine.Pin(16, machine.Pin.OUT)

while (not sta_if.isconnected()):
        out.off()
        time.sleep(2)
        out.on()
        time.sleep(2)

server.main()
