from db.conexion_oracle import obtener_conexion




def insertar_libro(isbn, titulo, autor, ano_publicacion, biblioteca_id):
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO libro (isbn, titulo, autor, ano_publicacion, biblioteca_id)
            VALUES (:1, :2, :3, :4, :5)
        """, [isbn, titulo, autor, ano_publicacion, biblioteca_id])
        conexion.commit()
    except Exception as error:
        print("Error al insertar libro:", error)
        conexion.rollback()
    finally:
        cursor.close()
        conexion.close()