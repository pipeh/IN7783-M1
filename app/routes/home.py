from flask import Blueprint, jsonify, request

main = Blueprint('home', __name__)

@main.route('/')
def home():
    return "Servidor Flask en ejecución. Accede a /docs para ver la documentación."