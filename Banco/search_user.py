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
