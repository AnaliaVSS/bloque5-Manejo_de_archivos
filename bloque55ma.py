from collections import Counter
import re

def contar_palabras(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            texto = f.read().lower()  # Leer todo el contenido del archivo y convertirlo a minúsculas
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe. Por favor, asegúrate de que la ruta es correcta.")
        return
    except Exception as e:
        print(f"Se produjo un error al leer el archivo: {e}")
        return

    # Utilizar una expresión regular para encontrar las palabras
    palabras = re.findall(r'\b\w+\b', texto)
    
    # Contar la frecuencia de cada palabra
    contador = Counter(palabras)
    
    # Obtener las 5 palabras más comunes
    palabras_comunes = contador.most_common(5)

    # Mostrar las palabras más comunes y su frecuencia
    for palabra, frecuencia in palabras_comunes:
        print(f"'{palabra}' aparece {frecuencia} veces")

# Llamar a la función con el nombre del archivo
nombre_archivo = "C:/Users/Analía/Documents/Bloque 5/libros.txt"
contar_palabras(nombre_archivo)