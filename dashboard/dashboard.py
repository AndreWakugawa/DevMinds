import matplotlib.pyplot as plt
import textwrap
import numpy as np
import csv
import os

from notas_alunos import obter_notas_alunos
from graficos import exibir_graficos
from medias import calcular_media_sala

csv_path = os.path.abspath('evalDB.csv')
media_sala = calcular_media_sala(csv_path)
notas_alunos = obter_notas_alunos(csv_path)

while True:

    print("\nVISUALIZAÇÃO DE DASHBOARDS\n")
    aluno_id = input("Digite o ID do aluno que deseja analisar: ")

    if aluno_id.strip() == "":
        print("ID do aluno não pode estar vazio. Por favor, digite um valor válido.")
        continue

    exibir_graficos(int(aluno_id))
    opcao = str(input('O que deseja fazer?\n'
                      '1.Visualizar outro aluno\n'
                      '2.Sair\n'
                      'Digite aqui: '))

    if opcao.strip() == "":
        print("Opção inválida. Por favor, digite um valor válido.")
        continue

    if opcao.isdigit():
        opcao = int(opcao)
        if opcao == 1:
            continue
        elif opcao == 2:
            break
        else:
            print("Opção inválida. Digite 1 para continuar ou 2 para sair.")
    else:
        print("Valor inválido.")
