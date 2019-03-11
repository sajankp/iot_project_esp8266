import machine
import time
out = machine.Pin(16, machine.Pin.OUT)
def main():
    while True:
        out.off()
        time.sleep(3)
        out.on()
        time.sleep(5)
