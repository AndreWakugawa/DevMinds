import csv
import os

# Arquivo aval.csv precisa estar na mesma pasta nesse exemplo

# CHECAR QUAL USUÁRIO É (Sistema de login?)
# E A PARTIR DISSO DEFINIR QUEM VAI SER AVALIADO (Puxando os ids do mesmo time a partir do login do usuário)


integrantes = []


# Pegar a pasta em que este script está:
script_dir = os.path.dirname(os.path.abspath(__file__))

# Identificar o caminho do csv relativo a pasta do script:
csv_path = os.path.join(script_dir, 'aval.csv')

# Abrir o arquivo csv para LER e extrair os usuários do time na turma (NESSE CASO TIME 1 DA TURMA 1!!!)
with open(csv_path, 'r') as avalcsv:
    avalread = csv.reader(avalcsv)

    # Pegar o header do csv
    header = next(avalread)

    # Definir a coluna para encontrar a turma
    turma = "turma"
    colunaturma = header.index(turma)

    # Pesquisar por linha
    for linha in avalread:
        # Checar igualdade entre coluna turma e código desejado, nesse caso: 1; E chega time e código desejado, nesse caso também 1
        ### !!! ENCONTRAR UM JEITO DE PEGAR O CÓDIGO DA TURMA ATRAVÉS DO USUÁRIO QUE LOGOU PARA AVALIAR !!!
        if linha[colunaturma] == "1" and linha[colunaturma + 1] == "1":
            # Com a igualdade, adicionar os integrantes da quinta coluna, 'aluno' (coluna 1 + 4) que forem do da turma 1, time 1
            if linha[colunaturma + 4] not in integrantes:
                integrantes.append(linha[colunaturma + 4])





print ("Inicia-se a avaliação 360 da sprint <sprint atual>")
print ("As notas serão de 0 a 4 sendo \n0: Insatisfatório \n1: Abaixo das expectativas \n2: Satisfatório \n3: Acima das expectativas \n4: Excelente")
#LINKAR LISTAS COM O ARQUIVO CSV > COMUNICAÇÃO, ENGAJAMENTO, CONHECIMENTO, RESULTADO E AUTOGESTÃO

# Inserção inicial dos 5 critérios da avaliação exigidos pela PBLTeX
# Utiliza-se uma escala de 0 a 4 (5 opções)

fatores_chave = ["Comunicação e Trabalho em Equipe", "Engajamento e Pró-atividade", "Conhecimento e Aplicabilidade Técnica", "Entrega de Resultados com Valor Agregado", "Auto-gestão das Atividades"]

avaliacoes = []

for fator in fatores_chave:
    print(f"AVALIAÇÃO: {fator}\n")
    avaliacoes_fator = []
    for colega in integrantes:
        while True:
            avaliacao = int(input(f"Em uma escala de 0 a 4, para {fator}, como você avalia {colega}?\n"))
            try:
                if 0 <= avaliacao <= 4:
                    break
                else:
                    print("Escala incorreta, por favor avalie de 0 a 4!\n")
            except ValueError:
                print("Valor inválido, por favor insira um número inteiro!\n")
        avaliacoes_fator.append(avaliacao)
    avaliacoes.append(avaliacoes_fator)

print ("Avaliação Finalizada!!!")

# Somente para visualizar os inputs salvos na variável
print (avaliacoes)