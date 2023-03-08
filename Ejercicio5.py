def separar_num(num):

# Convertir el número en una cadena para poder acceder a sus caracteres individualmente
    num_str = str(num)
# Recorrer el número desde el final hacia el principio y añadir ceros en los espacios vacíos
    for i in range(len(num_str)):
        factor = num_str[len(num_str) - i - 1]
        if factor != "0":
            print(factor + "0" * i)

def main_separar():
    num = int(input("Introduce un número: "))
    print(separar_num(num))

if __name__ == "__main__":
    main_separar()