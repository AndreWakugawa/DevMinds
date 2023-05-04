import csv
import os

# Arquivo aval.csv precisa estar na mesma pasta nesse exemplo

# CHECAR QUAL USUÁRIO É (Sistema de login?)
# E A PARTIR DISSO DEFINIR QUEM VAI SER AVALIADO (Puxando os ids do mesmo time a partir do login do usuário)


integrantes = []


# Pegar a pasta em que este script está:
script_dir = 'data_sample/'

# Identificar o caminho do csv relativo a pasta do script:
csv_path = os.path.join(script_dir, 'aval_data.csv')

# Abrir o arquivo csv para LER e extrair os usuários do time na turma (NESSE CASO SPRINT 1 DO TIME 1 DA TURMA 1!!!)
with open(csv_path, 'r') as avalcsv:
    avalread = csv.reader(avalcsv)

    # Pegar o header do csv
    header = next(avalread)

    # Definir as colunas do csv
    colunaturma = header.index('turma')
    colunatime = header.index('time')
    colunasprint = header.index('sprint')
    colunaaluno = header.index('nome')
    colunanotas = header.index('notas')

    # Pesquisar por linha
    for linha in avalread:
        # Checar igualdade entre coluna turma, time e sprint desejado, nesse caso: 1, 1 e 1
        ### !!! ENCONTRAR UM JEITO DE PEGAR O CÓDIGO DA TURMA ATRAVÉS DO USUÁRIO QUE LOGOU PARA AVALIAR !!!
        if linha[colunaturma] == "1" and linha[colunatime] == "1" and linha[colunasprint] == "1":
            # Com a igualdade, adicionar os integrantes da quinta coluna, 'aluno' (coluna 1 + 4) que forem do da turma 1, time 1
            if linha[colunaaluno] not in integrantes:
                integrantes.append(linha[colunaaluno])





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






# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# Salvando os inputs da aval dentro do aval.csv

with open(csv_path, 'r+', newline='') as avalcsv:
    avalread = csv.reader(avalcsv)
    # Carrega os dados originais do csv
    dados = [initlinha for initlinha in avalread]

    integrantesindex = 0
    notasalunoindex = 0


    notasaluno = [avalnota[notasalunoindex] for avalnota in avaliacoes]

    while notasaluno and notasalunoindex <= len(avaliacoes[0]):

    # Update dos dados dentro das condições para a add de notas
        for linha in dados:

            if linha[0] == "1" and linha[1] == "1" and linha[2] == "1":
            
                if linha[colunaaluno] == integrantes[integrantesindex]:
                # confere e remove se tiver um espaço em branco antes de add
                    notas = linha[5].strip()
                # se a celula estiver vazia add o valor
                    if notas == "":
                        notas += str(notasaluno[0])
                # se a celula estiver algo dentro, add uma virgula antes de add valor
                    else:
                        notas += "," + str(notasaluno[0])
                    if linha[5].startswith('"') and linha[5].endswith('"'):
                        pass
                    else:
                        linha[5] = notas
                # METODO pop() MARAVILHOSO QUE ENCAIXOU CERTINHO PRO QUE EU QUERIA
                    notasaluno.pop(0)
        if len(notasaluno) == 0:
            notasalunoindex += 1
            integrantesindex += 1
            if notasalunoindex >= len(avaliacoes[0]):
                break
            notasaluno = [avalnota[notasalunoindex] for avalnota in avaliacoes]

    
    # Volta ao inicio do csv para reescrever os novos dados sobre o csv original
    # A leitura estava na ultima linha do csv após a passagem do loop for
    avalcsv.seek(0)

    avalwriter = csv.writer(avalcsv)
    avalwriter.writerows(dados)

    # Remove tudo após os writes para manter o arquivo limpo
    avalcsv.truncate()
    # Fecha o open para evitar acessos concorrentes
    avalcsv.close()