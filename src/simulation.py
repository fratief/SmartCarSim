import numpy as np
import os
import matplotlib
import matplotlib.pyplot as plt
import control as ctrl

class Simulation:
    def __init__(self, system, time_interval):
        self.system = system
        self.time_interval = time_interval
    
    def run(self):
        """Simula la risposta del sistema a un ingresso step"""
        time, response = ctrl.step_response(self.system.T_s, self.time_interval)
        return time, response
    
    def plot_response(self, time, response):
        """Visualizza la risposta del sistema"""
        plt.plot(time, response)
        plt.title('Risposta del Sistema con Controllo (Retroazione)')
        plt.xlabel('Tempo (s)')
        plt.ylabel('Risposta')
        plt.grid(True)
        file_path = 'tests/figure.png'
        counter = 1
        # Verifica se il file esiste già
        while os.path.exists(file_path):
            # Se il file esiste, aggiungi il contatore al nome del file
            file_path = f'tests/figure_{counter}.png'
            counter += 1
        # Salva la figura con il nuovo nome
        plt.savefig(file_path)