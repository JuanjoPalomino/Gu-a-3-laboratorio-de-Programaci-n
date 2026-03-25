import tkinter as tk
import time
import threading

pila = []
ocupado = False

class Tarea:
    def __init__(self, tipo, tiempo):
        self.tipo = tipo
        self.tiempo = tiempo
        
def Etarea(tarea):
    global ocupado
    ocupado = True

    for i in range(tarea.tiempo):
        output.delete("1.0", tk.END)
        output.insert(tk.END, f"Tarea: {tarea.tipo} | Tiempo: {i+1}s")

        output.update()
        time.sleep(1)

    output.delete("1.0", tk.END)
    output.insert(tk.END, "Tarea terminada\n")

    ocupado = False
def NewTarea():
    tipo = entry_tipo.get()
    tiempo = int(entry_tiempo.get())
    tarea = Tarea(tipo, tiempo)
    if not ocupado:
        threading.Thread(target=Etarea, args=(tarea,)).start()
    else:
        pila.append(tarea)
        output.insert(tk.END, "Tarea guardada en pila\n")
def epila():
    def exe():
        while pila:
            tarea = pila.pop()
            Etarea(tarea)
    threading.Thread(target=exe).start()
ventana = tk.Tk()
ventana.title("Robot con Pila")

tk.Label(ventana, text="Tipo:").pack()
entry_tipo = tk.Entry(ventana)
entry_tipo.pack()

tk.Label(ventana, text="Tiempo:").pack()
entry_tiempo = tk.Entry(ventana)
entry_tiempo.pack()

tk.Button(ventana, text="Agregar tarea", command=NewTarea).pack()
tk.Button(ventana, text="Ejecutar pila", command=epila).pack()

output = tk.Text(ventana, height=20, width=50)
output.pack()
ventana.mainloop()