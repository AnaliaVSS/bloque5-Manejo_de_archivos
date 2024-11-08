import os

# Ruta completa al archivo libros.txt
ruta_libros = r"C:\Users\Analía\Documents\Libros\libros.txt"

# Función para buscar libros por autor
def buscar_libros_por_autor(nombre_autor):
    libros_encontrados = []

    # Verificar si el archivo libros.txt existe en la ruta especificada
    if not os.path.isfile(ruta_libros):
        print(f"El archivo {ruta_libros} no existe. Por favor, asegúrate de que la ruta es correcta.")
        return

    print("Archivo encontrado. Procediendo con la lectura...")

    # Abrir el archivo libros.txt en modo lectura
    with open(ruta_libros, "r", encoding='utf-8') as archivo:
        for linea in archivo:
            print(f"Procesando línea: {linea.strip()}")
            # Asegurarse de que la línea tenga el formato correcto
            partes = linea.strip().split(" - ")
            if len(partes) == 2:
                titulo, autor = partes
                if autor.lower() == nombre_autor.lower():
                    libros_encontrados.append(titulo)

    if libros_encontrados:
        print(f"Libros escritos por {nombre_autor}:")
        for libro in libros_encontrados:
            print(f"- {libro}")
    else:
        print(f"No se encontraron libros escritos por {nombre_autor}.")

# Solicitar al usuario que ingrese el nombre del autor
nombre_autor = input("Introduce el nombre del autor: ")

# Llamar a la función para buscar los libros por el autor
buscar_libros_por_autor(nombre_autor)

