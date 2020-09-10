import random
import test

print("Test del TP3")


def principal():
    n = 16
    participantes = [None] * n
    test.carga_automatica(participantes)
    ordenado = test.orden_sort(participantes)
    print("Lista de participantes ordenado")
    test.mostrar_participantes(ordenado)
    print("octavos\n")
    test.fixture(ordenado)
    print("Cuartos")
    test.ganadores(ordenado)
    test.cuartos(ordenado)



if __name__ == "__main__":
    principal()