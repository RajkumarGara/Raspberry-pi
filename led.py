import machine
import time

led = machine.Pin("LED", machine.Pin.OUT)
gio17 = machine.Pin(17, machine.Pin.OUT)
cnt = 0

while True:
    led.on()
    gio17.value(1)
    time.sleep(0.5)    
    
    led.off()
    gio17.value(0) 
    time.sleep(0.5)
    
    print(cnt)
    cnt = cnt + 1
    