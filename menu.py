import Ejercicio1
import Ejercicio2
import Ejercicio3
import Ejercicio4
import Ejercicio5
import Ejercicio6
import Ejercicio7

def menu_run():
    print("Ej1.invertir cadena")
    print("Ej2.número mágico")
    print("Ej3.coincidencias en listas")
    print("Ej4.tareas")
    print("Ej5.descomposición de número")
    print("Ej6.separar lista")
    print("Ej7.agregar a lista")
    print("Salir del programa")

    while True:
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            Ejercicio1.main_invert()
        elif opcion == 2:
            Ejercicio2.main_numeros()
        elif opcion == 3:
            Ejercicio3.main_coincidencias()
        elif opcion == 4:
            Ejercicio4.main_tareas()
        elif opcion == 5:
            Ejercicio5.main_separar()
        elif opcion == 6:
            Ejercicio6.main_separarlist()
        elif opcion == 7:
            Ejercicio7.main_lista()
        elif opcion == 8:
            break
        else:
            print("Opción incorrecta")


if __name__ == "__main__":
    menu_run()