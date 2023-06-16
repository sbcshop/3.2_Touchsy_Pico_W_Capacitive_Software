'''
For this example code external library used -> sdcard.py
from lib folder-> https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Software/tree/main/lib
----------------------------------------------------------------------------------------------------
This simple demo code creates new file as File.txt into SD card and writes 'Hello World!' text inside file 
'''                

from machine import Pin, SPI ,UART
import sdcard
import os
import utime

uart = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))

def sdtest(data):
    #define and configure SPI interfacing of sdcard with Pico
    spi=SPI(0,sck=Pin(18),mosi=Pin(19),miso=Pin(16))
    sd=sdcard.SDCard(spi,Pin(17))

    #mount file system
    vfs = os.VfsFat(sd)
    os.mount(vfs, "/fc") 
    print("Filesystem check")
    print(os.listdir("/fc"))

    #file name 
    fn = "/fc/File.txt"
    print()
    print("Single block read/write")

    #write operation 
    with open(fn, "a") as f:
        n = f.write(data)  
        print(n, "bytes written")

    #read operation
    with open(fn, "r") as f:
        result2 = f.read()
        print(len(result2), "bytes read")

    os.umount("/fc")
while True:
    sdtest('Hello World!')
    utime.sleep(0.5)
