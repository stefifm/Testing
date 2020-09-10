class Participantes:
    def __init__(self, nom, conti, rank):
        self.nombre = nom
        self.continente = conti
        self.ranking = rank

def to_string(participantes):
    resultado = " "
    resultado += "El participante es: "
    resultado += " - Nombre: " + participantes.nombre
    resultado += " - Continente: " + str(participantes.continente)
    resultado += " - Ranking: " + str(participantes.ranking)
    return resultado

def mostrar_participantes(participantes):
    for i in range(len(participantes)):
        #muestra cada participante invocando a la función to_string
        print(to_string(participantes[i]))

def validar_rango(inf, sup):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input("Ingrese un valor entre " + str(inf) +
                          " y " + str(sup) + ": "))
        if n < inf or n > sup:
            print("Error")
    return n

def validar(inf, sup):
    n = inf
    while n <= inf or n < sup or n > sup:
        n = int(input("Cargue la cantidad de participantes: "))
        if n <= inf or n < sup or n > sup:
            print("Error. Ingrese un número que no sea cero y no sea menor o mayor a 16.")
    return n

def linear_search(v, nombre):
    for i in range(v):
        if nombre == v[i]:
            return i
        return -1

def validar_nombre(participantes):
    n = len(participantes)
    equipos = ("Mercedes", "Red Bull", "Ferrari", "McLaren", "Williams",
               "Racing Point", "Renault", "Alpha Tauri", "Haas", "Alfa Romeo",
               "Team Penske", "Toyota Gazoo Racing", "Peugeot Sport Team",
               "Chip Ganassi Racing", "RLL Racing", "Action Express")
    print("Participantes:",equipos)
    nom = []
    for i in range(n):
        nombre = input("Ingrese el nombre del equipo: ")
        while linear_search(nom, nombre) != -1:
            nombre = input("Ese nombre ya existe. Ingrese otro: ")
        nom.append(nombre)
    return nom



def cargar_vector(participantes):
    for i in range(len(participantes)):
        # cargar datos de los participantes
        nombre = validar_nombre(participantes)
        continente = validar_rango(0, 4)
        ranking = validar_rango(1, 50)
        # crear el participante
        a = Participantes(nombre, continente, ranking)
        # grabar en el vector
        participantes[i] = a
    return participantes


def test():
    n = validar(0, 16)
    vec_participantes = [None] * n
    print("Cargue los datos de los partcipantes")
    cargar_vector(vec_participantes)
    mostrar_participantes(vec_participantes)





if __name__ == "__main__":
    test()