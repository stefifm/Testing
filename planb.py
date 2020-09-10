import random

class Participantes:
    def __init__(self, nom, conti, rank, punt):
        self.nombre = nom
        self.continente = conti
        self.ranking = rank
        self.puntos = punt


def to_string(participantes):
    r = " "
    r += "Nombre: " + participantes.nombre
    r += "- Continente: " + str(participantes.continente)
    r += "- Ranking: " + str(participantes.ranking)
    r += "- Puntos: " + str(participantes.puntos)
    return r

def mostrar_participantes(participantes):
    for i in range(len(participantes)):
        print(to_string(participantes[i]))

def buscar_nombre(nombre, participantes):
    for registro in participantes:
        if registro.nombre == nombre:
            return True
    return False


nom = ("Mercedes", "Red Bull", "Ferrari", "McLaren", "Williams",
           "Racing Point", "Renault", "Alpha Tauri", "Haas", "Alfa Romeo",
           "Team Penske", "Toyota Gazoo Racing", "Peugeot Sport Team",
           "Chip Ganassi Racing", "RLL Racing", "Action Express")
def carga_automatica(participantes):
    for i in range(16):
        nombre = random.choice(nom)
        while buscar_nombre(nombre, participantes):
            nombre = random.choice(nom)

        continente = random.randint(0, 4)
        ranking = random.randint(1, 70)
        puntos = random.randint(100, 1000)
        participantes.append(Participantes(nombre, continente, ranking,
                                            puntos))


def orden_sort(participantes):
    # algoritmo de selección directa
    n = len(participantes)
    for i in range(n-1):
        for j in range(i+1, n):
            if participantes[i].ranking > participantes[j].ranking:
                participantes[i], participantes[j] = participantes[j], \
                                                     participantes[i]
    return participantes


# generación de cruces
def octavos(participantes):
    n = len(participantes) // 2
    posicion = len(participantes) - 1
    c = 0
    for i in range(n):
        p1 = participantes[i].nombre
        participantes[i].puntos = random.randint(100, 1000)
        p2 = participantes[posicion-c].nombre
        participantes[posicion - c].puntos = random.randint(100, 1000)
        c += 1
        print(p1, participantes[i].puntos, "vs", p2, participantes[posicion
                                                                   - c].puntos)



def ganadores(participantes):
    n = len(participantes) // 2
    ronda = []
    posicion = len(participantes) - 1
    c = 0
    for i in range(n):
        participantes[i].puntos = random.randint(100, 1000)
        participantes[posicion-c].puntos = random.randint(100, 1000)
        if participantes[i].puntos > participantes[posicion-c].puntos:
            ronda.append(participantes[i])
        else:
            ronda.append(participantes[posicion-c])
        c += 1
    return ronda

def final(participantes):
    n = len(participantes) // 2
    # ronda = []
    posicion = len(participantes) - 1
    c = 0
    for i in range(n):
        participantes[i].puntos = random.randint(100, 1000)
        participantes[posicion-c].puntos = random.randint(100, 1000)
        if participantes[i].puntos > participantes[posicion-c].puntos:
            ganador = participantes[i]
            segundo = participantes[posicion-c]
        else:
            ganador = participantes[posicion-c]
            segundo = participantes[i]
        c += 1
        return ganador, segundo






def cruces(participantes):
    n = len(participantes) // 2
    posicion = len(participantes) - 1
    c = 0
    for i in range(n):
        c += 1
        print(participantes[i].nombre, participantes[i].puntos, "vs",
              participantes[posicion-c].nombre, participantes[posicion-c].puntos)