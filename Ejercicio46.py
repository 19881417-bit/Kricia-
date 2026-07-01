agenda = {}

def agregar(nombre, telefono):
    agenda[nombre] = telefono

def buscar(nombre):
    if nombre in agenda:
        print(agenda[nombre])
    else:
        print("No encontrado")

def eliminar(nombre):
    if nombre in agenda:
        del agenda[nombre]
        print("Eliminado")
    else:
        print("No existe")

agregar("Ana", "1234")
buscar("Ana")
eliminar("Ana")