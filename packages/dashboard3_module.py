import numpy as np
import os
import csv
import matplotlib.pyplot as plt

from matplotlib.widgets import Button


def dash_cleber():

    def alunoxtime(csv_path, turma_escolhida, time_escolhido):

        with open(csv_path, "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)

            notas_alunos_dict = {}

            for row in csv_reader:
                id_turma = int(row[3])
                id_time = int(row[2])

                if turma_escolhida == id_turma and time_escolhido == id_time:
                    id_user = int(row[1])
                    notas = [int(row[i]) if row[i] else 0 for i in range(5, 10)]
                    notas_alunos_dict[id_user] = notas

            notas_alunos = np.array(list(notas_alunos_dict.values()))
            media_time = np.mean(notas_alunos, axis=0)

        return media_time, notas_alunos_dict

    def update_chart():

        notas_aluno = list(notas_alunos_dict.values())[current_aluno]
        for bar, nota in zip(bars_aluno, notas_aluno):
            bar.set_height(nota)
        plt.draw()

    def next_aluno(event):
      
        nonlocal current_aluno
        current_aluno = (current_aluno + 1) % num_alunos
        ax.set_title(f'Aluno {list(notas_alunos_dict.keys())[current_aluno]} x Time')
        update_chart()


    def previous_aluno(event):
    
        nonlocal current_aluno
        current_aluno = (current_aluno - 1) % num_alunos
        ax.set_title(f'Aluno {list(notas_alunos_dict.keys())[current_aluno]} x Time')
        update_chart()

    csv_path = os.path.abspath('evalDB.csv')

    while True:

        turma_escolhida = None

        while turma_escolhida is None:
            turma_input = input("Digite o número da turma (0 a 3): ")
            if not turma_input.isdigit() or int(turma_input) < 0 or int(turma_input) > 3:
                print("Turma inválida. Digite um valor numérico entre 0 e 3.")
            else:
                turma_escolhida = int(turma_input)

        time_escolhido = None

        while time_escolhido is None:
            time_input = input("Digite o número do time (1 a 4): ")
            if not time_input.isdigit() or int(time_input) < 1 or int(time_input) > 4:
                print("Time inválido. Digite um valor numérico entre 1 e 4.")
            else:
                time_escolhido = int(time_input)

        media_time, notas_alunos_dict = alunoxtime(csv_path, turma_escolhida, time_escolhido)
        num_alunos = len(notas_alunos_dict)

        barWidth = 0.25
        r1 = np.arange(len(list(notas_alunos_dict.values())[0]))

        fig, ax = plt.subplots(figsize=(16, 8))
        bars_aluno = ax.bar(r1, notas_alunos_dict[list(notas_alunos_dict.keys())[0]], color='#7D10C8', width=barWidth, label='Notas do Aluno')
        bar_time = ax.bar(r1 + barWidth, media_time, color='#561385', width=barWidth, label='Média do Time')
        ax.legend(loc='upper right', labels=['Aluno', 'Time'])
        plt.xlabel('Provas')
        plt.ylabel('Notas')
        plt.title('Comparação Aluno x Média do Time')
        plt.xticks(r1 + barWidth, ["Comunicação", "Engajamento", "Conhecimento", "Entrega", "Auto-gestão"])
        plt.ylim(0, 5)

        current_aluno = 0
        ax.set_title(f'Aluno {list(notas_alunos_dict.keys())[current_aluno]} x Time')

        ax_next_button = plt.axes([0.8, 0.05, 0.1, 0.04])
        btn_next = Button(ax_next_button, 'Próximo Aluno')
        btn_next.on_clicked(lambda event: next_aluno(event))

        ax_prev_button = plt.axes([0.1, 0.05, 0.1, 0.04])
        btn_prev = Button(ax_prev_button, 'Aluno Anterior')
        btn_prev.on_clicked(lambda event: previous_aluno(event))

        ax.set_position([0.1, 0.3, 0.6, 0.6])

        fig.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.3)

        plt.show()

        print()
        return
