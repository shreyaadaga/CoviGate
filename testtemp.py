from pyfirmata import Arduino
from pyfirmata.util import Iterator
import time

board = Arduino('COM6') # connect to arduino usb port

iterator = Iterator(board) # start reading analog input
iterator.start()

pinTemp = board.get_pin('a:1:i') # set valid in analog pin

while True:
    voltage = pinTemp.read() # read voltage input
    if voltage is not None: # first read after startup is somtimes None
        temp = (voltage/1024.0)*3300# convert voltage to temperature
        print (temp/10)
        time.sleep(1) # 1 second waiting 