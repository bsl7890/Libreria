from db.conexion_oracle import obtener_conexion


def agregar_biblioteca(id_biblioteca, nombre_biblioteca, ubicacion_biblioteca):
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO biblioteca VALUES (:1, :2, :3)",
                       [id_biblioteca, nombre_biblioteca, ubicacion_biblioteca])
        print("Ingresado con exito")
        
        conexion.commit()

    except Exception as error:
        print("Error al insertar datos:",error)
        conexion.rollback()
    finally:
        cursor.close()
        conexion.close()


def obtener_nombre():
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id_biblioteca, nombre FROM biblioteca ORDER BY id_biblioteca")
        nombreBiblioteca = cursor.fetchall()

        nombreDic = {nombre:id_biblioteca for id_biblioteca,nombre in nombreBiblioteca}
        return nombreDic

    except Exception as error:
        print("Error al insertar datos:",error)
        conexion.rollback()
    finally:
        cursor.close()
        conexion.close()


def nombre_biblioteca_existe(nombre_biblioteca):
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM biblioteca WHERE LOWER(nombre) = LOWER(:1)", [nombre_biblioteca])
        resultado, = cursor.fetchone()
        return resultado > 0
    except Exception as error:
        print("Error al verificar nombre:", error)
        return False
    finally:
        cursor.close()
        conexion.close()



def obtener_biblioteca():
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id_biblioteca, nombre, ubicacion FROM biblioteca ORDER BY id_biblioteca")
        bibliotecas = cursor.fetchall()
        return bibliotecas

    except Exception as error:
        print("Error al insertar datos:",error)
        conexion.rollback()
    finally:
        cursor.close()
        conexion.close()
