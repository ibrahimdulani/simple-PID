import time

class PID(object):

    def __init__(self, Kp=1.0, Ki=0.0, Kd=0.0, target=0, dt=1):

        self.kp = Kp
        self.ki = Ki
        self.kd = Kd
        self.setpoint=target
        self.time_step = dt

        self.error = 0
        self.last_error = 0
        self._proportional = 0
        self._integral=0
        self._derivative=0 

        self.output = 0

        
    def compute(self, input_):

        self.error = self.setpoint - input_

        self._proportional = self.kp * self.error
        self._integral += self.ki * self.error * self.time_step
        self._derivative = self.kd*(self.error - self.last_error)/ self.time_step 
        self.last_error = self.error

        self.output = self._proportional + self._integral + self._derivative

        return self.output



            




