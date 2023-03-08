import sys
#crea una funcion que pida un numero entre 1 y 8 y devuelva el numero magico multiplicado por ese numero
def correcto(numero_usuario):
    if numero_usuario > 9:
        print("El número introducido es mayor que 9")
        sys.exit()
    elif numero_usuario < 1:
        print("El número introducido es menor que 1")
        sys.exit()
    else:
        print("El número introducido es correcto")

def new_number(numero_usuario,numero_magico):
    nuevo_numero = (9*numero_usuario)
    new_number = nuevo_numero*numero_magico
    return "El resultado es",new_number

def magicalonso():
    numero_magico = 12345679
    numero_usuario = int(input("Introduce un número entre 1 y 9: "))
    correcto(numero_usuario)
    new_number(numero_usuario,numero_magico)
    print(new_number(numero_usuario,numero_magico))

if __name__ == "__main__":
    magicalonso()

      