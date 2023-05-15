def mudartime():
    import csv
    
    while True:
        id_userChange = input('\n'"Informe a ID do aluno que deseja mudar o time: ")
        timenovo = input('\n'"Informe o novo time do aluno: ")
        if id_userChange.isdigit() and timenovo.isdigit():
            break
        else:
            print('\n'"A ID informada não existe, ou o valor do time  informado não é um numero")
    
    with open('usersDB.csv', 'r', newline='', encoding='utf-8') as usersDB:
        linhas_nova = []
        reader = csv.DictReader(usersDB)
        next(reader)
        for row in reader:
            if row['id_user'] == id_userChange:
                row['id_time'] = timenovo
                linhas_nova.append(row)
                
    with open('usersDB.csv', 'r', newline='', encoding='utf-8') as usersDB:
        reader = csv.reader(usersDB)
        rows = [row for row in reader if row[0] != id_userChange] 
    with open('usersDB.csv', 'w', newline='', encoding='utf-8') as usersDB:
        writer = csv.writer(usersDB)
        writer.writerows(rows)

    with open('usersDB.csv', 'a', newline='', encoding='utf-8') as bdnovo:

        campos = ['id_user','id_time','id_turma','email','senha','nome','user_level']

        writer = csv.DictWriter(bdnovo, fieldnames=campos)
        for row in linhas_nova:
            writer.writerow(row)