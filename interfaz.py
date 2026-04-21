import tkinter as tk
import threading
from carrera import Carrera

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