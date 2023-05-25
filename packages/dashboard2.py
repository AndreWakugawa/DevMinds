import os
import csv
import numpy as np
import matplotlib.pyplot as plt
from medias import medTime

fatores_chave = ["Comunicação", "Engajamento", "Conhecimento", "Entrega", "Auto-gestão"]
num_fatores = len(fatores_chave)
csv_path = os.path.abspath('eValDB.csv')

turma_escolhida = int(input("Qual turma você deseja visualizar? "))
turmas = medTime(turma_escolhida)

times_turma = None
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

