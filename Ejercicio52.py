tareas = []

def agregar_tarea(nombre, prioridad):
    tareas.append({
        "nombre": nombre,
        "prioridad": prioridad,
        "completada": False
    })

def completar_tarea(nombre):
    for tarea in tareas:
        if tarea["nombre"] == nombre:
            tarea["completada"] = True

def eliminar_tarea(nombre):
    for tarea in tareas:
        if tarea["nombre"] == nombre:
            tareas.remove(tarea)

agregar_tarea("Estudiar Python", 1)
agregar_tarea("Hacer tarea", 2)
agregar_tarea("Leer libro", 3)

completar_tarea("Estudiar Python")

tareas.sort(key=lambda x: x["prioridad"])

for tarea in tareas:
    print(tarea)