def aval(os, sys, csv):
    filename = 'aval.csv' # Nome do arquivo
    target_dir = 'Aval/' # Diretório relativo
    csv_path = os.path.join(target_dir, filename) # Seleciona diretório

    fatores_chave = ["\nComunicação e Trabalho em Equipe",
                    "\nEngajamento e Pró-atividade",
                    "\nConhecimento e Aplicabilidade Técnica",
                    "\nEntrega de Resultados com Valor Agregado",
                    "\nAuto-gestão das Atividades"]
    avaliacoes = []

    with open(csv_path, 'r+', newline='') as aval_csv:
        reader_obj = csv.reader(aval_csv, delimiter=',') # Cria um objeto de leitura para CSV
        next(reader_obj, None) # Ignora headers

        # ADICIONAR SELEÇÃO PARA AVALIAR
        print('Quem você deseja avaliar?')

        for linha in reader_obj: # Loop de cada aluno a ser avaliado
            colega = [1]
            fator = [5]
            print(f"AVALIANDO {linha[1]}\n")
            avaliacoes_fator = []
            for fator in fatores_chave: # Loop das avaliacoes de cada integrante
                while True:
                    avaliacao = int(input(f"Em uma escala de 1 a 5, para {fator}, como você avalia {colega}?\n"))
                    if 1 <= avaliacao <= 5:
                        break
                    else:
                        print("Valor inválido\n")
                return False
            avaliacoes_fator.append(avaliacao)
        avaliacoes.append(avaliacoes_fator)