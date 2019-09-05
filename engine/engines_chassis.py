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
    pwm_value_straight=90
    pwm_value_turn=60
    
    engine1=engine.Engine(engine1_output1,engine1_output2,engine1_pwm_output ,pwm_value_straight)
    engine2=engine.Engine(engine2_input1 ,engine2_output2,engine2_pwm_output ,pwm_value_straight)
    
    #engine1=engine.Engine()
    #engine2=engine.Engine()
    def move(self, x):
        
        
        if x== 'p':
            self.engine1.stop()
            self.engine2.stop() 
            print("Stop")

            
        elif x== 'w':
            self.engine1.pwm_value.ChangeDutyCycle(self.pwm_value_straight)
            self.engine1.forward()
            self.engine2.forward() 
            print("Forward")

            
        elif x== 's' :
            self.engine1.pwm_value.ChangeDutyCycle(self.pwm_value_straight)
            self.engine1.backward()
            self.engine2.backward() 
            print("Backward")
            
        elif x== 'a':
            self.engine1.pwm_value.ChangeDutyCycle(self.pwm_value_turn)
            self.engine1.forward()
            self.engine2.backward() 
            print("Left")
            
        elif x== 'd' :
            self.engine1.pwm_value.ChangeDutyCycle(self.pwm_value_turn)
            self.engine1.backward()
            self.engine2.forward() 
            print("Right")
            
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

            


        
         
        
       
        
           
