import control as ctrl

class Controller:
    def __init__(self, mass, damping,kp):
        self.mass = mass
        self.damping = damping
        self.kp = kp
        self.L_s = kp*ctrl.TransferFunction([self.mass, self.damping], [1, 0])  # Funzione di trasferimento del controllore ((mass*s + damping)/(s))....
        #Più si auementa KP più più la risposta in frequenza sarà alta