#CODIGO PARA TESTE DE MEDIAS LINKADO COM O DA AVALIAÇÃO

#LINKAR LISTAS COM O ARQUIVO CSV > COMUNICAÇÃO, ENGAJAMENTO, CONHECIMENTO, RESULTADO E AUTOGESTÃO

# Inserção inicial dos 5 critérios da avaliação exigidos pela PBLTeX
# Utiliza-se uma escala de 0 a 4 (5 opções)
import statistics
print("------AVALIAÇÃO DO TIME------\n\nAs notas serão de 0 a 4 sendo:")
print("\n0: Insatisfatório \n1: Abaixo das expectativas \n2: Satisfatório \n3: Acima das expectativas \n4: Excelente\n")

fatores_chave = ["Comunicação e Trabalho em Equipe", "Engajamento e Pró-atividade", "Conhecimento e Aplicabilidade Técnica", "Entrega de Resultados com Valor Agregado", "Auto-gestão das Atividades"]

avaliacoes = []
notas_aluno1 = []
notas_aluno2 = []
notas_aluno3 = []

# Puxar ID dos integrantes pelo arquivo CSV
integrantes = ["Aluno 1", "Aluno 2", "Aluno 3"]

for fator in fatores_chave:
    print(f"AVALIAÇÃO: {fator}\n")
    for i, pessoa in enumerate(integrantes):
        avaliacao = 10
        while avaliacao > 4:
            avaliacao = int(input(f"Em uma escala de 0 a 4, para {fator}, como você avalia o {pessoa}?\n"))
            if avaliacao > 4:
                print("Escala incorreta, por favor avalie de 0 a 4!\n")
        if i == 0:
            notas_aluno1.append(avaliacao)
        elif i == 1:
            notas_aluno2.append(avaliacao)
        else:
            notas_aluno3.append(avaliacao)

media_aluno1 = statistics.mean(notas_aluno1)
media_aluno2 = statistics.mean(notas_aluno2)
media_aluno3 = statistics.mean(notas_aluno3)

while True:
    aluno = int(input("Qual aluno você deseja ver a média?\n(1) Aluno 1 (2) Aluno 2 (3) Aluno 3\n(4) Sair\n"))
    if aluno == 1:
        print (f"A média do aluno 1 é: {media_aluno1}")
    elif aluno == 2:
        print (f"A média do aluno 2 é: {media_aluno2}")
    elif aluno == 3:
        print (f"A média do aluno 3 é: {media_aluno3}")
    elif aluno == 4:
        break
    else:
        print("Aluno inexistente.")


    fatores_chave = ["\nComunicação e Trabalho em Equipe",
                    "\nEngajamento e Pró-atividade",
                    "\nConhecimento e Aplicabilidade Técnica",
                    "\nEntrega de Resultados com Valor Agregado",
                    "\nAuto-gestão das Atividades"]
    avaliacoes = []
    integrantes = []

    for colega in integrantes: # Loop de cada fator de avaliação
        print(f"AVALIAÇÃO: {colega}\n")
        avaliacoes_fator = []
        for fator in fatores_chave: # Loop da avaliação de cada integrante
            while True:
                avaliacao = int(input(f"Em uma escala de 1 a 5 em {fator}, como você avalia {colega}?\n"))
                try:
                    if avaliacao != [1,2,3,4,5]:
                        break
                    else:
                        print("Escala incorreta, por favor avalie de 1 a 5!\n")
                except ValueError:
                    print("Valor inválido, por favor insira um número inteiro!\n")
            avaliacoes_fator.append(avaliacao)
        avaliacoes.append(avaliacoes_fator)