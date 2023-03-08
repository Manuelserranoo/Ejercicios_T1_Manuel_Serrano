#dadas dos listas hacer una tercera con los elementos que se repiten en ambas sin que se repitan en la tercera
def main():
    lista1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
    lista2 = ["h",'o','l','a',' ', 'l','u','n','a']
    lista3 = []
    for i in lista1:
        if i in lista2:
            lista3.append(i)
    #eliminar los elementos repetidos de la lista3
    lista4 = []
    for i in lista3:
        if i not in lista4:
            lista4.append(i)
    print(lista4)

if __name__ == "__main__":
    main()
