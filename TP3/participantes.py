import random

print("Para la carga de los participantes")

class Participantes:
    def __init__(self, nom, conti, rank):
        self.nombre = nom
        self.continente = conti
        self.ranking = rank


def to_string(participantes):
    r = " "
    r += "Nombre: " + participantes.nombre
    r += " - Continente: " + str(participantes.continente)
    r += " - Ranking: " + str(participantes.ranking)
    r += "\n"
    return r



#------------------------------------------------------------------------------
def mostrar_participantes(participantes):
    for i in range(len(participantes)):
        print(to_string(participantes[i]))


def buscar_nombre(nom, participantes):
    for reg in participantes:
        if reg.nombre == nom:
            return True
    return False

def validar(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print("Error. El valor debe ser mayor a cero")
    return n

def validar_rango(inf, sup, mensaje):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("Valor no válido. Ingrese un valor entre",str(inf),"y",
                  str(sup))
    return n

#Carga manual del vector
def carga_manual(participantes):
    for i in range(16):
        nombre = input("Ingrese el nombre de los participantes: ")
        while buscar_nombre(nombre, participantes):
            nombre = input("Ingrese el nombre de los participantes: ")
        continente = validar_rango(0, 4, "Ingrese el continente [0-América. "
                                         "1-Europa. 2-Asia. 3-África. "
                                         "4-Oceanía")
        ranking = validar_rango(1, 70, "Ingrese el ranking: ")
        reg1 = Participantes(nombre, continente, ranking)
        participantes.append(reg1)

#carga automática

def carga_automatica(participantes):
    nom = ("Mercedes", "Red Bull", "Ferrari", "McLaren", "Williams",
           "Racing Point", "Renault", "Alpha Tauri", "Haas", "Alfa Romeo",
           "Team Penske", "Toyota Gazoo Racing", "Peugeot Sport Team",
           "Chip Ganassi Racing", "RLL Racing", "Action Express")
    for i in range(16):
        nombre = random.choice(nom)
        while buscar_nombre(nombre, participantes):
            nombre = random.choice(nom)
        continente = random.randint(0, 4)
        ranking = random.randint(1, 70)
        reg1 = Participantes(nombre, continente, ranking)
        participantes.append(reg1)


#ordenamiento de mayor a menor
def orden_sort(participantes):
    # algoritmo de selección directa
    n = len(participantes)
    for i in range(n-1):
        for j in range(i+1, n):
            if participantes[i].ranking < participantes[j].ranking:
                participantes[i], participantes[j] = participantes[j], \
                                                     participantes[i]

#Estadística participante por continente
def estadistica_continente(participantes):
    conteo_continente = [0] * 16
    for i in range(len(participantes)):
        cont = int(participantes[i].continente)
        conteo_continente[cont] += 1
    for i in range(16):
        if conteo_continente[i] != 0:
            print("Continente:",i,"Cantidad de participantes:",
                  conteo_continente[i])

#------------------------------------------------------------------------------
class Fixture:
    def __init__(self, participantes, punt):
        self.nombre = participantes.nombre
        self.puntos = punt

def to_string_fixture(fixture):
    r = " "
    r += "Nombre: " + fixture.nombre
    r += " - Puntos: " + str(fixture.puntos)
    return r


#generar el fixture
def fixture(fixture):
    n = len(fixture) // 2
    posicion = len(fixture) - 1
    c = 0
    for i in range(n):
        fixture[i].puntos = random.randint(100, 1000)
        fixture[posicion - c].puntos = random.randint(100, 1000)
        e1 = Fixture(fixture[i],fixture[i].puntos)
        e2 = Fixture(fixture[posicion-c], fixture[posicion - c].puntos)
        c += 1
        print(to_string_fixture(e1), "vs", to_string_fixture(e2))



def ganador(fixture):
    n = len(fixture) // 2
    posicion = len(fixture) - 1
    c = 0
    ronda = []
    for i in range(n):
        if fixture[i].puntos > fixture[posicion-c].puntos:
            ronda.append(fixture[i])
        else:
            ronda.append(fixture[posicion-c])
        c += 1
    return ronda

def final(fixture):
    n = len(fixture) // 2
    posicion = len(fixture) - 1
    c = 0
    ronda_final = []
    for i in range(n):
        if fixture[i].puntos > fixture[posicion - c].puntos:
            ronda_final.append(fixture[i])
        else:
            ronda_final.append(fixture[posicion - c])
        c += 1
    return ronda_final

def tercer(fixture):
    n = len(fixture) // 2
    posicion = len(fixture) - 1
    c = 0
    ronda_tercero = []
    for i in range(n):
        if fixture[i].puntos < fixture[posicion - c].puntos:
            ronda_tercero.append(fixture[i])
        else:
            ronda_tercero.append(fixture[posicion - c])
        c += 1
    return ronda_tercero

def estadistica_promedio_ronda(fixture):
    suma = 0
    contador = 0
    for reg in fixture:
        suma += reg.puntos
        contador += 1
    prom = round(suma / contador, 2)
    print("\nEl promedio de la ronda es de:",prom)


#------------------------------------------------------------------------------
def top2(final):
    posicion = len(final) - 1
    c = 0
    for i in range(len(final)):
        if final[i].puntos > final[posicion - c].puntos:
            ganador = final[i]
            segundo = final[posicion-c]
        else:
            ganador = final[posicion-c]
            segundo = final[i]
        c += 1
        return ganador, segundo

def tercero(ter):
    posicion = len(ter) - 1
    c = 0
    for i in range(len(ter)):
        if ter[i].puntos > ter[posicion - c].puntos:
            tercer_lugar = ter[i]
        else:
            tercer_lugar = ter[posicion-c]
        c += 1
        return tercer_lugar

#------------------------------------------------------------------------------
def nuevo_arreglo(pri, seg, ter, participantes):
    pri.ranking += 25
    seg.ranking += 15
    ter.ranking += 5
    return participantes