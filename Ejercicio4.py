from collections import deque


# Función para agregar tareas a la cola y mantenerla ordenada
def agregar_tarea(tarea):
    # Agregamos la tarea a la cola
    cola_tareas.append(tarea)
    # Ordenamos la cola
    cola_tareas = deque(sorted(cola_tareas))
def main_tareas():
# Agregamos algunas tareas a la cola
    agregar_tarea("Hacer la compra")
    agregar_tarea("Pagar la factura")
    agregar_tarea("Llamar al dentista")

# Imprimimos las tareas en orden
    while cola_tareas:
        cola_tareas = deque()
        tarea = cola_tareas.popleft()
        print(tarea)    

if __name__ == "__main__":
    main_tareas()
