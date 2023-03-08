def tareas_ordenadas(list_tareas):
    tareas = list(list_tareas.items())
    tareas.sort()
    return tareas

def main_tareas():
    list_tareas = {1:"Pasear al perro",2:"Hacer la compra",5: "Pintar el salón",3:"Lavar los platos",4:"Limpiar el baño"}
    print(tareas_ordenadas(list_tareas))

if __name__=="__main__":
    main_tareas()
    