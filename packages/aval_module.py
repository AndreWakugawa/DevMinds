def aval(id_user, nome):
    import os, csv
    filename = os.path.abspath('evalDB.csv') # Nome do arquivo

    integrantes_nome = []
    integrantes_info = []
    integrantes_id = {} # dict nome:id_user
    turma = []
    time = []
    inputDB = [] #A nova linha inputada no DB. Obrigatoriamente segue a ordem dos Headers existentes lá.

    with open('usersDB.csv', 'r', newline='', encoding='utf-8') as user_csv:
        user_reader = csv.reader(user_csv)
        next(user_reader, None)

        for linha in user_reader: #Loop até valores das colunas baterem numa linha
            if linha[0] == id_user:
                turma = linha[2] # index coluna turma
                time = linha[1] # index coluna time
                print(f"\nTurma: {turma} \nTime: {time}") # Print de sua turma e time        
        user_csv.seek(0)
        for linha_integrante in user_reader:
            if linha_integrante[2] == turma and linha_integrante[1] == time: #Checa se turma e time batem
                integrantes_info.append(linha_integrante[0]) # Junta IDs em lista
                integrantes_nome.append(linha_integrante[5]) # Junta nomes em lista ???
                integrantes_id[linha_integrante[5]] = linha_integrante[0]   # Cria uma lista assim : {'Nome': 'ID'}. Exemplo {'Cleber': '2'}

            #dados = [csvlinha for csvlinha in reader_obj] # reescrita do csv dentro de lista em python
            #fb_coluna_index = 10 # Coluna inicial dos feedbacks no aval_data.csv
            #crit_coluna_index = 5 # Coluna inicial dos critérios no aval_data.csv

        avaliacoes = []
        feedbacks = []
        fatores_chave = ["Comunicação e Trabalho em Equipe",
                        "Engajamento e Pró-atividade",
                        "Conhecimento e Aplicabilidade Técnica",
                        "Entrega de Resultados com Valor Agregado",
                        "Auto-gestão das Atividades"]
        newidAval = None

        with open('evalDB.csv', 'r',encoding='utf-8') as addID:
            readeridnew = csv.reader(addID)
            idnew = 0
            for idold,row in enumerate(readeridnew):
                if idold == 0:
                    continue
                last_id = int(row[0])
            idnew = last_id + 1
            inputDB.append(idnew)

        
        
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
                user_csv.seek(0) # Retorna pointer ao inicio do csv
                for linha_integrante in user_reader: # Busca linha por linha no csv
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
                        avaliacoes.append(int(avaliacao))
                        #avaliacoes.append(avaliacao)
                        # Feedback caso a avaliação seja entre 1 e 3
                        if int(avaliacao) in range(1,4):
                            feedback_confirm = ""
                            while feedback_confirm not in ['y']:
                                feedback = input(f"Insira um feedback de como {integrante} pode melhorar em {fator}:\n")
                                feedback_confirm = input("Você confirma o feedback?(y/n)\n")
                                if feedback_confirm != "y":
                                    print ("Tente novamente:")
                                else:
                                    feedbacks.append(feedback)  # Registro do feedback
                        else:
                            feedback = None
                            feedbacks.append(feedback)# Registro do feedback vazio       
                        print(inputDB)
                        # Nos appends juntam-se as notas dadas em uma lista
                    inputDB.append(int(integrantes_id[integrante]))
                    inputDB.append(int(time))
                    inputDB.append(int(turma))
                    inputDB.append("Ainda não implementado")
                    inputDB.extend(avaliacoes) #Adição da lista avaliacoes na linha virtual.
                    inputDB.extend(feedbacks) #Adição da lista feedbackas na linha virtual.
                    print("Avaliação Finalizada!!!")
                    print(f'{integrante} foi avaliado(a)!!\n{avaliacoes}') # Visualiza notas dadas 
                    break
            else:
                print('Integrante não encontado, tente novamente.')
                break
    row = [str(item) for item in inputDB]

    # Criar uma única string com os elementos separados por vírgulas
    csv_row = ','.join(row)

    # Gravar a linha no arquivo CSV
    with open('evalDB.csv', 'a', newline='', encoding='utf-8') as cad_csv:
        cad_csv.write(csv_row + '\n')
