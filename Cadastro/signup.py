def add_cad():
    # Teste para verificar se usuário digitou senha corretamente
    email = input("Insira seu e-mail:")
    while password != conf_password:
        print ("Senha incorreta, tente novamente!")
        password = input("Insira sua senha:")
        conf_password = input("Confirme sua senha:")
    else:
        print ("Cadastro bem sucedido!")

    # Inserção das variáveis dentro de uma lista
    lista_cadastro = []
    lista_cadastro.append(email)
    lista_cadastro.append(password)

    # Biblioteca 'csv' para manipulação de arquivos .csv
    # Biblioteca 'os' para manipulação de pastas dentro do windows
    # Biblioteca 'sys' para o algoritmo encontrar o arquivo "cadastro.csv" dentro da própria pasta em que está sendo executado.
    

    # Abertura do arquivo "cadastro.csv" e inserção da lista 'lista_cadastro' em uma nova linha.
    # Importante ressaltar o argumento "newline='' " para impedir a criação de linhas vazias dentro do arquivo .csv.
    # O uso da biblioteca 'os' com 'sys' faz com que o algoritmo atualize o arquivo "cadastro.csv" dentro da pasta,
    # Sem eles um novo arquivo "cadastro.csv" seria criado dentro do CWD (no caso, direto no repo DevMinds).
    with open(os.path.join(sys.path[0],"cadastro.csv"),"a", newline='') as csvfile:
        csvcadastro = csv.writer(csvfile)
        csvcadastro.writerow(lista_cadastro)