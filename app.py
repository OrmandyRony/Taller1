from flask import Flask, request, jsonify
import json

app = Flask(__name__)
personas = []

@app.route('/', methods=['GET'])
def inicio():
    return "Bienvenido"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=4000)