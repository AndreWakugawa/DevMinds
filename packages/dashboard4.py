import matplotlib.pyplot as plt
import textwrap
import pwinput as pw 
import numpy as np
import csv
import os

from notas_alunos import obter_notas_alunos
from medias import calcular_media_sala

fatores_chave = ["Comunicação e Trabalho em Equipe",
                "Engajamento e Pró-atividade",
                "Conhecimento e Aplicabilidade Técnica",
                "Entrega de Resultados com Valor Agregado",
                "Auto-gestão das Atividades"]
def obter_notas_alunos(csv_path, id_aluno):
    notas_por_id = {}
    turma_aluno = None

    with open(csv_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        for row in csv_reader:
            id_aluno_csv = int(row[1])
            time = int(row[2])
            turma = int(row[3])
            notas = [int(row[i]) if row[i] else 0 for i in range(5, 10)]

            if id_aluno_csv == id_aluno:
                turma_aluno = turma

            if turma == turma_aluno:
                if id_aluno_csv in notas_por_id:
                    notas_por_id[id_aluno_csv]["notas"].append(notas)
                else:
                    notas_por_id[id_aluno_csv] = {"notas": [notas], "time": time, "turma": turma}

    return notas_por_id

id_aluno = int(input("ID: "))

csv_path = os.path.abspath('evalDB.csv')
notas_por_id = obter_notas_alunos(csv_path, id_aluno)

print(notas_por_id)