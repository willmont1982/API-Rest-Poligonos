from flask import Flask, request, jsonify
from shapely.geometry import Polygon
import csv
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as PolygonPatch

app = Flask(__name__)

poligonos = {}


def calcular_metricas(poligono):
    num_lados = len(poligono.exterior.coords) - 1
    perimetro = poligono.length
    area = poligono.area
    num_diagonais = num_lados * (num_lados - 3) / 2
    soma_angulos_internos = (num_lados - 2) * 180

    return {
        'Número de lados': num_lados,
        'Perímetro': perimetro,
        'Área': area,
        'Número de diagonais': num_diagonais,
        'Soma dos ângulos internos': soma_angulos_internos
    }


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo foi enviado'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'Nenhum arquivo foi selecionado'}), 400

    try:
        data = file.stream.read().decode('utf-8').splitlines()
        reader = csv.DictReader(data, delimiter=';')

        for row in reader:
            x = float(row['x'])
            y = float(row['y'])
            identifier = row['polygon_identifier']
            order = int(row['point_order'])

            if identifier not in poligonos:
                poligonos[identifier] = []

            poligonos[identifier].append((x, y))

        return jsonify({'message': 'Arquivo enviado com sucesso'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/listagem', methods=['GET'])
def listagem_poligonos():
    resultado = {}

    fig, ax = plt.subplots()

    for arquivo, pontos in poligonos.items():
        poligonos_arquivo = {}
        for i, pontos_poligono in enumerate(pontos):
            nome_poligono = f'Polígono {i+1}'
            poligono = Polygon(pontos_poligono)
            metricas = calcular_metricas(poligono)

            poligonos_arquivo[nome_poligono] = metricas

            patch = PolygonPatch(poligono, alpha=0.5)
            ax.add_patch(patch)

        resultado[arquivo] = poligonos_arquivo

    ax.autoscale()
    ax.set_aspect('equal', adjustable='datalim')
    plt.show()

    return jsonify(resultado), 200


if __name__ == '__main__':
    app.run()

#Adicionamos as importações necessárias e criamos uma figura (fig) e um eixo (ax) utilizando o Matplotlib. 
#A cada iteração na rota /listagem, criamos um patch (PolygonPatch) para cada polígono e o adicionamos ao eixo ax. 
#Por fim, chamamos plt.show() para exibir o gráfico com os polígonos desenhados.