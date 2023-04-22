def login_check(os, csv):
    filename = 'cadastro.csv' # Nome do arquivo
    target_dir = 'Cadastro/' # Diretório relativo
    csv_path = os.path.join(target_dir, filename) # Seleciona diretório

    print('Bem vindo ao eVAL360!\n'
        'Antes de acessar, por favor faça seu login\n')

    with open(csv_path,'r', newline='') as cad_csv: # Abrir o arquivo para extrair logins
        reader_obj = csv.reader(cad_csv) # Cria um objeto de leitura para CSV

        while True: # Loop até login e senha = True
            email_login = input("Login: ")
            senha_login = input("Senha: ")
            for linha in reader_obj: #Loop até valores das colunas baterem numa linha
                if linha[2] == email_login and linha[3] == senha_login:
                    nome = linha[1]
                    return print('Olá!', nome) # Login bem sucedido
            print("Dados de Login ou Senha incorretos, tente novamente")            
        return False
        cad_csv.seek(0) # Reseta o pointer do arquivo para o início
    cad_csv.close()