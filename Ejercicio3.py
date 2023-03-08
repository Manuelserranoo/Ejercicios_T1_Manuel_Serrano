#dadas dos listas hacer una tercera con los elementos que se repiten en ambas sin que se repitan en la tercera
def coincidencias(lista,list):
    lista3 = []
    for i in lista:
        if i in list:
            lista3.append(i)
    #eliminar los elementos repetidos de la lista3
    lista4 = []
    for i in lista3:
        if i not in lista4:
            lista4.append(i)
    return(lista4)
def main_coincidencias():
    lista1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
    lista2 = ["h",'o','l','a',' ', 'l','u','n','a']
    print("las coincidencias son",coincidencias(lista1,lista2))

if __name__ == "__main__":
    main_coincidencias()
