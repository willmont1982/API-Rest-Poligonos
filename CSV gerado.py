import csv

def gerar_csv():
    dados = [
        [0.0, 0.0, "triangulo", 1],
        [1.5, 1.5, "triangulo", 2],
        [0.0, 2.0, "triangulo", 3],
        [0.0, 0.0, "quadrado", 1],
        [1.0, 0.0, "quadrado", 2],
        [1.0, 1.0, "quadrado", 3],
        [0.0, 1.0, "quadrado", 4],
        [1.0, 0.0, "pentagono", 1],
        [0.30901699437494745, 0.9510565162951535, "pentagono", 2],
        [-0.8090169943749473, 0.5877852522924732, "pentagono", 3],
        [-0.8090169943749475, -0.587785252292473, "pentagono", 4],
        [0.30901699437494723, -0.9510565162951536, "pentagono", 5],
        [1.0, 0.0, "hexagono", 1],
        [0.5000000000000001, 0.8660254037844386, "hexagono", 2],
        [-0.4999999999999998, 0.8660254037844387, "hexagono", 3],
        [-1.0, 1.22, "hexagono", 4],
        [-0.5000000000000004, -0.8660254037844385, "hexagono", 5],
        [0.5000000000000001, -0.8660254037844386, "hexagono", 6]
    ]

    with open('dados_poligonos.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(['x', 'y', 'polygon_identifier', 'point_order'])
        writer.writerows(dados)

# Chamando a função para gerar o arquivo CSV
gerar_csv()

#Ao executar essa função, será gerado um arquivo chamado dados_poligonos.csv contendo os dados fornecidos no formato CSV, separados por tabulação ('\t'). 