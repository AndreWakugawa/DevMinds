import os
import csv
import numpy as np
import matplotlib.pyplot as plt
from medias import calcular_medias_times

fatores_chave = ["Comunicação", "Engajamento", "Conhecimento", "Entrega", "Auto-gestão"]
num_fatores = len(fatores_chave)
csv_path = os.path.abspath('eValDB.csv')

medias_times = calcular_medias_times(csv_path)

time_1 = np.append(medias_times[1], medias_times[1][0])
time_2 = np.append(medias_times[2], medias_times[2][0])
time_3 = np.append(medias_times[3], medias_times[3][0])
time_4 = np.append(medias_times[4], medias_times[4][0])

fig, axs = plt.subplots(2, 2, figsize=(21, 9), subplot_kw={'projection': 'polar'})
theta = np.linspace(0, 2 * np.pi, num_fatores+1, endpoint=True)

colors = ['red', 'green', 'blue', 'orange']

for i, ax in enumerate(axs.flat):
    ax.plot(theta, [time_1, time_2, time_3, time_4][i], color=colors[i])
    ax.fill(theta, [time_1, time_2, time_3, time_4][i], alpha=0.4, color=colors[i])
    ax.set_xticks(theta[:-1])
    ax.set_xticklabels(fatores_chave, fontsize=8)
    ax.set_ylim(0, 5)
    ax.set_title(f'Time {i+1}')
    ax.set_theta_offset(np.pi/2) 

plt.suptitle("Comparação de Times", fontsize=16)

plt.show()
