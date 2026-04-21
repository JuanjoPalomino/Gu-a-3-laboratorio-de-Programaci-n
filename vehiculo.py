import random
import time

class Vehiculo:
    def __init__(self, canvas, nombre, y):
        self.canvas = canvas
        self.nombre = nombre
        self.y = y
        self.x = 10
        self.velocidad = random.randint(1, 5)
        self.tiempo = 0

        self.direccion = 1  
        self.vueltas = 0
        self.termino = False

        self.figura = canvas.create_rectangle(self.x, y, self.x+40, y+20, fill="red")
        self.texto = canvas.create_text(self.x+20, y-10, text=nombre)

    def mover(self, velocidad_global, meta, inicio, rondas, callback_fin):
        while self.vueltas < rondas:

            self.velocidad = random.randint(1, 5)
            dx = self.velocidad * velocidad_global * self.direccion
            self.x += dx

            self.canvas.move(self.figura, dx, 0)
            self.canvas.move(self.texto, dx, 0)

            if self.x >= meta:
                self.direccion = -1

            if self.x <= inicio:
                self.direccion = 1
                self.vueltas += 1

            self.tiempo += 1

            self.canvas.update()
            time.sleep(0.05)

        self.termino = True
        callback_fin(self)