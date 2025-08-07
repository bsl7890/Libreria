import tkinter as tk
from tkinter import messagebox, ttk
from model.biblioteca_modelo import agregar_biblioteca, nombre_biblioteca_existe, obtener_biblioteca
from gui.formulario_libros import crear_libro
def crear_biblioteca(root:tk.Tk):
    root.title("Formulario bilbioteca")
    labelid = tk.Label(root,text="Id bilioteca:")
    labelid.grid(row=0, column=0, sticky="e")

    input_id = tk.Entry(root)
    input_id.grid(row=0, column=1, padx=5, pady=5)

    labelnombre = tk.Label(root,text="nombre")
    labelnombre.grid(row=1, column=0, sticky="e")

    input_nombre = tk.Entry(root)
    input_nombre.grid(row=1, column=1, padx=5, pady=5)

    labelubicacion = tk.Label(root,text="Ubicacion:")
    labelubicacion.grid(row=2, column=0, sticky="e")

    input_ubicacion = tk.Entry(root)
    input_ubicacion.grid(row=2, column=1, padx=5, pady=5)

    def agregar():
        try:
            id = input_id.get()
            nombre = input_nombre.get().strip().lower()
            ubicacion = input_ubicacion.get()
            if not(id and nombre and ubicacion):
                messagebox.showwarning("Advertencia", "Debes rellenar los campos!")
                return
            if nombre_biblioteca_existe(nombre):
                messagebox.showerror("Error", f"Ya existe una biblioteca con el nombre '{nombre}'.")
                return
            agregar_biblioteca(id, nombre, ubicacion)
            cargar_biblioteca()
            messagebox.showinfo("Mensaje", "Biblioteca agregada con exito!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    boton_guardar = tk.Button(root,  text="Registrar", command= agregar)
    boton_guardar.grid(row=3, column=1, padx=5)


    boton_agregarLibro = tk.Button(root, text="Agregar libro", command=crear_libro)
    boton_agregarLibro.grid(row=4, column=1, padx=5, pady=5)

    # Vamos a mostrar una tablita:
    lista_biblioteca = tk.Label(root, text = "Listado biblioteca")
    lista_biblioteca.grid(row=5, column=0, columnspan=2)

    tabla = ttk.Treeview(root, columns=("ID", "NOMBRE", "UBICACION"), show="headings")
    tabla.heading("ID", text="ID")
    tabla.heading("NOMBRE", text="Nombre")
    tabla.heading("UBICACION", text="Ubicación")
    tabla.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

    # Función para cargar bibliotecas
    def cargar_biblioteca():
        try:
            for fila in tabla.get_children():
                tabla.delete(fila)

            biblioteca = obtener_biblioteca()
            for b in biblioteca:
                tabla.insert("", "end", values=b)

        except Exception as error:
            messagebox.showerror("Error", f"No se pudieron cargar las bibliotecas:\n{error}")

    # Cargar datos al inicio
    cargar_biblioteca()