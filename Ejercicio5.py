import sys

def descomposicion(num):
    unidades = num % 10
    decenas = (num // 10) % 10
    centenas = (num // 100) % 10
    miles = (num // 1000) % 10
    return miles, centenas, decenas, unidades

if len(sys.argv) == 2:
    try:
        num = int(sys.argv[1])
        if num > 0:
            miles, centenas, decenas, unidades = descomposicion(num)
            print("{:04d}".format(unidades))
            print("{:04d}".format(decenas * 10))
            print("{:04d}".format(centenas * 100))
            print("{:04d}".format(miles * 1000))
        else:
            print("El número debe ser positivo.")
    except ValueError:
        print("El argumento debe ser un número entero.")
else:
    print("Este script necesita un argumento, que debe ser un número entero positivo.")

def main():
    num = int(input("Introduce un número: "))
    print(descomposicion(num))

if __name__ == "__main__":
    main()