import os
import numpy as np
import matplotlib.pyplot as plt

from packages.medias_module import medTime


def dash_times():

    fatores_chave = ["Comunicação", "Engajamento", "Conhecimento", "Entrega", "Auto-gestão"]
    num_fatores = len(fatores_chave)
    csv_path = os.path.abspath('evalDB.csv')

    while True:
        turma_escolhida = None
        while turma_escolhida is None:
            turma_input = input("Digite o número da turma (1 a 4): ")
            if not turma_input.isdigit() or int(turma_input) < 1 or int(turma_input) > 4:
                print("Turma inválida. Digite um valor numérico entre 1 e 4.")
            else:
                turma_escolhida = int(turma_input)
                turmas = medTime(turma_escolhida)

        for turma in turmas:
            if turma['id_turma'] == turma_escolhida:
                times_turma = turma['times']
                break

        if times_turma is not None:
            times = []
            for time_id, time_data in times_turma.items():
                times.append(np.append(time_data, time_data[0]))

            fig, axs = plt.subplots(2, 2, figsize=(21, 9), subplot_kw={'projection': 'polar'})
            theta = np.linspace(0, 2 * np.pi, num_fatores+1, endpoint=True)

            colors = ['red', 'green', 'blue', 'orange']

            for i, ax in enumerate(axs.flat):
                ax.plot(theta, times[i], color=colors[i])
                ax.fill(theta, times[i], alpha=0.4, color=colors[i])
                ax.set_xticks(theta[:-1])
                ax.set_xticklabels(fatores_chave, fontsize=8)
                ax.set_ylim(0, 5)
                ax.set_title(f'Time {i+1}')
                ax.set_theta_offset(np.pi/2) 

            plt.suptitle(f"Comparação de Times - Turma {turma_escolhida}", fontsize=16)

            plt.show()
        else:
            print("Turma não encontrada.")

        print()
        return
