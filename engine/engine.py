import RPi.GPIO as GPIO          

class Engine :
    def __init__(self,pin_output1,pin_output2, pin_pwm_output,pwm_value):
        self.output1 = pin_output1
        self.output2 = pin_output2
        self.pwm_output = pin_pwm_output

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.output1,GPIO.OUT)
        GPIO.setup(self.output2,GPIO.OUT)
        GPIO.setup(self.pwm_output,GPIO.OUT)
    
        GPIO.output(self.output1,GPIO.LOW)
        GPIO.output(self.output2,GPIO.LOW)
    
        self.pwm_value=GPIO.PWM(self.pwm_output,1000)
        self.pwm_value.start(pwm_value)


    def forward(self):
        GPIO.output(self.output1,GPIO.LOW)
        GPIO.output(self.output2,GPIO.HIGH)
    
    def backward(self):
        GPIO.output(self.output1,GPIO.HIGH)
        GPIO.output(self.output2,GPIO.LOW)
    
    def stop(self):
        GPIO.output(self.output1,GPIO.LOW)
        GPIO.output(self.output2,GPIO.LOW)
        
    def end(self):
        GPIO.cleanup()
            
        
       
