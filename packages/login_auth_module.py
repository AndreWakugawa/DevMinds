def login_check(id_user, nome):
    import os, sys, csv
    import pwinput as pw 
    filename = os.path.abspath('usersDB.csv') # Nome do arquivo

    with open(filename,'r', newline='',encoding='utf-8') as usersDB: # Abrir o arquivo para extrair logins
        reader_obj = csv.reader(usersDB, quoting=csv.QUOTE_NONE) # Cria um objeto de leitura para CSV
        print('\nBem vindo ao eVAL360!\n'
                'Antes de acessar, por favor faça seu login\n')
        email = input('Email: ')
        senha = pw.pwinput(prompt='Senha: ')
        for linha in reader_obj: #Loop até valores das colunas baterem numa linha
            if linha[3] == email and linha[4] == senha:
                id_user = linha[0] # Index id_user
                nome = linha[5] # Index nome
                usersDB.seek(0) # Reseta o pointer do arquivo para o início
                usersDB.close()
                return (id_user, nome) # Retorna info de cadastro
        usersDB.seek(0) # Reseta o pointer do arquivo para o início
        usersDB.close()
        return False