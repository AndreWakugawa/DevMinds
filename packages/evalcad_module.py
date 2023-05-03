def evalcad():
    from Main import csv, sys, os

    filename = 'login_data.csv'
    target_dir = 'data_sample/'
    csv_path = os.path.join(target_dir, filename)
    csv_path2 = os.path.join(target_dir, 'aval_data.csv')

    with open(csv_path, 'r', encoding='utf-8') as f1, open(csv_path2,'r+', encoding='utf-8') as f2:
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