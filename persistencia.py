"""
Persistencia
"""
def guardar_pedido(nombre, apellidos):
    """ Guarda el pedido con el nombre y apellidos """
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write("-" + nombre + " " + apellidos + "\n")
        file.close()
