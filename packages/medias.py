import numpy as np
import csv
import os

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

def calcular_medias_times(csv_path):
    medias_times = {}

    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            id_time = int(row[2])
            notas = []
            for i in range(5, 10):
                notas.append(int(row[i]))

            if id_time not in medias_times:
                medias_times[id_time] = []

            if notas:
                medias_times[id_time].append(notas)

    for id_time, notas_times in medias_times.items():
        notas_times = np.array(notas_times)
        medias_times[id_time] = np.mean(notas_times, axis=0)

    return medias_times
