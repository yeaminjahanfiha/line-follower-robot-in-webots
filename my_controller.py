from controller import Robot

def run_robot(robot):
    time_step=32
    max_speed=6.28
    motor_1=robot.getDevice('motor_1')
    motor_2=robot.getDevice('motor_2')
    motor_1.setPosition(float('inf'))
    motor_2.setPosition(float('inf'))
    motor_1.setVelocity(0.0)
    motor_2.setVelocity(0.0)
    
    ir0=robot.getDevice('ir0')
    ir0.enable(time_step)
    
    ir1=robot.getDevice('ir1')
    ir1.enable(time_step)
    
    ir0_5=robot.getDevice('ir0_5')
    ir0_5.enable(time_step)
    
    while robot.step(time_step) !=-1:
        
        left_ir_value=ir0.getValue()
        right_ir_value=ir1.getValue()
        mid_ir_value=ir0_5.getValue()
        
        print("left : {} mid:{} right : {}".format(left_ir_value,mid_ir_value,right_ir_value))
        
        left_speed=max_speed
        right_speed=max_speed
        
        if ( left_ir_value <1000 ) and (right_ir_value<1000)and( mid_ir_value>=1000 ):
     
            left_speed = -max_speed
            right_speed=-max_speed
        elif ( left_ir_value<1000 ) and (right_ir_value>=1000 ) and (mid_ir_value>=1000):
   
            left_speed=-max_speed
            right_speed =0   
        elif(left_ir_value>=1000)and(right_ir_value<1000)and(mid_ir_value>=1000):
            left_speed=0
            right_speed=-max_speed
        elif(left_ir_value>=1000)and(right_ir_value<1000)and(mid_ir_value<1000):
            left_speed=0
            right_speed=-max_speed
        elif(left_ir_value<1000)and(right_ir_value>=1000)and(mid_ir_value<1000):
            left_speed=-max_speed
            right_speed=0
        elif(left_ir_value<1000)and(right_ir_value<1000)and(mid_ir_value<1000):
            left_speed=-max_speed
            right_speed=-max_speed
                 
        motor_1.setVelocity(left_speed)
        motor_2.setVelocity(right_speed)
        
if __name__ == "__main__":
    my_robot = Robot() 
    run_robot(my_robot)       