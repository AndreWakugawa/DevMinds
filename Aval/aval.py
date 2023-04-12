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

# Abrir o arquivo csv para LER e extrair os usuários do time
with open(csv_path, 'r') as avalcsv:
    avalread = csv.reader(avalcsv)

    # Pegar o header do csv
    header = next(avalread)

    # Definir a coluna para encontrar o time
    time = "time"
    colunatime = header.index(time)

    # Pesquisar por linha
    for linha in avalread:
        # Checar igualdade entre coluna time e código desejado, nesse caso: 11
        # # !!! ENCONTRAR UM JEITO DE PEGAR O CÓDIGO DO TIME ATRAVÉS DO USUÁRIO QUE LOGOU PARA AVALIAR !!!
        if linha[colunatime] == "11":
            # Checa se o integrante já não está na lista
            if linha[colunatime + 3] not in integrantes:
                # Com a igualdade, adicionar os integrantes da quarta coluna, 'aluno' (coluna 1 + 3) que forem do time 11
                integrantes.append(linha[colunatime + 3])





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
            avaliacao = input(f"Em uma escala de 0 a 4, para {fator}, como você avalia {colega}?\n")
            try:
                avaliacao = int(avaliacao)
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