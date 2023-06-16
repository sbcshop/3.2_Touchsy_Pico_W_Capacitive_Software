import network
from time import sleep
import machine
import urequests # handles making and servicing network requests
import json

ssid = 'your network ssid'
password = 'your network password'

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    
    # GET request for website and print HTML
    r = urequests.get("http://www.google.com")
    print(r.content)
    
    r = urequests.get("http://date.jsontest.com") # Server that returns the current GMT+0 time.
    print(r.json())
    r.close()
    return ip

try:
    ip = connect()
except KeyboardInterrupt:
    machine.reset()
