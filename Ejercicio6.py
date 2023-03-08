def separar_lista(lista):
    lista1 = []
    lista2 = []
    for i in lista:
        if i%2 ==0:
            lista1.append(i)
        else:
            lista2.append(i)
    return lista1, lista2
def main_separar():
    lista = [1,2,3,4,5,6,7,8,9,10]
    lista1, lista2 = separar_lista(lista)
    print("Lista de números pares: ",lista1)
    print("Lista de números impares: ",lista2)
if __name__=="__main__":
    main_separar()