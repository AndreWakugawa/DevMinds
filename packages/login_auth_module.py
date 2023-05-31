import os, csv
import pwinput as pw


def login_check(id_user, nome, turma):


    with open(os.path.abspath('usersDB.csv'),'r', newline='',encoding='utf-8') as usersDB:
        reader_obj = csv.reader(usersDB, quoting=csv.QUOTE_NONE)
        print('\nBem vindo ao eVAL360!\n'
                'Antes de acessar, por favor faça seu login\n')
        email = input('Email: ')
        senha = pw.pwinput(prompt='Senha: ')

        for linha in reader_obj:
            if linha[3] == email and linha[4] == senha:
                id_user = linha[0]
                turma = linha[2]
                nome = linha[5]
                usersDB.seek(0)
                usersDB.close()
                return (id_user, nome, turma)
        
        usersDB.seek(0)
        usersDB.close()

        return False
    