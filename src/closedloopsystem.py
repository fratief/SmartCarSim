
class ClosedLoopSystem:
    def __init__(self, car, controller):
        self.car = car
        self.controller = controller
        self.T_s = self.calculate_closed_loop_transfer_function()
    
    def calculate_closed_loop_transfer_function(self):
        """Calcola la funzione di trasferimento del sistema chiuso"""
        return self.controller.L_s * self.car.G_s / (1 + self.controller.L_s * self.car.G_s)