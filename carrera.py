import threading
from vehiculo import Vehiculo

class Carrera:
    def __init__(self, canvas, num_vehiculos, rondas):
        self.canvas = canvas
        self.vehiculos = []
        self.rondas = rondas
        self.meta = 700
        self.finalizados = []

        for i in range(num_vehiculos):
            v = Vehiculo(canvas, f"CARRO {i+1}", 50 + i*30)
            self.vehiculos.append(v)

    def agregar_finalizado(self, vehiculo):
        self.finalizados.append(vehiculo)

    def correr(self, velocidad_global):
        inicio = 10
        hilos = []

        for v in self.vehiculos:
            hilo = threading.Thread(
                target=v.mover,
                args=(velocidad_global, self.meta, inicio, self.rondas, self.agregar_finalizado)
            )
            hilos.append(hilo)
            hilo.start()

        for h in hilos:
            h.join()

        self.finalizados.sort(key=lambda x: x.tiempo)
        return self.finalizados