import control as ctrl

class Controller:
    def __init__(self, mass, damping):
        self.mass = mass
        self.damping = damping
        self.L_s = ctrl.TransferFunction([self.mass, self.damping], [1, 0])  # Funzione di trasferimento del controllore ((mass*s + damping)/(s)).... 