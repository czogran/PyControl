from engine import engine



class EnginesChassis :
    #default values of engines pins
    engine1_output1 = 23
    engine1_output2 = 24
    engine1_pwm_output = 25

    engine2_input1 = 22
    engine2_output2 = 27
    engine2_pwm_output = 17
    
    #default value of pwm
    pwm_value=50
    
    engine1=engine.Engine(engine1_output1,engine1_output2,engine1_pwm_output ,pwm_value)
    engine2=engine.Engine(engine2_input1 ,engine2_output2,engine2_pwm_output ,pwm_value)
    
    #engine1=engine.Engine()
    #engine2=engine.Engine()
    def move(self, x):
        
        
        if x== 'p':
            print("Stop")
            self.engine1.stop()
            self.engine2.stop() 
            
        elif x== 'w':
            print("Forward")
            self.engine1.forward()
            self.engine2.forward() 
            
        elif x== 's' :
            print("Forward")
            self.engine1.backward()
            self.engine2.backward() 
            
        elif x== 'a':
            print("Left")
            self.engine1.forward()
            self.engine2.backward() 
            
        elif x== 'd' :
            print("Right")
            self.engine1.backward()
            self.engine2.forward() 
            
        elif x== 'e':
            self.engine1.end()
            self.engine2.end()
            
        elif x=='l':
            print("low")
            self.engine1.pwm_value.ChangeDutyCycle(25)
            self.engine2.pwm_value.ChangeDutyCycle(25)
          

        elif x=='m':
            print("medium")
            
            self.engine1.pwm_value.ChangeDutyCycle(50)
            self.engine2.pwm_value.ChangeDutyCycle(50)

        elif x=='h':
            print("high")
            self.engine1.pwm_value.ChangeDutyCycle(75)
            self.engine2.pwm_value.ChangeDutyCycle(75)
        else:
            print("<<<  wrong data  >>>")
            print("please enter the defined data to continue.....")

            


        
         
        
       
        
           
