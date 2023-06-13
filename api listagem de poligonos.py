#Envio de um arquivo CSV contendo as coordenadas dos pontos dos polígonos através de uma solicitação POST para a rota /upload.
#Certificar de que o arquivo CSV esteja incluído na solicitação como um campo file.
#Os pontos devem estar nas colunas 'X' e 'Y', o nome do polígono deve estar na coluna 'Nome' e a ordem do ponto na sequência do polígono deve estar na coluna 'Ordem'.
#Os polígonos serão processados e armazenados em memória para posterior análise.
#Listagem de arquivos e polígonos:

#Obter a lista de arquivos enviados através de uma solicitação GET para a rota /arquivos.
#Para cada arquivo, obter a lista de polígonos presentes através de uma solicitação GET para a rota /poligonos/<arquivo>, onde <arquivo> é o nome do arquivo desejado.
#Para cada polígono, serão exibidas as seguintes métricas: número de lados, perímetro, área, número de diagonais e soma dos ângulos internos.

from flask import Flask, request, jsonify
import csv
import math

app = Flask(__name__)
arquivos = {}

def calcular_metricas(poligono):
    num_lados = len(poligono)
    perimetro = calcular_perimetro(poligono)
    area = calcular_area(poligono)
    num_diagonais = calcular_num_diagonais(num_lados)
    soma_angulos = calcular_soma_angulos(num_lados)
    
    return {
        'numero_lados': num_lados,
        'perimetro': perimetro,
        'area': area,
        'numero_diagonais': num_diagonais,
        'soma_angulos_internos': soma_angulos
    }

def calcular_perimetro(poligono):
    perimetro = 0
    for i in range(len(poligono) - 1):
        x1, y1 = poligono[i]
        x2, y2 = poligono[i+1]
        perimetro += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return perimetro

def calcular_area(poligono):
    area = 0
    for i in range(len(poligono) - 1):
        x1, y1 = poligono[i]
        x2, y2 = poligono[i+1]
        area += (x1 * y2 - x2 * y1)
    return abs(area / 2)

def calcular_num_diagonais(num_lados):
    return int(num_lados * (num_lados - 3) / 2)

def calcular_soma_angulos(num_lados):
    return (num_lados - 2) * 180

@app.route('/upload', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    arquivo = request.files['file']
    if arquivo.filename == '':
        return jsonify({'error': 'Nome de arquivo inválido'}), 400

    try:
        leitor_csv = csv.reader(arquivo)
        poligonos = []
        for linha in leitor_csv:
            pontos = [(float(linha[i]), float(linha[i+1])) for i in range(0, len(linha), 2)]
            poligonos.append(pontos)

        arquivos[arquivo.filename] = poligonos
        return jsonify({'message': 'Arquivo enviado com sucesso'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/arquivos', methods=['GET'])
def listar_arquivos():
    return jsonify(list(arquivos.keys())), 200

@app.route('/arquivos/<nome_arquivo>', methods=['GET'])
def listar_poligonos(nome_arquivo):
    if nome_arquivo in arquivos:
        poligonos = arquivos[nome_arquivo]
        lista_metricas
@app.route('/arquivos/<nome_arquivo>', methods=['GET'])
def listar_poligonos(nome_arquivo):
    if nome_arquivo in arquivos:
        poligonos = arquivos[nome_arquivo]
        lista_metricas = []
        for poligono in poligonos:
            metricas = calcular_metricas(poligono)
            lista_metricas.append(metricas)
        return jsonify(lista_metricas), 200
    else:
        return jsonify({'error': 'Arquivo não encontrado'}), 404
    
   
