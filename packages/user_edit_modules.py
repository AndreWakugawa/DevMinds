import re,os,csv
import pwinput as pw


def add_cad():

    csv_path = os.path.abspath('usersDB.csv')
    senha = None
    conf_senha = None

    with open(csv_path, 'r',newline='',encoding='utf-8') as banco:
        reader = csv.reader(banco)
        id = 0
        for i,row in enumerate(reader):
            if i == 0:
                continue
            last_id = int(row[0])
        id = last_id + 1

    email_regex = r'^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$'
    
    while True:
        email = input("\nInsira o e-mail do novo usuário: ")

        if re.match(email_regex, email):
            break
        else:
            print("\nE-mail inválido. Por favor, tente novamente.")
        
    nome = input("Insira seu nome: ")

    while True:
        senha = pw.pwinput("Crie uma senha: ")
        conf_senha = pw.pwinput("Confirme sua senha: ")
        if senha == conf_senha:
            break
        else:
            print("\nSenha incorreta, tente novamente!")

    while True:
        turma = input('\nInsira a turma do aluno: ')
        if turma.isnumeric():
            turma = int(turma)
            user_level = 0
            print ("\nCadastro bem sucedido!")
            break
        else:
            print("\nEntrada inválida. Por favor, insira um valor numérico para a turma.")

    with open(csv_path,'r+', newline='',encoding='utf-8') as cad_csv:
        csv_writer = csv.writer(cad_csv)
        cad_csv.seek(0, 2)
        csv_writer.writerow([id, None, turma, email, senha, nome, user_level])


def excluir_usuario():

    id_userDelete = input('ATENÇÃO!!\n'
                        'Usuários apagados terão seus dados perdidos permanentemente!!'
                        'Entre com a ID do usuário a ser deletado: ')
    
    confirmacao = input("\nDeseja mesmo deletar esse usuário? [Y,N]: ").lower()

    if confirmacao == "y":
        with open('usersDB.csv', 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = [row for row in reader if row[0] != id_userDelete]   
        with open('usersDB.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
    elif confirmacao == "n":
        print("\nFunção encerrada\n")


def buscar_usuario():

    id_userSearch = input("\nInsira a ID do usuário:\n")

    with open('usersDB.csv', 'r', newline='',encoding='utf-8') as f:
        reader = csv.reader(f)
        cabecalhos = next(reader)
        
        for row in reader:
            if row[0] == id_userSearch:
                print('\n'"Aqui estão os dados do usuário selecionado: ")
                print('\n',{cabecalhos[i]: row[i] for i in range(len(cabecalhos))})
    
