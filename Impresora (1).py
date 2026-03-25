import tkinter as tk
from collections import deque


ventana = tk.Tk()
ventana.title("Sistema de Venta de Aplicaciones")

nomDoc = tk.Label(ventana, text="Nombre Documento:").grid(row=0,column=0,padx=10,pady=10)

nomDoc = tk.Entry(ventana)
nomDoc.grid(row=0,column=1,padx=10,pady=10) 

numPag = tk.Label(ventana, text="Numero de paginas:").grid(row=1,column=0,padx=20,pady=20)

numPag = tk.Entry(ventana)
numPag.grid(row=1,column=1,padx=10,pady=10) 

Tiempo = tk.Label(ventana, text="Tiempo por pagina:").grid(row=2,column=0,padx=30,pady=30)

Tiempo = tk.Entry(ventana)
Tiempo.grid(row=2,column=1,padx=10,pady=10) 

cola=deque()

def mostrar_texto():
    texto1 = nomDoc.get()
    texto2 = numPag.get()
    texto3 = Tiempo.get()

    cola.append((texto1, int(texto2), int(texto3)))

    etiqueta0.config(text=f"Documento en Cola: {list(cola)}")

    etiqueta2.config(text=f"Nombre: {texto1}")
    etiqueta3.config(text=f"Paginas: {texto2}")
    etiqueta4.config(text=f"Tiempo: {texto3}")

boton_Agregar = tk.Button(ventana, text="Agregar documento a la cola", command=mostrar_texto)
boton_Agregar.grid(row=3,column=1,padx=10,pady=10) 

etiqueta0 = tk.Label(ventana, text="")
etiqueta0.grid(row=4,column=0,padx=10,pady=10) 

etiqueta2 = tk.Label(ventana, text="")
etiqueta2.grid(row=5,column=1,padx=10,pady=10) 

etiqueta3 = tk.Label(ventana, text="")
etiqueta3.grid(row=6,column=1,padx=10,pady=10) 

etiqueta4 = tk.Label(ventana, text="")
etiqueta4.grid(row=7,column=1,padx=10,pady=10) 

def imprimir_pagina(texto1, texto2, texto3, pagina_actual):

    if pagina_actual <= texto2:
        etiqueta2.config(
            text=f"Imprimiendo página {pagina_actual} de {texto2} del documento {texto1}"
        )

        ventana.after(
            int(texto3*1000),
            lambda: imprimir_pagina(texto1, texto2, texto3, pagina_actual + 1)
        )
    else:
        etiqueta2.config(text=f"Documento '{texto1}' terminado")

        etiqueta0.config(text=f"Documentos en cola: {list(cola)}")

def imprimir():

    if len(cola) > 0:
        texto1, texto2, texto3 = cola.popleft()
        imprimir_pagina(texto1, texto2, texto3, 1)
    else:
        etiqueta2.config(text="No hay documentos en cola")


boton_imprimir = tk.Button(ventana, text="Empezar impresion", command=imprimir)
boton_imprimir.grid(row=8,column=0,padx=10,pady=10) 

etiqueta1 = tk.Label(ventana, text="")
etiqueta1.grid(row=9,column=0,padx=10,pady=10) 


ventana.mainloop()

