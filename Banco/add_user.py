def adicionar_usuario(id_user, email, senha, nome):
    import csv
    with open('dados.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([id_user, email, senha, nome])
#Não está sendo utilizada.