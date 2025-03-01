import numpy as np
import matplotlib
matplotlib.use('Agg')  # Usa il backend 'Agg' per rendering non interattivo
import matplotlib.pyplot as plt
import control as ctrl
from car import  Car
from controller import Controller
from closedloopsystem import ClosedLoopSystem
from simulation import Simulation

# Parametri del sistema (modifica questi valori per ottenere diverse risposte)
mass = 0.0001  # Massa (in kg)
damping = 0.1  # Smorzamento (in Ns/m)
time_interval = np.linspace(0, 10, 1000)  # Intervallo di tempo per la simulazione

# Creazione degli oggetti per la macchina, il controllore e il sistema chiuso
car = Car(mass, damping)
controller = Controller(mass, damping)
closed_loop_system = ClosedLoopSystem(car, controller)

# Creazione della simulazione
simulation = Simulation(closed_loop_system, time_interval)

# Esecuzione della simulazione
time, response = simulation.run()

# Visualizzazione della risposta
simulation.plot_response(time, response)