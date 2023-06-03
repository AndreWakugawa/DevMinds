import csv

def obter_notas_alunos(csv_path):

    notas_por_id = {}

    with open(csv_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        for row in csv_reader:
            id_aluno = int(row[1])
            time = int(row[2])
            turma = int(row[3])
            notas = [int(row[i]) if row[i] else 0 for i in range(5, 10)]

            if id_aluno in notas_por_id:
                notas_por_id[id_aluno]["notas"].append(notas)
            else:
                notas_por_id[id_aluno] = {"notas": [notas], "time": time, "turma": turma}

    return notas_por_id
