def add_cad():
    from Main import os, sys, csv, pw, uuid # Puxa imports da main
    filename = 'login_data.csv' # Nome do arquivo
    target_dir = 'Data_Sample/' # Diretório relativo
    csv_path = os.path.join(target_dir, filename) # Seleciona diretório
    
    senha = None
    conf_senha = None
    uuidFour = uuid.uuid4()
    id = uuidFour

    # Teste para verificar se usuário digitou senha corretamente
    email = input("Insira seu e-mail: ")
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
    with open(csv_path,'a', newline='', encoding='utf-8') as cad_csv: # Abre csv, inserindo uma nova linha
        csv_writer = csv.writer(cad_csv) # Objeto de escrito do csv
        csv_writer.writerow([id, nome, email, senha])