# Paso 1: Crear una lista para los nombres
nombres = []
for i in range(3):
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    nombres.append(nombre)

# Paso 2: Crear una tupla para las edades
edades = tuple(int(input(f"Ingrese la edad de {nombres[i]}: ")) for i in range(3))

# Paso 3: Crear un diccionario para almacenar la información completa
estudiantes = {}
for i in range(3):
    materias_estudiante = input(f"Ingrese las materias de {nombres[i]} separadas por comas: ").split(",")
    estudiantes[nombres[i]] = {
        "edad": edades[i],
        "materias": [materia.strip() for materia in materias_estudiante]  # Limpiar espacios en blanco
    }

# Mostrar la información completa
print("\nInformación de los estudiantes:")
for nombre, info in estudiantes.items():
    print(f"Nombre: {nombre}, Edad: {info['edad']}, Materias: {', '.join(info['materias'])}")