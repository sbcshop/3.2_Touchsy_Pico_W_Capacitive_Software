'''
For this example code external library used ili9341.py, xglcd_font.py
from lib folder-> https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software/tree/main/lib
'''

from machine import Pin, SPI
import ili9341
from xglcd_font import XglcdFont
from ili9341 import Display, color565


#GP15 connected to backlight of Display 
BL = Pin(15, Pin.OUT) # make as OUTPUT
BL.value(1) # set pin as HIGH i.e turns on BackLight

#configure display spi interface
spi = SPI(0, baudrate=40000000, sck=Pin(6), mosi=Pin(7))
display = Display(spi, dc=Pin(11), cs=Pin(13), rst=Pin(14),rotation = 180)

#using Unispace font -> https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software/tree/main/fonts
unispace = XglcdFont('Unispace12x24.c', 12, 24) 

display.clear()
display.draw_text(50, 25, '3.2" Touchsy', unispace,color565(0, 255, 255))
display.draw_text(75, 50, 'Pico W', unispace,color565(0, 255, 255))
display.draw_text8x8(65, 80,' Capacitive ', color565(255, 255, 0))
display.draw_text(40, 130, "Hello...", unispace, color565(255, 250, 255))


