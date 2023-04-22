
    filename = 'aval.csv' # Nome do arquivo
    target_dir = 'Aval/' # Diretório relativo
    script_dir = os.path.dirname(os.path.abspath(__file__)) # Puxa a pasta
    csv_path = os.path.join(target_dir, filename) # Seleciona diretório

    # Abrir o arquivo csv para extrair os users (sprint 1 / time 1 / turma 1)
    with open(csv_path, 'r+') as aval_csv:
        reader_obj = csv.reader(aval_csv) # Cria um objeto de leitura para CSV
        header = next(reader_obj) # Pegar o header do csv

        # Definir as colunas do csv
        colunaturma = header.index('turma')
        colunatime = header.index('time')
        colunasprint = header.index('sprint')
        coluna_aluno = header.index('aluno')
        colunanotas = header.index('notas')
        
        integrantes = []

        for linha in reader_obj: # Loop até dados das colunas baterem
            ### !!! ENCONTRAR UM JEITO DE PEGAR O CÓDIGO DA TURMA ATRAVÉS DO USUÁRIO QUE LOGOU PARA AVALIAR !!!
            if linha[colunaturma] == "1" and linha[colunatime] == "1" and linha[colunasprint] == "1":
                # Com a igualdade, adicionar os integrantes da quinta coluna, 'aluno' (coluna 1 + 4) que forem do da turma 1, time 1
                if linha[coluna_aluno] not in integrantes:
                    integrantes.append(linha[coluna_aluno])


    print ("Inicia-se a avaliação 360 da sprint <sprint atual>")
    print ("As notas serão de 0 a 4 sendo \n0: Insatisfatório \n1: Abaixo das expectativas \n2: Satisfatório \n3: Acima das expectativas \n4: Excelente")
    #LINKAR LISTAS COM O ARQUIVO CSV > COMUNICAÇÃO, ENGAJAMENTO, CONHECIMENTO, RESULTADO E AUTOGESTÃO

    fatores_chave = ["\nComunicação e Trabalho em Equipe"
                    "\nEngajamento e Pró-atividade"
                    "\nConhecimento e Aplicabilidade Técnica"
                    "\nEntrega de Resultados com Valor Agregado"
                    "\nAuto-gestão das Atividades"]
    avaliacoes = []
    integrantes = []

    for fator in fatores_chave: # Loop de cada fator de avaliação
        print(f"AVALIAÇÃO: {fator}\n")
        avaliacoes_fator = []
        for colega in integrantes: # Loop da avaliação de cada integrante
            while True:
                avaliacao = int(input(f"Em uma escala de 1 a 5, para {fator}, como você avalia {colega}?\n"))
                try:
                    if avaliacao != [1,2,3,4,5]:
                        break
                    else:
                        print("Escala incorreta, por favor avalie de 1 a 5!\n")
                except ValueError:
                    print("Valor inválido, por favor insira um número inteiro!\n")
            avaliacoes_fator.append(avaliacao)
        avaliacoes.append(avaliacoes_fator)

    print ("Avaliação Finalizada!!!")
    print (avaliacoes) # Somente para visualizar os inputs salvos na variável

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    # Salvando os inputs da aval dentro do aval.csv

    with open(csv_path, 'r+', newline='') as aval_csv:
        reader_obj = csv.reader(aval_csv)

        dados = [linha for linha in reader_obj] # Carrega os dados originais do csv

        integrantes_index = 0 
        notas_aluno_index = 0 

        notas_aluno = [aval_nota[notas_aluno_index] for aval_nota in avaliacoes]

        while notas_aluno and notas_aluno_index <= len(avaliacoes[0]):

        # Update dos dados dentro das condições para a add de notas
            for linha in dados:

                if linha[0] == "1" and linha[1] == "1" and linha[2] == "1":
                
                    if linha[coluna_aluno] == integrantes[integrantes_index]:
                        notas = linha[5].strip() # Remove espaços em branco antes de add
                        if notas == "": # Se vazia add o valor a celula
                            notas += str(notas_aluno[0])
                        else: # Se preenchida, add virgula antes de add valor
                            notas += "," + str(notas_aluno[0])
                        if linha[5].startswith('"') and linha[5].endswith('"'):
                            pass
                        else:
                            linha[5] = notas
                        # METODO pop() MARAVILHOSO QUE ENCAIXOU CERTINHO PRO QUE EU QUERIA
                        notas_aluno.pop(0)

            if len(notas_aluno) == 0:
                notas_aluno_index += 1
                integrantes_index += 1
                if notas_aluno_index >= len(avaliacoes[0]):
                    break
                notas_aluno = [aval_nota[notas_aluno_index] for aval_nota in avaliacoes]

        aval_csv.seek(0) # Reseta o pointer do arquivo para o início
        aval_writer = csv.writer(aval_csv)
        aval_writer.writerows(dados)
        aval_csv.truncate() # Remove tudo após os writes para manter o arquivo limpo
        aval_csv.close() # Fecha o open para evitar acessos concorrentes