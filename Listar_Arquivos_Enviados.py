import json
from shapely.geometry import Polygon

def montar_json_poligonos(poligonos):
    dados_json = {}

    for arquivo, poligonos_arquivo in poligonos.items():
        dados_arquivo = []
        for nome, pontos in poligonos_arquivo.items():
            poligono = Polygon(pontos)

            num_lados = len(poligono.exterior.coords) - 1
            perimetro = poligono.length
            area = poligono.area
            num_diagonais = num_lados * (num_lados - 3) / 2
            soma_angulos_internos = (num_lados - 2) * 180

            dados_poligono = {
                'Nome': nome,
                'Número de lados': num_lados,
                'Perímetro': perimetro,
                'Área': area,
                'Número de diagonais': num_diagonais,
                'Soma dos ângulos internos': soma_angulos_internos
            }

            dados_arquivo.append(dados_poligono)

        dados_json[arquivo] = dados_arquivo

    return json.dumps(dados_json, indent=4)

#A função montar_json_poligonos recebe como parâmetro um dicionário poligonos com a estrutura de dados dos polígonos, onde as chaves do primeiro nível são os nomes dos arquivos e as chaves do segundo nível são os nomes dos polígonos.

#A função percorre o dicionário poligonos e cria um dicionário com os dados dos polígonos e suas métricas para cada arquivo. Em seguida, converte o dicionário em um formato JSON usando json.dumps() e retorna o JSON resultante.

#Para utilizar essa função, você pode chamar o seguinte código:

poligonos = {
    'arquivo1.csv': {
        'triangulo': [(0.0, 0.0), (1.5, 1.5), (0.0, 2.0)],
        'quadrado': [(0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)]
    },
    'arquivo2.csv': {
        'pentagono': [(0.0, 0.0), (1.0, 0.0), (1.5, 0.5), (1.0, 1.0), (0.0, 1.0)]
    }
}

json_resultante = montar_json_poligonos(poligonos)
print(json_resultante)

#A função `montar_json_poligonos` irá retornar uma string contendo o JSON com a listagem dos arquivos, polígonos e suas métricas correspondentes. 
#Em seguida, o código imprime o JSON resultante na tela.