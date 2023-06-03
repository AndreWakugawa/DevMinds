import csv


def level(file_path, id):

    with open(file_path, mode='r') as csv_file:
        level_reader = csv.reader(csv_file, delimiter=',')
        next(level_reader, None)

        for linha in level_reader:
            print(linha[0] + ',' + id)
            if linha[0] == id:
                if linha[4] == '1':
                    return 1
                elif linha[4] == '0':
                    return 0
            break
        else:
            print("Dados de Login ou Senha incorretos, tente novamente")
