import matplotlib.pyplot as plt
import textwrap
import numpy as np
import csv
import os

from packages.notas_alunos_module import obter_notas_alunos
from packages.graficos_module import exibir_graficos
from packages.medias_module import calcular_media_sala


def dash_adm():

    csv_path = os.path.abspath('evalDB.csv')
    media_sala = calcular_media_sala(csv_path)
    notas_alunos = obter_notas_alunos(csv_path)

    while True:
        print("\nVISUALIZAÇÃO DE DASHBOARDS")
        id_turma = input("Digite o ID da turma que deseja ver: ")

        while True:
            if id_turma.strip() == "":
                print("ID da turma não pode estar vazio. Por favor, digite um valor válido.")
                id_turma = input("Digite o ID da turma que deseja ver: ")
                continue

            if id_turma.isdigit():
                id_turma = int(id_turma)
                break
            else:
                print("Valor inválido.")
                id_turma = input("Digite o ID da turma que deseja ver: ")

        with open('usersDB.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row['id_turma']) == id_turma:
                    print(f"{row['nome']} ({row['id_user']})")

        aluno_id = input("\nDigite o ID do aluno que deseja analisar: ")
        if aluno_id.strip() == "":
            print("ID do aluno não pode estar vazio. Por favor, digite um valor válido.")
            continue
        exibir_graficos(int(aluno_id))

        while True:
            opcao = input("\nO que deseja fazer?\n(0) Visualizar aluno\n(1) Sair\n")
            if opcao.strip() == "":
                print("Opção inválida. Por favor, digite um valor válido.")
                continue
            if opcao.isdigit():
                if opcao == '0':
                    break
                elif opcao == '1':
                    break
                else:
                    print("Opção inválida. Digite 0 para sair ou 1 para continuar.")
            else:
                print("Valor inválido.")
        
        if opcao == '1':
            break
