# Creacion de pantalla
import tkinter as tk
from gui.formulario_biblioteca import crear_biblioteca
ventana = tk.Tk()
ventana.title("Formulario")
ventana.geometry("650x500")
crear_biblioteca(ventana)
ventana.mainloop()
