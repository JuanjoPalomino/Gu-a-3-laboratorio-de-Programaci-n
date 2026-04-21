import tkinter as tk
import random
import time
import threading

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


class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Carrera de Vehículos")

        self.canvas = tk.Canvas(root, width=800, height=400, bg="white")
        self.canvas.pack()

        self.frame = tk.Frame(root)
        self.frame.pack()

        tk.Label(self.frame, text="Rondas:").grid(row=0, column=0)
        self.entry_rondas = tk.Entry(self.frame)
        self.entry_rondas.insert(0, "1")
        self.entry_rondas.grid(row=0, column=1)

        tk.Label(self.frame, text="Apuesta (1-10):").grid(row=1, column=0)
        self.entry_apuesta = tk.Entry(self.frame)
        self.entry_apuesta.grid(row=1, column=1)

        tk.Label(self.frame, text="Velocidad:").grid(row=2, column=0)
        self.velocidad = tk.Scale(self.frame, from_=1, to=5, orient="horizontal")
        self.velocidad.set(2)
        self.velocidad.grid(row=2, column=1)

        self.btn = tk.Button(self.frame, text="Iniciar Carrera", command=self.iniciar)
        self.btn.grid(row=3, column=0, columnspan=2)

        self.resultado = tk.Label(root, text="")
        self.resultado.pack()

    def iniciar(self):
        self.canvas.delete("all")

        rondas = int(self.entry_rondas.get())
        apuesta = int(self.entry_apuesta.get())
        velocidad_global = self.velocidad.get()

        self.carrera = Carrera(self.canvas, 10, rondas)

        threading.Thread(
            target=self.ejecutar_carrera,
            args=(velocidad_global, apuesta)
        ).start()

    def ejecutar_carrera(self, velocidad_global, apuesta):
        vehiculos = self.carrera.correr(velocidad_global)

        texto = "RESULTADOS:\n"
        for i, v in enumerate(vehiculos):
            texto += f"{i+1}. {v.nombre} - Tiempo: {v.tiempo}\n"

        if vehiculos[0].nombre == f"CARRO {apuesta}":
            texto += "\n¡GANASTE!"
        else:
            texto += f"\nPerdiste. Ganó {vehiculos[0].nombre}"

        self.resultado.config(text=texto)


root = tk.Tk()
app = Interfaz(root)
root.mainloop()