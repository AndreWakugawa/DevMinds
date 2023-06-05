def adicionar_turma(id_user):
    print('\n''\n'"Bem vindo à criação de time!! Entre com os dados solicitados para cadastrar um time.")
    actual_turma = input("Qual é a turma em que esse time será criado?")
    
    newTime = input("Qual será o nome do seu time?")
    import csv
    with open('usersDB.csv', 'r', newline='') as bancoCheck:
        reader = csv.reader(bancoCheck)
        for row in reader:
            if row[1] == newTime:
                