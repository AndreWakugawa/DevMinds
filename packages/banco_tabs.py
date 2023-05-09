import csv
#Início dados mockados
#tabela Turma
turma_data = [
    {"id_turma": "2", "id_time": "2", "turma": "Turma 1", "cargo": "Professor"},
]

#tabela Usuário
usuario_data = [
    {"id_user": "1", "id_time": "0", "id_turma": "0", "email": "aaa@adm.com", "senha": "111", "nome": "João", "ADM": "1"}
]

#tabela Avaliação
avaliacao_data = [
    {"id_avaliacao": "1", "id_turma": "2", "id_user": "2", "id_time": "2", "sprint":"3", "criterio1":"5", "criterio2":"5", "criterio3":"5", "criterio4":"5", "criterio5":"5", "fb1":"","fb2":"","fb3":"","fb4":"","fb5":""},]
#Fim dados mockados

# Criação do arquivo CSV
with open("turmasDB.csv", "w", newline="", encoding='utf-8') as f:
    # Dados da tabela Turma
    writer = csv.DictWriter(f, fieldnames=["id_turma", "id_time", "turma", "cargo"])
    writer.writeheader()
    for row in turma_data:
        writer.writerow(row)
    
    # Dados da tabela Usuário
with open ("usersDB.csv","w",newline="", encoding='utf-8') as usersDB:
    writer = csv.DictWriter(usersDB, fieldnames=["id_user","id_time","id_turma", "email", "senha", "nome", "ADM"])
    writer.writeheader()
    for row in usuario_data:
        writer.writerow(row)
    #Dados tabela Avaliação

with open("evalDB.csv", "w", newline="", encoding='utf-8') as eval:
    writer = csv.DictWriter(eval, fieldnames=["id_avaliacao", "id_turma", "id_user", "id_time", "sprint", "criterio1", "criterio2", "criterio3", "criterio4", "criterio5", "fb1","fb2","fb3","fb4","fb5"])
    writer.writeheader()
    for row in avaliacao_data:
        writer.writerow(row)


# excl. turma
    def excluir_turma(id_turma):
        with open('dados.csv', 'r', newline='') as f:
            reader = csv.reader(f)
            rows = [row for row in reader if row[0] != str(id_turma)]
        with open('dados.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
# bscr turma
    def buscar_turma(id_turma):
        with open('dados.csv', 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == str(id_turma):
                    return row
            return None
        
# add avaliação   
def adicionar_avaliacao(id_avaliacao, id_turma, id_user, nota):
    with open('dados.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([id_avaliacao, id_turma, id_user, nota])

# excl. avaliação
def excluir_avaliacao(id_avaliacao):
    with open('dados.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row[0] != str(id_avaliacao)]
    with open('dados.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

# bscr avaliação
def buscar_avaliacao(id_avaliacao):
    with open('dados.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == str(id_avaliacao):
                return row
        return None
