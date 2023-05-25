def medTime():
    import csv
    import os

    filename = os.path.abspath('evalDB.csv') # Nome do arquivo
    notas_por_time = {}

    with open(filename, 'r', newline='', encoding='utf-8') as usersDB:
        reader = csv.DictReader(usersDB)
        next(reader)
        for row in reader:
            id_turma = int(row['id_turma'])
            id_time = int(row['id_time'])
            criterios = [int(row[f'criterio{i}']) for i in range(1, 6)]
            
            if id_turma not in notas_por_time:
                notas_por_time[id_turma] = {id_time: criterios}
            elif id_time not in notas_por_time[id_turma]:
                notas_por_time[id_turma][id_time] = criterios

    print("Notas por time e turma:")
    for turma, times in notas_por_time.items():
        for time, notas in times.items():
            print(f"Turma {turma}, Time {time}: {notas}")


medTime()