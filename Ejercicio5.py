#haceer una función que reciba un numero positivo y lo descomponga en centenas, decenas y unidades
def descomponer(numero):
    centenas = numero // 100
    decenas = (numero - (centenas*100)) // 10
    unidades = numero - (centenas*100) - (decenas*10)
    return centenas,decenas,unidades

def main():
    numero = int(input("Introduce un número: "))
    centenas,decenas,unidades = descomponer(numero)
    print("El número",numero,"tiene",centenas,"centenas,",decenas,"decenas y",unidades,"unidades")


if __name__ == "__main__":
    main()