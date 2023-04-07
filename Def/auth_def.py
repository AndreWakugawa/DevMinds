def check_csv(): #PRECISA DE IMPORT CSV
    # Abre CSV em modo de leitura (por enquanto local)
    with open('arquivolocal.csv', 'r') as file:
        
        # Cria um objeto de leitura para CSV
        csv_leitor = csv.reader(file)
        
        # Faz o loop até o usuário acertar o login
        while True:
            # Pedir input do usuário
            coluna1 = input("Login: ")
            coluna2 = input("Senha: ")
            
            # Faz o loop em cada linha do CSV
            for linha in csv_leitor:
                
                # Checa se os valores batem com ambas as colunas
                if linha[0] == coluna1 and linha[1] == coluna2:
                    return True
            
            # Caso não sucedido, pergunta por uma nova tentativa
            print("Dados de Login ou Senha incorretos, tente novamente")
        return False
        file.seek(0)  # Reseta o pointer do arquivo para o início