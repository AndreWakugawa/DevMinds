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

def medTime(turma_escolhida):
    filename = os.path.abspath('evalDB.csv') 
    turmas = []

    with open(filename, 'r', newline='', encoding='utf-8') as usersDB:
        reader = csv.DictReader(usersDB)
        next(reader)
        for row in reader:
            id_turma = int(row['id_turma'])
            id_time = int(row['id_time'])
            criterios = [int(row[f'criterio{i}']) for i in range(1, 6)]

            if id_turma == turma_escolhida:  # Filtra apenas a turma desejada
                turma_atual = None
                for turma in turmas:
                    if turma['id_turma'] == id_turma:
                        turma_atual = turma
                        break

                if turma_atual is None:
                    turma_atual = {'id_turma': id_turma, 'times': {}}
                    turmas.append(turma_atual)

                if id_time not in turma_atual['times']:
                    turma_atual['times'][id_time] = criterios
                else:
                    turma_atual['times'][id_time] = [sum(vals) // len(vals) for vals in zip(turma_atual['times'][id_time], criterios)]

    return turmas
