'''
RaspberryPi Alphabot: test version of the alphabot library

@Andrea-Tomatis
@Nicolo-Cora
'''

# Copy of the Alphabot class.
# Every method returns only a string to print
class AlphaBot(object):
    
    def __init__(self, in1=13, in2=12, ena=6, in3=21, in4=20, enb=26):
        pass # no parameters are needed to make the object run

    def forward(self):
        return 'forward'

    def stop(self):
        return 'stop'

    def backward(self):
        return 'backward'

    def left(self, speed=30):
        return 'turn left'

    def right(self, speed=30):
        return 'turn right'
        
    def set_pwm_a(self, value): # simulates the motorA pulse modulation
        return f'set pwm_a to {value}'

    def set_pwm_b(self, value): # simulates the motorA pulse modulation
        return f'set pwm_b to {value}'    
        
    def set_motor(self, left, right): #simulates the motors settings
        return 'motors settled'


