def login_check(id, nome):
    import os, sys, csv
    import pwinput as pw 
    filename = os.path.abspath('usersDB.csv') # Nome do arquivo

    with open(filename,'r', newline='',encoding='utf-8') as cad_csv: # Abrir o arquivo para extrair logins
        reader_obj = csv.reader(cad_csv, quoting=csv.QUOTE_NONE) # Cria um objeto de leitura para CSV
        print('\nBem vindo ao eVAL360!\n'
                'Antes de acessar, por favor faça seu login\n')
        email = input('Email: ')
        senha = pw.pwinput(prompt='Senha: ')
        for linha in reader_obj: #Loop até valores das colunas baterem numa linha
            if linha[1] == email and linha[2] == senha:
                id = linha[0] # Index id
                nome = linha[3] # Index nome
                cad_csv.seek(0) # Reseta o pointer do arquivo para o início
                cad_csv.close()
                return (id, nome) # Retorna info de cadastro
        cad_csv.seek(0) # Reseta o pointer do arquivo para o início
        cad_csv.close()
        return False