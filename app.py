"""
App Pizza
"""
from flask import Flask, request, redirect, Response
import persistencia

#from flask import request

app = Flask(__name__)

@app.route("/pizza", methods=['POST'])
def pizza_post():
    """ Recoge el nombre y apellido, y lo envia a persistencia """
    nombre = request.form.get("nombre")
    apellidos = request.form.get("apellidos")
    print("Nombre: " + nombre)
    print("Apellidos: " + apellidos)
    persistencia.guardar_pedido(nombre, apellidos)
    return redirect("http://localhost/solicita_pedido.html", code=302)

@app.route("/checksize",methods=['POST'])
def checksize():
    """
    Comprueba disponibilidad de un tamaño de pizza.
    """
    tam = request.form.get("size")
    if tam == "S":
        mensaje = "No disponible"
    else:
        mensaje = "Disponible"
    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})
