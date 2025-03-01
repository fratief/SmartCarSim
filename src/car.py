
import control as ctrl

class Car:
    def __init__(self, mass, damping):
        self.mass = mass
        self.damping = damping
        self.G_s = ctrl.TransferFunction([1], [self.mass, self.damping])  # Funzione di trasferimento del sistema G(s)