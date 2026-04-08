import tkinter as tk
import random
import time

class Vehiculo:
    def __init__(self, canvas, nombre, y):
        self.canvas = canvas
        self.nombre = nombre
        self.y = y
        self.x = 10
        self.velocidad = random.randint(1, 11)
        self.tiempo = 0

        self.direccion = 1  
        self.vueltas = 0

        self.figura = canvas.create_rectangle(self.x, y, self.x+40, y+20, fill="blue")
        self.texto = canvas.create_text(self.x+20, y-10, text=nombre)

    def mover(self, velocidad_global, meta, inicio):
        self.x += self.velocidad * velocidad_global * self.direccion
        self.canvas.move(self.figura, self.velocidad * velocidad_global * self.direccion, 0)
        self.canvas.move(self.texto, self.velocidad * velocidad_global * self.direccion, 0)

        if self.x >= meta:
            self.direccion = -1

        if self.x <= inicio:
            self.direccion = 1
            self.vueltas += 1

 
class Carrera:
    def __init__(self, canvas, num_vehiculos, rondas):
        self.canvas = canvas
        self.vehiculos = []
        self.rondas = rondas
        self.meta = 700
        self.finalizados = []

        for i in range(num_vehiculos):
            v = Vehiculo(canvas, f"V{i+1}", 50 + i*30)
            self.vehiculos.append(v)

    def correr(self, velocidad_global, callback_fin):
        inicio = 10

        en_carrera = True

        while en_carrera:
            en_carrera = False

            for v in self.vehiculos:
                if v.vueltas < self.rondas:
                    v.mover(velocidad_global, self.meta, inicio)
                    v.tiempo += 1
                    en_carrera = True

            self.canvas.update()
            time.sleep(0.05)

        
        self.vehiculos.sort(key=lambda x: x.tiempo)

        callback_fin(self.vehiculos)

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

        self.root.after(100, lambda: self.ejecutar_carrera(apuesta, velocidad_global))

    def ejecutar_carrera(self, apuesta, velocidad_global):
        def fin(vehiculos):
            ganador = vehiculos[0]

            texto = "RESULTADOS:\n"
            for i, v in enumerate(vehiculos):
                texto += f"{i+1}. {v.nombre} - Tiempo: {v.tiempo}\n"

            if ganador.nombre == f"V{apuesta}":
                texto += "\n ¡GANASTE LA APUESTA!"
            else:
                texto += f"\n Perdiste. Ganó {ganador.nombre}"

            self.resultado.config(text=texto)

        self.carrera.correr(velocidad_global, fin)


root = tk.Tk()
app = Interfaz(root)
root.mainloop()