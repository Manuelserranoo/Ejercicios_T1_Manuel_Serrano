def invert(cadena):
    #La función invert recibe una cadena y devuelve la cadena invertida
    cadena1 = cadena[::-1]
    return cadena1

def mostrar(cadena1):
    #La función mostrar recibe una cadena y devuelve una cadena con el nombre y la nota
    lista = cadena1.split(sep=',',maxsplit=1)
    
    return lista[1] + " ha sacado un " + lista[0] + " de nota"
def main_invert():
    cadena = "zeréP nauJ,01"
    cadena2 = "zaiD sacuL,7"
    print(mostrar(invert(cadena)))
    print(mostrar(invert(cadena2)))
if __name__=="__main__":
    main_invert()