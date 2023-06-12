from flask import Flask, request, jsonify
from shapely.geometry import Polygon

app = Flask(__name__)

# Dicionário para armazenar os polígonos
poligonos = {}


@app.route('/poligonos', methods=['POST'])
def cadastrar_poligono():
    data = request.get_json()

    nome = data['nome']
    pontos = data['pontos']

    poligono = Polygon(pontos)
    poligonos[nome] = poligono

    return 'Polígono cadastrado com sucesso', 201


@app.route('/poligonos/<nome>', methods=['GET'])
def obter_poligono(nome):
    if nome in poligonos:
        poligono = poligonos[nome]

        num_lados = len(poligono.exterior.coords) - 1
        perimetro = poligono.length
        area = poligono.area
        num_diagonais = num_lados * (num_lados - 3) / 2
        soma_angulos_internos = (num_lados - 2) * 180

        metrics = {
            'num_lados': num_lados,
            'perimetro': perimetro,
            'area': area,
            'num_diagonais': num_diagonais,
            'soma_angulos_internos': soma_angulos_internos
        }

        return jsonify(metrics), 200
    else:
        return 'Polígono não encontrado', 404


if __name__ == '__main__':
    app.run()

#Aqui estão as principais características desta API:

#Cadastro de Polígono:

#Para cadastrar um polígono, você deve enviar uma solicitação POST para a rota /poligonos com os dados do polígono em formato JSON. Os dados devem incluir um nome e uma lista de pontos que representam as coordenadas X e Y de cada vértice do polígono.
#Extração de Métricas:

#Para obter as métricas de um polígono cadastrado, você deve enviar uma solicitação GET para a rota /poligonos/<nome>, onde <nome> é o nome do polígono desejado. As métricas retornadas incluem o número de lados, o perímetro, a área, o número de diagonais e a soma dos ângulos internos do polígono.