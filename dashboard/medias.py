import numpy as np
import csv

def calcular_media_sala(csv_path):
    
    with open(csv_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        notas_alunos = []

        for row in csv_reader:
            notas = [int(row[i]) if row[i] else 0 for i in range(5, 10)]
            notas_alunos.append(notas)

        notas_alunos = np.array(notas_alunos)
        media_sala = np.mean(notas_alunos, axis=0)

    return media_sala
