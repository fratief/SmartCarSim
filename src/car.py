


class Car:
    def __init__(self, max_speed, m, d):
        self.speed = 0
        self.max_speed =max_speed
        self.m = m
        self.d = d
        self.err_sum = 0
        self.prev_err = 0

    def set_speed_d(self,desired_speed):
        self.desired_speed = desired_speed

    
        
