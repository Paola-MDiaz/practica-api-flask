from flask import Flask, jsonify, request

app = Flask(__name__)

# 1. Endpoint de Bienvenida (Root)
@app.route('/')
def home():
    return "API de Pau - Proyecto Municipal Dolores Hidalgo" # Un toque personal para tu proyecto CityExplorer

# 2. Endpoint GET con parámetros
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    # Obtener un query param si existe (ej. ?nombre=Pau)
    nombre_extra = request.args.get('nombre')
    
    user_data = {
        "id": user_id,
        "rol": "Estudiante de Software",
        "mensaje": "Datos obtenidos con éxito"
    }
    
    if nombre_extra:
        user_data["nombre_query"] = nombre_extra
        
    return jsonify(user_data), 200 # Código 200: OK

# 3. Endpoint POST para "crear" usuarios
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() # Recibe el JSON de Postman
    data["status"] = "user created"
    return jsonify(data), 201 # Código 201: Creado

if __name__ == '__main__':
    app.run(debug=True) # Modo debug para que se reinicie solo al guardar