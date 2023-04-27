import csv
import pandas as pd

#tabela Turma
turma_data = [
    {"id_turma": 2, "time": "Time A", "turma": "Turma 1", "cargo": "Professor"},
]

#tabela Usuário
usuario_data = [
    {"id_user": 2, "email": "email@test.com", "senha": "senha", "nome": "João"},
]

#tabela Avaliação
avaliacao_data = [
    {"id_avaliacao": 2, "id_turma": 1, "id_user": 1, "nota": 8.5},
]

# Criação do arquivo CSV
with open("dados.csv", "w", newline="") as f:
    # Dados da tabela Turma
    writer = csv.DictWriter(f, fieldnames=["id_turma", "time", "turma", "cargo"])
    writer.writeheader()
    for row in turma_data:
        writer.writerow(row)
    
    # Dados da tabela Usuário
    writer = csv.DictWriter(f, fieldnames=["id_user", "email", "senha", "nome"])
    writer.writeheader()
    for row in usuario_data:
        writer.writerow(row)
    
    # Dados da tabela Avaliação
    writer = csv.DictWriter(f, fieldnames=["id_avaliacao", "id_turma", "id_user", "nota"])
    writer.writeheader()
    for row in avaliacao_data:
        writer.writerow(row)

# add turma
    def adicionar_turma(id_turma, time, turma, cargo):
        with open('dados.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([id_turma, time, turma, cargo])
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
        
# add usuario
def adicionar_usuario(id_user, email, senha, nome):
    with open('dados.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([id_user, email, senha, nome])

# excl. usuario
def excluir_usuario(id_user):
    with open('dados.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row[0] != str(id_user)]
    with open('dados.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

# bscr usuario
def buscar_usuario(id_user):
    with open('dados.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == str(id_user):
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