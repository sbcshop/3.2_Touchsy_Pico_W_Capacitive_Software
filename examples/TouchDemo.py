'''
For this example code external library used -> ili9341.py, xglcd_font.py, config.py
dependent touch libraries -> FT6236.py
from lib folder-> https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software/tree/main/lib
'''
from machine import SPI,Pin,PWM,I2C
import time,os
from FT6236 import Touch
from ili9341 import Display, color565
from xglcd_font import XglcdFont

#configure touch controller for I2C interface with Pico
i2c=I2C(0,sda=Pin(20), scl=Pin(21))

unispace = XglcdFont('Unispace12x24.c', 12, 24)

#GP15 connected to backlight of Display 
BL = Pin(15, Pin.OUT) # make as OUTPUT
BL.value(1) # set pin as HIGH i.e turns on BackLight

#configure display spi interface
spi = SPI(0, baudrate=40000000, sck=Pin(6), mosi=Pin(7))
display = Display(spi, dc=Pin(11), cs=Pin(13), rst=Pin(14),rotation = 180)
time.sleep(1)

print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config
print('Scan i2c bus...')
devices = i2c.scan()
print(devices)

if len(devices) == 0:
      print("No i2c device !")
else:
     print('i2c devices found:',len(devices))

for device in devices:
     print("Decimal address: ",device," | Hexa address: ",hex(device))

ft = Touch(i2c,debug=False)

display.draw_text(50, 25, '3.2" Touchsy', unispace,color565(0, 255, 255))
display.draw_text(75, 50, 'Pico W', unispace,color565(0, 255, 255))
display.draw_text8x8(60, 80,' Capacitive ', color565(255, 255, 0))
display.draw_text8x8(20, 290,'Press, Hold and move Pen', color565(255, 255, 0))

time.sleep(0.5)
while 1:
    if ft.touched:	# if the screen is being touched print the touches
        print(ft.touches)
        lst = ft.touches
        #print(lst[0])
        if len(lst)>0:
            lst = lst[0]
            x = lst['x']
            y = lst['y']
            
            display.draw_text8x8(x,y,"*",color565(255, 0, 255))
            display.draw_text8x8(display.width // 2 - 32,display.height - 9,"{0:03d}, {1:03d}".format(x, y),color565(255, 255, 0))
    
    time.sleep(0.03)
