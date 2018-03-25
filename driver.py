import ASUS.GPIO as GPIO

class Driver:
    #data pin locations
    DATA   = 11
    SHIFT  = 13
    STORE  = 12

    #screen settings
    width = 8
    height = 8
    orientation = 3

    #initiate GPIO pins
    def __init__(self):
        self.setupGPIO()
        self.screenData = [0] * (self.width*self.height)
        self.runtime = 0

    def setupGPIO(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.DATA, GPIO.OUT)
        GPIO.setup(self.SHIFT, GPIO.OUT)
        GPIO.setup(self.STORE, GPIO.OUT)
        GPIO.output(self.DATA, GPIO.LOW)
        GPIO.output(self.SHIFT, GPIO.LOW)
        GPIO.output(self.STORE, GPIO.LOW)

    #rotate screen
    def rotate(self):
        self.orientation += 1

    #set a pixel value
    def set(self, x, y, v):
        self.screenData[y*8+x] = v

    def setScreen(self, data):
        for i in range(0,len(data)):
            self.screenData[i] = data[i]

    #clear the screen
    def clear(self):
        for i in range(0,self.height):
            for j in range(0,self.width):
                self.set(i,j,0)
                
    #draw the screen            
    def write(self):
        self.runtime += 1
        o = self.orientation%4
        for i in range(0,self.height):
            for j in range(0,self.width):
                if(o==0):
                    self.pushBit(self.screenData[i*8+j])
                elif(o==1):
                    self.pushBit(self.screenData[j*8+(7-i)])
                elif(o==2):
                    self.pushBit(self.screenData[(7-i)*8+(7-j)])
                else:
                    self.pushBit(self.screenData[(7-j)*8+i])
            self.pushRow(i)
            GPIO.output(self.STORE, 1)
            GPIO.output(self.STORE, 0)

    #push a single bit into shift registers
    def pushBit(self, bit):
        GPIO.output(self.DATA, (not (bit>self.runtime%10)))
        GPIO.output(self.SHIFT, 1)
        GPIO.output(self.SHIFT, 0)

    #push byte describing screen row
    def pushRow(self, row):
        for i in range(0,8):
            GPIO.output(self.DATA, (i==row))
            GPIO.output(self.SHIFT, 1)
            GPIO.output(self.SHIFT, 0)

    #clear GPIO pins
    def clean(self):
        GPIO.cleanup()
