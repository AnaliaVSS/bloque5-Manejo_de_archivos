def registrar_prestamo():
    # Solicitar los datos del préstamo al usuario
    nombre_libro = input("Introduce el nombre del libro: ")
    nombre_prestatario = input("Introduce el nombre del prestatario: ")
    fecha_prestamo = input("Introduce la fecha del préstamo (DD/MM/AAAA): ")

    # Crear o abrir el archivo en modo añadir
    with open("prestamos.txt", "a") as archivo:
        # Escribir los datos del préstamo en el archivo
        archivo.write(f"Libro: {nombre_libro}, Prestatario: {nombre_prestatario}, Fecha: {fecha_prestamo}\n")

    print("El préstamo ha sido registrado correctamente.")

# Llamar a la función para registrar un préstamo
registrar_prestamo()
