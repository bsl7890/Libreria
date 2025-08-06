import tkinter as tk
from tkinter import messagebox
from model.biblioteca_modelo import obtener_nombre
from model.libro_modelo import insertar_libro

ventana_libro = None

def crear_libro():


    global ventana_libro
    if ventana_libro is not None and ventana_libro.winfo_exists():
        ventana_libro.lift()  # Trae al frente si ya está abierta
        return

    ventana_libro = tk.Toplevel()
    ventana_libro.title("Creacion libro")
    ventana_libro.geometry("400x300")

    def al_cerrar():
        global ventana_libro
        if ventana_libro is not None:
            ventana_libro.destroy()
            ventana_libro = None

        

    ventana_libro.protocol("WM_DELETE_WINDOW", al_cerrar)  # Manejar el cierre de la ventana

    labelisbn = tk.Label(ventana_libro,text="Escriba el isbn del libro:")
    labelisbn.grid(row=0, column=0, sticky="e")

    input_isbn = tk.Entry(ventana_libro)
    input_isbn.grid(row=0, column=1, padx=5, pady=5)

    labeltitulo = tk.Label(ventana_libro,text="escriba el tituto del libro")
    labeltitulo.grid(row=1, column=0, sticky="e")

    input_titulo = tk.Entry(ventana_libro)
    input_titulo.grid(row=1, column=1, padx=5, pady=5)

    labelautor = tk.Label(ventana_libro,text="escriba el autor del libro:")
    labelautor.grid(row=2, column=0, sticky="e")

    input_autor = tk.Entry(ventana_libro)
    input_autor.grid(row=2, column=1, padx=5, pady=5)

    labelano_publicacion = tk.Label(ventana_libro,text="escriba el año de publicacion del libro:")
    labelano_publicacion.grid(row=3, column=0, sticky="e")

    input_ano_publicacio = tk.Entry(ventana_libro)
    input_ano_publicacio.grid(row=3, column=1, padx=5, pady=5)


    labelano_publicacion = tk.Label(ventana_libro,text="Seleccione el nombre de la libreria:")
    labelano_publicacion.grid(row=4, column=0, sticky="e")

    opciones_libreria = tk.StringVar()
    opciones_libreria.set("Seleccione")
    try:
        nombre_libreria = obtener_nombre()
        if not nombre_libreria:
            raise ValueError("No se encontraron bibliotecas en la base de datos!")
    except Exception as ex:
        messagebox.showerror("Error", "No se pudieron cargar las bibliotecas")
        ventana_libro.destroy()
        ventana_libro = None
        return
    menu = tk.OptionMenu(ventana_libro,opciones_libreria, *nombre_libreria.keys())
    menu.grid(row = 4, column=1, padx=5, pady=5)

    def agregar():
        try:
            isbn = input_isbn.get()
            titulo = input_titulo.get()
            autor = input_autor.get()
            ano_publicacion = input_ano_publicacio.get()
            biblioteca_nombre = opciones_libreria.get().strip()
            if not(isbn and titulo and autor and ano_publicacion and biblioteca_nombre != "Seleccione"):
                messagebox.showwarning("Advertencia", "Debes rellenar los campos!")
                return
            if not ano_publicacion.isdigit():
                messagebox.showerror("Error", "El año de publicación debe ser un número entero.")
                return

            ano_publicacion = int(ano_publicacion)
            biblioteca_id = nombre_libreria[biblioteca_nombre]
            insertar_libro(isbn,titulo,autor,ano_publicacion,biblioteca_id)
            messagebox.showinfo("Mensaje", "libro agregada con exito!")
        except Exception as e:
            messagebox.showerror("Error", e)

    boton_agregarLibro = tk.Button(ventana_libro, text="Agregar libro", command=agregar)
    boton_agregarLibro.grid(row=5, column=1, padx=5, pady=5)