import matplotlib.pyplot as plt
import numpy as np
import textwrap
import csv
import os

from packages.notas_alunos_module import obter_notas_alunos


def dash_user(id_user):

    csv_path = os.path.abspath('evalDB.csv')
    fatores_chave = ["Comunicação e Trabalho em Equipe",
                    "Engajamento e Pró-atividade",
                    "Conhecimento e Aplicabilidade Técnica",
                    "Entrega de Resultados com Valor Agregado",
                    "Auto-gestão das Atividades"]
    
    id_usuario = int(id_user)

    with open('evalDB.csv', 'r') as file:
        reader = csv.DictReader(file)
        
        turma_usuario = None
        for linha in reader:
            if int(linha['id_user']) == id_usuario:
                turma_usuario = linha['id_turma']
                break
        
        file.seek(0)
        turma = []

        for row in reader:
            if row['id_turma'] == turma_usuario:
                turma.append(row)
        
        media_turma = [0, 0, 0, 0, 0]
        total_alunos = len(turma)

        for usuario in turma:
            media_turma[0] += float(usuario['criterio1'])
            media_turma[1] += float(usuario['criterio2'])
            media_turma[2] += float(usuario['criterio3'])
            media_turma[3] += float(usuario['criterio4'])
            media_turma[4] += float(usuario['criterio5'])
        
        media_turma = [round(media / total_alunos, 2) for media in media_turma]
        
        notas_usuario = []
        for usuario in turma:
            if int(usuario['id_user']) == id_usuario:
                notas_usuario = [float(usuario['criterio1']),
                                 float(usuario['criterio2']),
                                 float(usuario['criterio3']),
                                 float(usuario['criterio4']),
                                 float(usuario['criterio5'])]
                break

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

        labels = [textwrap.fill(criterio, 12) for criterio in fatores_chave]

        csv_path = os.path.abspath('evalDB.csv')
        notas_alunos = obter_notas_alunos(csv_path)

        media_sala = [float(valor) for valor in media_turma]
        cores_sala = np.where(np.array(media_sala) >= 4, '#1B63AB', np.where(np.array(media_sala) < 3, '#5C6065', '#1B63AB'))

        ax1.bar(labels, media_sala, color=cores_sala, alpha=0.5)
        ax1.set_ylim(0, 5)
        ax1.set_xticks(range(len(labels)))
        ax1.set_xticklabels(labels, fontsize=8)
        ax1.set_title('Média da Sala')

        if id_usuario in notas_alunos:
            notas_aluno = np.mean(notas_alunos[id_usuario]["notas"], axis=0)
            cores_aluno = np.where(notas_aluno >= 4, '#1B63AB', np.where(notas_aluno <= 3, '#5C6065', '#1B63AB'))

            ax2.bar(labels, notas_aluno, color=cores_aluno, alpha=0.5)
            ax2.set_ylim(0, 5)
            ax2.set_xticks(range(len(labels)))
            ax2.set_xticklabels(labels, fontsize=8)
            ax2.set_title('Você')
        else:
            ax2.text(0.5, 0.5, 'Aluno não encontrado', horizontalalignment='center', verticalalignment='center',
                    transform=ax2.transAxes, fontsize=12)

        plt.tight_layout()
        plt.show()


def dash_time(id_user):

    csv_path = os.path.abspath('evalDB.csv')
    id_user = int(id_user)

    with open(csv_path, "r") as file:
        csv_reader = csv.DictReader(file)

        user_time = None
        user_turma = None

        for linha in csv_reader:
            if int(linha['id_user']) == id_user:
                user_time = linha['id_time']
                user_turma = linha['id_turma']
                break
        
        time = 0
        file.seek(0)

        for row in csv_reader:
            if row['id_time'] == user_time and row['id_turma'] == user_turma:
                time += 1
                
        media_time = [0, 0, 0, 0, 0]
        file.seek(0)

        for row in csv_reader:
            id_time = row['id_time']
            id_turma = row['id_turma']

            if user_turma == id_turma and user_time == id_time:
                media_time[0] += float(row['criterio1'])
                media_time[1] += float(row['criterio2'])
                media_time[2] += float(row['criterio3'])
                media_time[3] += float(row['criterio4'])
                media_time[4] += float(row['criterio5'])
        media_time = [round(media / time, 2) for media in media_time]

        notas = [0, 0, 0, 0, 0]
        file.seek(0)

        for row in csv_reader:
            id_user = str(id_user)

            if id_user == row['id_user']:
                notas[0] += float(row['criterio1'])
                notas[1] += float(row['criterio2'])
                notas[2] += float(row['criterio3'])
                notas[3] += float(row['criterio4'])
                notas[4] += float(row['criterio5'])

    barWidth = 0.25
    r1 = np.arange(len(notas))

    fig, ax = plt.subplots(figsize=(16, 8))
    bar_aluno = ax.bar(r1, notas, color='#7D10C8', width=barWidth, label='Notas do Aluno')
    bar_time = ax.bar(r1 + barWidth, media_time, color='#561385', width=barWidth, label='Média do Time')
    ax.legend(loc='upper right', labels=['Aluno', 'Time'])

    plt.xlabel('Provas')
    plt.ylabel('Notas')
    plt.title('Comparação Aluno x Média do Time')
    plt.xticks(r1 + barWidth, ["Comunicação", "Engajamento", "Conhecimento", "Entrega", "Auto-gestão"])
    plt.ylim(0, 5)
    ax.set_title('Você x Time')
    ax.set_position([0.1, 0.3, 0.6, 0.6])
    fig.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.3)

    plt.show()
    return