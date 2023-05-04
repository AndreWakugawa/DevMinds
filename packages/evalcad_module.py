def evalcad():
    from Main import csv, sys, os

    filename_login = os.path.abspath('data_sample/login_data.csv')
    filename_aval = os.path.abspath('data_sample/aval_data.csv')

    with open(filename_login, 'r', encoding='utf-8') as f1, open(filename_aval,'r+', encoding='utf-8') as f2:
        # Lê os arquivos .csv usando a biblioteca csv
        reader1 = csv.DictReader(f1)
        reader2 = csv.DictReader(f2)

        # Cria um dicionário com os dados do último registro do arquivo login_data.csv
        last_row = None
        for row in reader1:
            last_row = row
        dict_selecionado = {'id': last_row['id'], 'nome': last_row['nome']}

        # Verifica se o usuário a ser adicionado já existe no arquivo destino
        exists = False
        for row in reader2:
            if row['id'] == dict_selecionado['id']:
                exists = True
                break
        # Adiciona uma nova linha no arquivo destino se o usuário não existir
        if not exists:
            f2.write('\n')
            writer = csv.DictWriter(f2, fieldnames=['id', 'nome'],skipinitialspace=False,lineterminator='') #Isso é o que realmente escreve no arquivo. O parâmetro 'lineterminator' é forçado com o valor nulo para não criar uma linha nova.
            writer.writerow(dict_selecionado)
            
            f2.write(',,,,,,,,,,,,,,,,,,,,,,,,,')