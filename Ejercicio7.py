def agregar_una_vez(lista, el):
    try:
        if el in lista:
            raise ValueError(f"Error: Imposible añadir elementos duplicados => {el}.")
        else:
            lista.append(el)
    except ValueError as ve:
        print(ve)


def main_lista():
    lista = [1, 5, -2]
    agregar_una_vez(lista, 10)
    agregar_una_vez(lista, -2)
    agregar_una_vez(lista, "Hola")
    print(lista)

if __name__ == "__main__":
    main_lista()
