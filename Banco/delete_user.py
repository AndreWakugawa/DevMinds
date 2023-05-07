def excluir_usuario():
    import csv
    id_userDelete = input('\n'"Esta função deleta o usuário correspondente a ID informada. Prossiga com cautela, visto que nada pode ser desfeito."'\n'"Entre com a ID do usuário a ser deletado:")
    
    confirmacao = input('\n'"Deseja mesmo deletar esse usuário?(Y,N): ")

    if confirmacao == "Y":
        with open('usersDB.csv', 'r', newline='', encoding='utf8') as f:
            reader = csv.reader(f)
            rows = [row for row in reader if row[0] != id_userDelete]   
        with open('usersDB.csv', 'w', newline='', encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
    elif confirmacao == "N":
        print('\n'"Função encerrada"'\n')