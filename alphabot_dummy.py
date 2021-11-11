'''
Stupid version of the Alphabot module
'''

import time


class AlphaBot(object):
    
    def __init__(self, in1=13, in2=12, ena=6, in3=21, in4=20, enb=26):
        pass

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
        
    def set_pwm_a(self, value):
        return f'set pwm_a to {value}'

    def set_pwm_b(self, value):
        return f'set pwm_b to {value}'    
        
    def set_motor(self, left, right):
        return 'motors settled'


if __name__ == '__main__':

    Ab = AlphaBot()
    Ab.forward()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass