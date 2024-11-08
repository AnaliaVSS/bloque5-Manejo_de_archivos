def mostrar_prestamos():
    with open("C:/Users/Analía/Documents/Bloque 5/Prestamos.txt","r") as archivo:
        prestamos = archivo.readlines()
    
    if not prestamos:
        print("No hay registros de préstamos.")
        return None,
    
    for i, prestamo in enumerate(prestamos, start=1):
        print(f"{i}. {prestamo.strip()}")

    return prestamos

def eliminar_prestamo():
    prestamos = mostrar_prestamos()
    if prestamos is None:
        return
    
    try:
        num_a_eliminar = int(input("Introduce el número del préstamo que deseas eliminar: "))
        if num_a_eliminar < 1 or num_a_eliminar > len(prestamos):
            print("Número inválido.")
            return
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número.")
        return
    
    prestamo_eliminar = prestamos.pop(num_a_eliminar - 1)
    print(f"Eliminando el préstamo: {prestamo_eliminar.strip()}")
    
    with open('prestamos.txt', 'w') as archivo:
        archivo.writelines(prestamos)
    
    print("El archivo ha sido actualizado.")

# Llamar a la función para eliminar un préstamo
eliminar_prestamo()