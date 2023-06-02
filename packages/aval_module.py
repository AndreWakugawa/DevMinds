import os, csv


def aval(id_user, nome, turma_nome, sprint_atual):

    integrantes_nome = []
    integrantes_info = []
    integrantes_id = {}
    turma = []
    time = []
    inputDB = []
    
    with open('usersDB.csv', 'r', newline='', encoding='utf-8') as user_csv:
        user_reader = csv.reader(user_csv)
        next(user_reader, None)

        for linha in user_reader:
            if linha[0] == id_user:
                turma = linha[2]
                time = linha[1]
                print(f'Turma: {turma_nome}\n'
                      f'Time: {time}\n')
        user_csv.seek(0)
        for linha_integrante in user_reader:
            if linha_integrante[2] == turma and linha_integrante[1] == time:
                integrantes_info.append(linha_integrante[0])
                integrantes_nome.append(linha_integrante[5])
                integrantes_id[linha_integrante[5]] = linha_integrante[0]

        avaliacoes = []
        feedbacks = []
        fatores_chave = ["Comunicação e Trabalho em Equipe",
                        "Engajamento e Pró-atividade",
                        "Conhecimento e Aplicabilidade Técnica",
                        "Entrega de Resultados com Valor Agregado",
                        "Auto-gestão das Atividades"]
        
        escala_avaliacao = ['Insatisfatório',
                            'Abaixo das expectativas',
                            'Regular',
                            'Acima das expectativas',
                            'Excelente']

        with open('evalDB.csv', 'r',encoding='utf-8') as addID:
            readerid_aval_new = csv.reader(addID)
            id_aval_new = 0
            for idold,row in enumerate(readerid_aval_new):
                if idold == 0:
                    continue
                last_id = int(row[0])
            id_aval_new = last_id + 1
            inputDB.append(id_aval_new)
        
        print("Integrantes do Time:")

        for integrante_nome in integrantes_nome:
            if integrante_nome == nome:
                print(f'{integrante_nome} <Você>')
            else:
                print(integrante_nome)
        print()

        while True:
            integrante = input('Quem você deseja avaliar? (Deixe vazio para retornar)\n')
            pergunta = ['se avalia',
                        f'avalia {integrante}']
            
            if integrante == '':
                return

            if integrante in integrantes_nome or integrante == nome:
                user_csv.seek(0)

                for linha_integrante in user_reader:
                    feedback = ""
                    if integrante == nome:
                        pergunta_index = 0
                        print('\nVocê está se autoavaliando...\n')
                    else:
                        pergunta_index = 1

                    for fator in fatores_chave:
                        while True:
                            avaliacao = input(f'Na escala de 1 a 5 em {fator}, como você {pergunta[pergunta_index]}?\n\n'
                                              f'1 = {escala_avaliacao[0]}\n'
                                              f'2 = {escala_avaliacao[1]}\n'
                                              f'3 = {escala_avaliacao[2]}\n'
                                              f'4 = {escala_avaliacao[3]}\n'
                                              f'5 = {escala_avaliacao[4]}\n\n'
                                              )
                            try:
                                if avaliacao.isnumeric() and int(avaliacao) not in range(1, 6): # Limita valor input
                                    print("Escala incorreta\n")
                                else:
                                    break
                            except ValueError:
                                print("Valor inválido\n")
                        avaliacoes.append(int(avaliacao))

                        if int(avaliacao) in range(1,4):
                            feedback_confirm = ""

                            while feedback_confirm not in ['y']:
                                feedback = input(f"Insira um feedback de como {integrante} pode melhorar em {fator}:\n")
                                feedback_confirm = input("Você confirma o feedback?[Y/N]\n").lower()
                                if feedback_confirm != "y":
                                    print ("Tente novamente:")
                                else:
                                    feedbacks.append(feedback)

                        else:
                            feedback = ""
                            feedbacks.append(feedback)

                    inputDB.append(int(integrantes_id[integrante]))
                    inputDB.append(int(time))
                    inputDB.append(int(turma))
                    inputDB.append(sprint_atual)
                    inputDB.extend(avaliacoes)
                    inputDB.extend(feedbacks)
                    inputDB.append(id_user)
                    print("Avaliação Finalizada!!!")
                    print(f'{integrante} foi avaliado(a)!!\n{avaliacoes}')
                    break
                break
            else:
                print('Integrante não encontado, tente novamente.')
                break

    row = [str(item) for item in inputDB]

    csv_row = ','.join(row)

    with open(os.path.abspath('evalDB.csv'), 'a', newline='', encoding='utf-8') as cad_csv:
        cad_csv.write(csv_row + '\n')
