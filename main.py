from machine import UART
import utime
import us100
import pycom

'''
Based on code written by Kai Fricke, available here:
https://github.com/kfricke/micropython-us100

Ported to Pycom based boards by Conor Farrell
https://github.com/conorf50/pycom-us100

'''
# The SiPy has two serial ports, one is used to communicate with the computer
# the second is used here

# Configure second UART bus on pins P3(TX1) and P4(RX1). Refer to datasheet if in doubt
uart1 = machine.UART(1, baudrate=9600)
sensor = us100.US100UART(uart1)

count = 1
while count < 10:
    print(sensor.distance())
    utime.sleep_ms(50)




    