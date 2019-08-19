import RPi.GPIO as GPIO          
from time import sleep


in1 = 23
in2 = 24
en = 25

ein1 = 22
ein2 = 27
een = 17

class Engine :
    in1 = 23
    in2 = 24
    en = 25

    ein1 = 22
    ein2 = 27
    een = 17

    temp1=1

    GPIO.cleanup()

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(en,GPIO.OUT)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    p=GPIO.PWM(en,1000)
    p.start(50)

    GPIO.setup(ein1,GPIO.OUT)
    GPIO.setup(ein2,GPIO.OUT)
    GPIO.setup(een,GPIO.OUT)
    GPIO.output(ein1,GPIO.LOW)
    GPIO.output(ein2,GPIO.LOW)
    pe=GPIO.PWM(een,1000)
    pe.start(50)
    print("\n")

    print("\n")    


    def move(self, x):

        if x=='p':
            print("stop")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            
            GPIO.output(ein1,GPIO.LOW)
            GPIO.output(ein2,GPIO.LOW)
            x='z'

        
        
        elif x=='w':
            print("forward")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            
            GPIO.output(ein1,GPIO.LOW)
            GPIO.output(ein2,GPIO.HIGH)
            
            
            temp1=1
            x='z'
       
        


        elif x=='s':
            print("backward")
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            
            GPIO.output(ein1,GPIO.HIGH)
            GPIO.output(ein2,GPIO.LOW)
            temp1=0
            x='z'
            
        elif x=='a':
            print("left")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            
            GPIO.output(ein1,GPIO.HIGH)
            GPIO.output(ein2,GPIO.LOW)
            
            
            temp1=1
            x='z'


        elif x=='d':
            print("right")
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            
            GPIO.output(ein1,GPIO.LOW)
            GPIO.output(ein2,GPIO.HIGH)
            temp1=0
            x='z'
            
            

        elif x=='l':
            print("low")
            p.ChangeDutyCycle(25)
            pe.ChangeDutyCycle(25)
            x='z'

        elif x=='m':
            print("medium")
            
            p.ChangeDutyCycle(50)
            pe.ChangeDutyCycle(50)
            x='z'

        elif x=='h':
            print("high")
            p.ChangeDutyCycle(75)
            pe.ChangeDutyCycle(75)
            x='z'
         
        
        elif x=='e':
            GPIO.cleanup()
            
        
        else:
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            
            GPIO.output(ein1,GPIO.LOW)
            GPIO.output(ein2,GPIO.LOW)
            print("<<<  wrong data  >>>")
            print("please enter the defined data to continue.....")