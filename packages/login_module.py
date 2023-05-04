def login_check(id, nome):
    from Main import os, sys, csv, pw # Puxa imports da main
    filename = 'login_data.csv' # Nome do arquivo
    target_dir = 'Data_Sample/' # Diretório relativo
    csv_path = os.path.join(target_dir, filename) # Seleciona diretório

    with open(csv_path,'r', newline='',encoding='utf-8') as cad_csv: # Abrir o arquivo para extrair logins
        reader_obj = csv.reader(cad_csv, quoting=csv.QUOTE_NONE) # Cria um objeto de leitura para CSV
        print('\nBem vindo ao eVAL360!\n'
                'Antes de acessar, por favor faça seu login\n')
        email = input('Email: ')
        senha = pw.pwinput(prompt='Senha: ')
        for linha in reader_obj: #Loop até valores das colunas baterem numa linha
            if linha[2] == email and linha[3] == senha:
                id = linha[0] # Index id
                nome = linha[1] # Index nome
                cad_csv.seek(0) # Reseta o pointer do arquivo para o início
                cad_csv.close()
                return (id, nome) # Retorna info de cadastro
        cad_csv.seek(0) # Reseta o pointer do arquivo para o início
        cad_csv.close()
        return False