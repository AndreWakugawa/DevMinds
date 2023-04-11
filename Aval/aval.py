# Inserção inicial dos 5 critérios da avaliação exigidos pela PBLTeX
# Utiliza-se uma escala de 0 a 4 (5 opções)
print ("Inicia-se a avaliação 360 da sprint <sprint atual>")
print ("As notas serão de 0 a 4 sendo \n0: Insatisfatório \n1: Abaixo das expectativas \n2: Satisfatório \n3: Acima das expectativas \n4: Excelente")
#LINKAR LISTAS COM O ARQUIVO CSV > COMUNICAÇÃO, ENGAJAMENTO, CONHECIMENTO, RESULTADO E AUTOGESTÃO

# Inserção inicial dos 5 critérios da avaliação exigidos pela PBLTeX
# Utiliza-se uma escala de 0 a 4 (5 opções)

fatores_chave = ["Comunicação e Trabalho em Equipe", "Engajamento e Pró-atividade", "Conhecimento e Aplicabilidade Técnica", "Entrega de Resultados com Valor Agregado", "Auto-gestão das Atividades"]

avaliacoes = []

# Puxar ID dos integrantes pelo arquivo CSV
integrantes = ["Aluno 1", "Aluno 2", "Aluno 3"]

for fator in fatores_chave:
    print(f"AVALIAÇÃO: {fator}\n")
    avaliacoes_fator = []
    for pessoa in integrantes:
        while True:
            avaliacao = input(f"Em uma escala de 0 a 4, para {fator}, como você avalia o seu {pessoa}?\n")
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

#Review > Tudo certo com o código (Gabriel)