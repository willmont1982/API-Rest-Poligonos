import csv

def upload_csv(file):
    poligonos = {}

    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            x = float(row['x'])
            y = float(row['y'])
            nome = row['polygon_identifier']
            ordem = int(row['point_order'])

            if nome not in poligonos:
                poligonos[nome] = []

            poligonos[nome].append((x, y, ordem))

    return poligonos

#A função upload_csv recebe o caminho do arquivo CSV como parâmetro. Ela lê o arquivo e armazena as coordenadas dos pontos de múltiplos polígonos em um dicionário, onde a chave é o nome do polígono e o valor é uma lista de tuplas contendo as coordenadas X, Y e a ordem de cada ponto.

#Para usar essa função, você pode chamar o seguinte código:

arquivo_csv = 'caminho/do/arquivo.csv'
poligonos = upload_csv(arquivo_csv)

#Após a execução da função upload_csv, a variável poligonos conterá um dicionário com os polígonos
#e suas respectivas coordenadas, na forma:

{
  'triangulo': [(0.0, 0.0, 1), (1.5, 1.5, 2), (0.0, 2.0, 3)],
  'quadrado': [(0.0, 0.0, 1), (1.0, 0.0, 2), (1.0, 1.0, 3), (0.0, 1.0, 4)]
}
