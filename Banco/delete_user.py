def excluir_usuario(id_user):
    import csv
    with open('dados.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row[0] != str(id_user)]
    with open('dados.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)