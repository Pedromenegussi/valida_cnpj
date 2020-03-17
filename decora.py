from time import sleep
#lista = [146, 7,742, 2, 1, 6,32,51, 3, 4, 50, 0, 91]
"""bubble sort
ordenado = False
while not ordenado:
    ordenado = True
    for x in range(len(lista)-1):
        if lista[x] > lista[x+1]:
            lista[x], lista[x+1] = lista[x+1], lista[x]
            ordenado = False
            print(lista)
"""

lista = [146, 7,742, 2, 1, 6,32,51, 3, 4, 50, 0, 91]
ordenado = False
while not ordenado:
    ordenado = True
    for i in range(len(lista) -1):
        if lista[i] == lista[i]:
            aux = lista[i]
            if aux >= lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
            elif aux < lista[i+1]:
                aux = lista[i+1]
                ordenado = False
    print(lista)
