from ili9341 import Display
from machine import Pin, SPI
from xpt2046 import Touch

TFT_CLK_PIN = const(6)
TFT_MOSI_PIN = const(7)
TFT_MISO_PIN = const(4)

TFT_CS_PIN = const(13)
TFT_RST_PIN = const(14)
TFT_DC_PIN = const(11)

XPT_CLK_PIN = const(2)
XPT_MOSI_PIN = const(3)
XPT_MISO_PIN = const(4)

XPT_CS_PIN = const(5)
XPT_INT = const(10)

'''
spi1 = SPI(0, baudrate=40000000, sck=Pin(6), mosi=Pin(7))
display = Display(spi1, dc=Pin(11), cs=Pin(13), rst=Pin(14),width=240, height=320,rotation=180)
    
spi2 = SPI(0, baudrate=2000000, sck=Pin(2), mosi=Pin(3), miso=Pin(4)) #touch
'''
def createMyDisplay():
    #spi = SPI(0, baudrate=40000000, sck=Pin(TFT_CLK_PIN), mosi=Pin(TFT_MOSI_PIN))
    spiTFT = SPI(0, baudrate=51200000,
                 sck=Pin(TFT_CLK_PIN), mosi=Pin(TFT_MOSI_PIN))
    display = Display(spiTFT,
                      dc=Pin(TFT_DC_PIN), cs=Pin(TFT_CS_PIN), rst=Pin(TFT_RST_PIN),rotation=180)
    return display

def createXPT(touch_handler):
    spiXPT = SPI(0, baudrate=1000000,
                 sck=Pin(XPT_CLK_PIN), mosi=Pin(XPT_MOSI_PIN), miso=Pin(XPT_MISO_PIN))

    xpt = Touch(spiXPT, cs=Pin(XPT_CS_PIN), int_pin=Pin(XPT_INT),
                int_handler=touch_handler)

    return xpt