import matplotlib.pyplot as plt
import textwrap
import numpy as np
import os

from notas_alunos import obter_notas_alunos
from medias import calcular_media_sala

fatores_chave = ["Comunicação e Trabalho em Equipe",
                "Engajamento e Pró-atividade",
                "Conhecimento e Aplicabilidade Técnica",
                "Entrega de Resultados com Valor Agregado",
                "Auto-gestão das Atividades"]

def exibir_graficos(aluno_id):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    labels = [textwrap.fill(criterio, 12) for criterio in fatores_chave]

    csv_path = os.path.abspath('eValDB.csv')
    notas_alunos = obter_notas_alunos(csv_path)
    
    media_sala = calcular_media_sala(csv_path)
    cores_sala = np.where(media_sala >= 4, '#1B63AB', np.where(media_sala < 3, '#5C6065', '#1B63AB'))
    ax1.bar(labels, media_sala, color=cores_sala, alpha=0.5)
    ax1.set_ylim(0, 5)
    ax1.set_xticks(range(len(labels)))
    ax1.set_xticklabels(labels, fontsize=8)
    ax1.set_title('Média da Sala')

    if aluno_id in notas_alunos:
        notas_aluno = np.mean(notas_alunos[aluno_id]["notas"], axis=0)
        cores_aluno = np.where(notas_aluno >= 4, '#1B63AB', np.where(notas_aluno < 3, '#5C6065', '#1B63AB'))
        ax2.bar(labels, notas_aluno, color=cores_aluno, alpha=0.5)
        ax2.set_ylim(0, 5)
        ax2.set_xticks(range(len(labels)))
        ax2.set_xticklabels(labels, fontsize=8)
        ax2.set_title(f'Nota do Aluno {aluno_id}')
    else:
        ax2.text(0.5, 0.5, 'Aluno não encontrado', horizontalalignment='center', verticalalignment='center',
                 transform=ax2.transAxes, fontsize=12)

    plt.tight_layout()
    plt.show()
