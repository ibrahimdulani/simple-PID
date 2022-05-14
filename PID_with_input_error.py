

class PID(object):

    def __init__(self, Kp=1, Ki=0, Kd=0, dt=0.1) -> None:
        self.kp=Kp
        self.ki=Ki
        self.kd=Kd
        self.time_step=dt

        self.error = 0
        self._proportional = 0
        self._integral = 0 
        self._derivative = 0 
        self.last_error=0

        self.output=0



    def compute(self,er=0):
        self.error = er
        
        self._proportional = self.kp*self.error
        self._integral = self.ki*self.error*self.time_step
        self._derivative = self.kd*(self.error - self.last_error)/self.time_step
        
        self.last_error=self.error

        self.output = self._proportional + self._integral + self._derivative

        return self.output


