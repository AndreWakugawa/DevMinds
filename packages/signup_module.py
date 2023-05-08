def add_cad():
    import re,os, sys, csv
    import pwinput as pw
    from packages.evalcad_module import evalcad
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
        email = input("Insira o e-mail do novo usuário: ")
        if re.match(email_regex, email):
            break
        else:
            print("E-mail inválido. Por favor, insira um e-mail no formato 'usuario@dominio.com'.")
        
    nome = input("Insira seu nome: ")
    while True:
        senha = pw.pwinput("Crie uma senha: ")
        conf_senha = pw.pwinput("Confirme sua senha: ")
        if senha == conf_senha:
            print ("Cadastro bem sucedido!")
            break
        else:
            print("Senha incorreta, tente novamente!")

    # Inserção das variáveis dentro de uma lista

    # Sem um novo arquivo "cadastro.csv" seria criado dentro do CWD (no caso, direto no repo DevMinds).
    with open(csv_path,'a', newline='',encoding='utf-8') as cad_csv: # Abre csv, inserindo uma nova linha
        csv_writer = csv.writer(cad_csv) # Objeto de escrito do csv
        csv_writer.writerow([id, email, senha, nome])
    #evalcad() Desativado devido a alteração no banco. Aparentemente não precisa mais que a evalcad faça o trabalho. Por enquanto, é claro.