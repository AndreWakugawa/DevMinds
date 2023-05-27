import hashlib

def add_cad():
    import re,os, sys, csv
    import pwinput as pw
    csv_path = os.path.abspath('usersDB.csv') # Nome do arquivo
    
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

    # Expressão regular para validar e-mail
    email_regex = r'^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$'
    
    while True:
        email = input('\n'"Insira o e-mail do novo usuário: ")
        if re.match(email_regex, email):
            break
        else:
            print('\n'"E-mail inválido. Por favor, insira um e-mail no formato 'usuario@dominio.com'.")
        
    nome = input("Insira seu nome: ")
    while True:
        senha = pw.pwinput("Crie uma senha: ")
        conf_senha = pw.pwinput("Confirme sua senha: ")
        # Criptografia de senha vindo da hashlib.
        hashed_password = hashlib.sha256(senha.encode()).hexdigest()
        if senha == conf_senha:
            break
        else:
            print('\n'"Senha incorreta, tente novamente!")

    while True:
        turma = input('\n'"Insira a turma do aluno: ")
        if turma.isnumeric():
            turma = int(turma)
            user_level = 0
            print ('\n'"Cadastro bem sucedido!")
            break
        else:
            print('\n'"Entrada inválida. Por favor, insira um valor numérico para a turma.")

    # Inserção das variáveis dentro de uma lista

    # Sem um novo arquivo "cadastro.csv" seria criado dentro do CWD (no caso, direto no repo DevMinds).
    with open(csv_path,'a', newline='',encoding='utf-8') as cad_csv: # Abre csv, inserindo uma nova linha
        csv_writer = csv.writer(cad_csv) # Objeto de escrito do csv
        csv_writer.writerow([id, None, turma, email, hashed_password, nome, user_level])
    #evalcad() Desativado devido a alteração no banco. Aparentemente não precisa mais que a evalcad faça o trabalho. Por enquanto, é claro.

def excluir_usuario():
    import csv
    id_userDelete = input('\n'"Esta função deleta o usuário correspondente a ID informada. Prossiga com cautela, visto que nada pode ser desfeito."'\n'"Entre com a ID do usuário a ser deletado:")
    
    confirmacao = input('\n'"Deseja mesmo deletar esse usuário?(Y,N): ")

    if confirmacao == "Y" or "y":
        with open('usersDB.csv', 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = [row for row in reader if row[0] != id_userDelete]   
        with open('usersDB.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
    elif confirmacao == "N" or "n":
        print('\n'"Função encerrada"'\n')

def buscar_usuario():
    import csv
    id_userSearch = input('\n'"Está é a função de busca de usuários."'\n'"Entre com a ID do usuário que deseje buscar:")
    with open('usersDB.csv', 'r', newline='',encoding='utf-8') as f:
        reader = csv.reader(f)
        cabecalhos = next(reader)
        for row in reader:
            if row[0] == id_userSearch:
                print('\n'"Aqui estão os dados do usuário selecionado: ")
                print('\n',{cabecalhos[i]: row[i] for i in range(len(cabecalhos))})
