from pyfirmata import Arduino, SERVO
import serial

port='COM6'

pin=10

board=Arduino(port)

board.digital[pin].mode=SERVO

def tempcheck(val1):
    if val1==0:
        ser=board.analog[5].read()
        print(ser)
        #if(ser<="30"):
            #doorAutomate(0)
    else:
        pass


def rotateServo(pin,angle):
    board.digital[pin].write(angle)

def doorAutomate(val):
    if val==0:
        rotateServo(pin, 180)
    elif val==1:
        rotateServo(pin, 40)