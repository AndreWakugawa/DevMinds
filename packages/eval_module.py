def eval():
    from Main import os, sys, csv, id, nome # Puxa imports da main
    filename = os.path.abspath('evalDB.csv') # Nome do arquivo

    with open(filename, 'r+', newline='',encoding='utf-8') as aval_csv:
        reader_obj = csv.reader(aval_csv, delimiter=',') # Cria um objeto de leitura para CSV

        dados = [csvlinha for csvlinha in reader_obj] # reescrita do csv dentro de lista em python
        fb_coluna_index = 10 # Coluna inicial dos feedbacks no aval_data.csv
        crit_coluna_index = 5 # Coluna inicial dos critérios no aval_data.csv
        aval_csv.seek(0)

        next(reader_obj, None) # Ignora headers

        avaliacoes = []
        fatores_chave = ["Comunicação e Trabalho em Equipe",
                        "Engajamento e Pró-atividade",
                        "Conhecimento e Aplicabilidade Técnica",
                        "Entrega de Resultados com Valor Agregado",
                        "Auto-gestão das Atividades"]
        
        id_coluna_index = 0
        for linha in reader_obj: #Loop até valores das colunas baterem numa linha
            if linha[id_coluna_index] == id:
                turma = linha[2] # index coluna turma
                time = linha[3] # index coluna time
                print(f"\nTurma: {turma} \nTime: {time}") # Print de sua turma e time

                integrantes_nome = []
                integrantes_info = []
                integrantes_id = {} # dict nome:id_user
                
                aval_csv.seek(0)
                for linha_integrante in reader_obj:
                    if linha_integrante[2] == turma and linha_integrante[3] == time: #Checa se turma e time batem
                        integrantes_info.append(linha_integrante) # Junta nomes em lista
                        integrantes_nome.append(linha_integrante[1])
                        integrantes_id[linha_integrante[1]] = linha_integrante[0]

        print("\nIntegrantes do Time:")
        for integrante_nome in integrantes_nome: # Print dos integrantes do time
            if integrante_nome == nome:
                print(f'{integrante_nome} <Você>')
            else:
                print(integrante_nome)

        while True:
            integrante = input('\nQuem você deseja avaliar?\n')
            pergunta = ['se avalia',f'avalia {integrante}']
            if integrante in integrantes_nome or integrante == nome: # Verifica há o integrante no time
                avaliacoes_fator = []
                aval_csv.seek(0) # Retorna pointer ao inicio do csv
                for linha_integrante in reader_obj: # Busca linha por linha no csv
                    feedback = ""
                    if integrante == nome: # Verifica se o nome é do próprio usuário
                        pergunta_index = 0
                        print('\nAUTOAVALIAÇÃO\n')
                    else:
                        pergunta_index = 1
                    for fator in fatores_chave: # Loop das avaliacoes de cada integrante
                        while True: # Faz loop até finalizar avaliação
                            avaliacao = input(f"Na escala de 1 a 5 em {fator}, como você {pergunta[pergunta_index]}?\n")
                            try:
                                if avaliacao.isnumeric() and int(avaliacao) not in range(1, 6): # Limita valor input
                                    print("Escala incorreta\n")
                                else:
                                    break
                            except ValueError:
                                print("Valor inválido\n")  
                        # Feedback caso a avaliação seja entre 1 e 3
                        if int(avaliacao) in range(1,4):
                            feedback_confirm = ""
                            while feedback_confirm not in ['y']:
                                feedback = input(f"Insira um feedback de como {integrante} pode melhorar em {fator}:\n")
                                feedback_confirm = input("Você confirma o feedback?(y/n)\n")
                                if feedback_confirm != "y":
                                    print ("Tente novamente:")
                        # Registro do feedback
                        for i, csvlinha in enumerate(dados):
                            if csvlinha[id_coluna_index] == integrantes_id[integrante] and fb_coluna_index <=14:
                                reg = csvlinha[fb_coluna_index]
                                if reg == "":
                                    dados[i][fb_coluna_index] = feedback
                                else:
                                    if feedback != "":
                                        dados[i][fb_coluna_index] = f'{dados[i][fb_coluna_index]},{feedback}'
                        feedback = ""
                        fb_coluna_index += 1
                        # Nos appends juntam-se as notas dadas em uma lista
                        avaliacoes_fator.append(avaliacao)
                    avaliacoes.append(avaliacoes_fator)
                    print("Avaliação Finalizada!!!")
                    print(f'{integrante} foi avaliado(a)!!\n{avaliacoes}') # Visualiza notas dadas 
                    break
            else:
                print('Integrante não encontado, tente novamente.')
                break

        aval_csv.seek(0)
        avalwriter = csv.writer(aval_csv)
        avalwriter.writerows(dados)
        # Remove tudo após os writes para manter o arquivo limpo
        aval_csv.truncate()
        #Avaliação terminada, falta adicao de notas ao csv