from threading import Thread
import RPi.GPIO as G
import time
import socket

a = '\0'

class control():
    def __init__(self):
        s = socket.socket()

        s.bind(('', 1234))
        s.listen()
        while True:
           # Establish connection with client.
           c, addr = s.accept()
           print("Connected")
           # send a thank you message to the client.
           a = c.recv(4)
           print(a)
           # Close the connection with the client
           c.close()

class motor ():
    def __init__(self,pins):
        G.setwarnings(False)
        G.setmode(G.BCM)
        for pin in pins:
            G.setup(pin[0],G.OUT)
            G.setup(pin[1],G.OUT)
        self.motorPins = list()
        for pin in pins:
            self.motorPins.append((G.PWM(pin[0], 100),G.PWM(pin[1], 100)))

        for motor in self.motorPins:
            motor[0].start(0)
            motor[1].start(0)

        self.control()

    def control(self):

        while(a!='quit'):
            motorNumber, speed = a.split(' ')
            if speed>0:
                self.motorPins[motorNumber][0].ChangeDutyCycle(speed)
                self.motorPins[motorNumber][1].ChangeDutyCycle(0)
            elif speed<0:
                self.motorPins[motorNumber][0].ChangeDutyCycle(0)
                self.motorPins[motorNumber][1].ChangeDutyCycle(speed)
            else:
                self.motorPins[motorNumber][0].ChangeDutyCycle(0)
                self.motorPins[motorNumber][1].ChangeDutyCycle(0)


motorList = {(2,3), (17,27), (9,11), (8,7), (14,15), (23,24)}
m = motor(motorList)
