# Creacion de pantalla
import tkinter as tk
from gui.formaulario_biblioteca import crear_biblioteca
ventana = tk.Tk()
ventana.title("Formulario")
ventana.geometry("300x200")
crear_biblioteca(ventana)
ventana.mainloop()
