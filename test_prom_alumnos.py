import random


#Crear el tipo de registro Alumno
class Alumno:
    def __init__(self, legajo, nombre, promedio):
        self.legajo = legajo
        self.nombre = nombre
        self.promedio = promedio

class Fixture:
    def __init__(self, equipo1, punt1, equipo2, punt2):
        self.equipo1 = equipo1
        self.punto1 = punt1
        self.equipo2 = equipo2
        self.punto2 = punt2

# Hacer una función para mostrar o armar cadena con los datos del registro
def to_string(alumno):
    resultado = " "
    resultado += "El alumno es: "
    resultado += "Legajo: " + str(alumno.legajo)
    resultado += " - Nombre: " + str(alumno.nombre)
    resultado += " - Promedio: " + str(alumno.promedio)
    return resultado

# def to_string2(alumno):
#     res = " "
#     res += "Legajo: " + str(alumno.legajo)
#     res += " - Nombre: " + str(alumno.nombre)
#     res += " - Promedio: " + str(alumno.promedio)
#     res += "\n contra\n"
#     res += "Legajo: " + str(alumno.legajo)
#     res += " - Nombre: " + str(alumno.nombre)
#     res += " - Promedio: " + str(alumno.promedio)
#     res += "\n"
#     return res


#funciones propias

def cargar_vector(v):
    for i in range(len(v)):
        #cargar datos del alumno
        legajo = random.randint(1,6)
        nombre = random.randint(1,6)
        promedio = float(input("Ingrese el promedio: "))
        #crear el alumno
        a = Alumno(legajo, nombre, promedio)
        #grabar en el vector
        v[i] = a
    return v

def mostrar_vector(v):
    for i in range(len(v)):
        #muestra cada alumno invocando a la función to_string
        print(to_string(v[i]))

def vec_fixture(v):
    posicion = len(v) - 1
    c = 0
    for i in range(len(v)):
        equipo1 = v[i].nombre
        puntos1 = random.randint(100, 600)
        equipo2 = v[posicion-c].nombre
        puntos2 = random.randint(100, 600)
        c += 1
        b = Fixture(equipo1, puntos1 ,equipo2, puntos2)
        v[i] = b
    return v

def mostrar_prom_mas_8(v):
    #recorrer el vector
    print("Alumnos con promedio mayor a 8: ")
    for i in range(len(v)):
        if v[i].promedio > 8:
            print(to_string(v[i]))

def orden_sort(vec):
    #algoritmo de selección directa
    n = len(vec)
    for i in range(n-1):
        for j in range(i+1, n):
            if vec[i].promedio > vec[j].promedio:
                vec[i], vec[j] = vec[j], vec[i]
    return vec

# def guardar(v):
#     print("Enfrentamientos")
#     n = len(v)
#     enfrentados = n * [0]
#     for i in range(n-1):
#         for j in range(-1, n):
#             if v[j].promedio > v[i].promedio:
#                 enfrentados[i], enfrentados[j] = v[j], v[i]
#     return enfrentados


def cruce(v):
    print("Enfrentamientos")
    n = len(v)//2
    posicion = len(v) - 1
    c = 0
    cruces = " "
    for i in range(n):
        cruces += str(v[i].equipo1)+" vs " + str(v[posicion-c].equipo2)
        cruces += "\n"
        c += 1
    return cruces

def ganador(fixture):
    for i in range(len(fixture)):
        pass


def contar_notas(vec):
    vc = 10 * [0]
    for i in range(vec):
        k = int(vec[i].promedio) - 1
        vc[k] += 1
    return vc


# Función principal
def test():
    #pedir la cantidad de alumnos
    n = int(input("Ingrese la cantidad de alumnos: "))
    #crear el vector de alumnos
    v = n * [None]
    #cargar los alumnos
    cargar_vector(v)
    #mostrar los alumnos
    mostrar_vector(v)
    #promedio mayor a 8
    mostrar_prom_mas_8(v)
    #Mostrar el vector ordenado
    print("Vector ordenado")
    vector_ordenado = orden_sort(v)
    mostrar_vector(vector_ordenado)

    #Mostrar el vector de conteo
    # vec_conteo = contar_notas(v)
    # mostrar_vector(vec_conteo)
    #enfrentados
    enfrentados = vec_fixture(vector_ordenado)
    octavos = fixture(enfrentados)
    print(octavos)

if __name__ == "__main__":
    test()