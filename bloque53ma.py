import csv

# Datos a escribir en el archivo CSV
datos = [
    ["Titulo", "Numero de Copias"],
    ["El Quijote", 5],
    ["Cien Años de Soledad", 3],
    ["La Casa de los Espíritus", 4]
]

# Crear y escribir el archivo CSV
with open('inventario.csv', mode='w', newline='') as archivo:
    escritor_csv = csv.writer(archivo)
    escritor_csv.writerows(datos)

print("El archivo inventario.csv ha sido creado y escrito correctamente.")
