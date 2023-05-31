import datetime as d
import csv
import os
from datetime import timedelta
from packages.aval_module import aval


def sprint_check():

    global filename
    filename = os.path.abspath('turmasDB.csv') # Nome do arquivo

    with open(filename,'r+', newline='',encoding='utf-8') as turmasDB:
        global reader_turmas
        reader_turmas = csv.reader(turmasDB, quoting=csv.QUOTE_NONE)
        writer_turmas = csv.writer(turmasDB, quoting=csv.QUOTE_NONE)
        next(reader_turmas, None)
        print ("TURMAS CADASTRADAS:")
        for linha in reader_turmas:
            turmaID = linha[0]
            turmaNome = linha[1]
            print(f"| ID: {turmaID} -> Turma: '{turmaNome}'")        
        print()
        turma = int(input("Qual o id da Turma que deseja gerenciar as Sprints?: "))
        turmasDB.seek(0)
        for linha in reader_turmas:
            if str(turma) == str(linha[0]):
                turma_nome = linha [1]
                print (f"Você está configurando a turma '{turma_nome}'.\n")
                if linha[4].strip() == "":
                    turmasDB.seek(0)
                    print ("A configuração inicial das Sprints ainda não foi realizada. Vamos prosseguir com ela.\n")
                    sprint_init_cfg(turma, turmasDB, reader_turmas, writer_turmas)
                    print (f"As Sprints foram configuradas para a turma '{turma_nome}'.\n")
                    break
                elif linha[4].strip() is not None:
                    turmasDB.seek(0)
                    edit_check = input("A configuração inicial já foi realizada, você deseja adicionar Sprints? [Y/N]").lower()
                    if edit_check == "y":
                        sprint_edit(turma, turmasDB, reader_turmas, writer_turmas, turma_nome)
                        return
                    else:
                        print("Retornando...")
                        return
        else:
            print("Turma não registrada. Retornando...")
            return


def sprint_init_cfg(turma, turmasDB, reader_turmas, writer_turmas):
    
    sprint_confirm = ''

    while sprint_confirm != "y":
        sprint_init_date_input = input("Digite a data inicial da Sprint no formato [AAAA-MM-DD].\n")
        ano, mes, dia = map(int, sprint_init_date_input.split('-'))
        sprint_init_date = d.date(ano, mes, dia)

        while sprint_init_date <= d.date.today():
            sprint_init_date_input = input("Data inválida. Digite uma nova data a partir de amanhã [AAAA-MM-DD]\n")
            ano, mes, dia = map(int, sprint_init_date_input.split('-'))
            sprint_init_date = d.date(ano, mes, dia)
        sprint_init_date = d.datetime.combine(sprint_init_date, d.time(23, 59, 59))
        sprint_len = input("Digite a duração da Sprint em dias.\n")
        sprint_qtd = input("Digite a quantidade de Sprints desejada.\n")
        sprint_confirm = input("Confirme os dados:\n"
                                f"A data inicial da Sprint foi definida para: {sprint_init_date}\n"
                                f"A duração das Sprints foi definida para: {sprint_len} dias.\n"
                                f"A quantia total de Sprints foi definida em: {sprint_qtd} Sprints.\n"
                                "Você deseja prosseguir com essa configuração? [Y/N]: "
                                ).lower()
        
    turmas_data = [i for i in reader_turmas]

    for linha in turmas_data:
        if str(turma) == linha[0]:
            linha[2] = sprint_init_date
            linha[3] = sprint_len
            linha[4] = sprint_qtd

    turmasDB.seek(0)
    writer_turmas.writerows(turmas_data)


def sprint_edit(turma, turmasDB, reader_turmas, writer_turmas, turma_nome):

    turmas_data = [i for i in reader_turmas]

    for linha in turmas_data:
        if str(turma) == linha[0]:
            sprints_orig = linha[4]

    print (f"A quantidade atual de Sprints definidas em '{turma_nome}' é de: {sprints_orig} Sprints.\n")
    sprint_add_check = input("Você deseja adicionar Sprints? [Y/N]: ").lower()

    if sprint_add_check == "y":
        sprints_add = (input(f"Quantas Sprints você deseja adicionar às {sprints_orig} Sprints originais?: "))
        sprints_new = int(sprints_orig) + int(sprints_add)

        for linha in turmas_data:
            if str(turma) == linha[0]:
                linha[4] = str(sprints_new)
                
    turmasDB.seek(0)
    writer_turmas.writerows(turmas_data)
    print (f"Configuração bem-sucedida, o novo total de Sprints para '{turma_nome}' é de: {sprints_new} Sprints.\n")
    
    return


def date_check(turma, turma_nome, sprint_atual):

    filename = os.path.abspath('turmasDB.csv') # Nome do arquivo

    with open(filename,'r+', newline='',encoding='utf-8') as turmasDB:
        reader_turmas = csv.reader(turmasDB, quoting=csv.QUOTE_NONE)
        next(reader_turmas, None)
        
        sprint_atual = 1
        hoje_today = d.datetime.today()
        
        for linha in reader_turmas:
            if turma == linha[0]:
                turma_nome = linha[1]
                sprint_init = d.datetime.strptime(linha[2], '%Y-%m-%d %H:%M:%S')
                sprint_length = int(linha[3])
                sprint_qtd = int(linha[4])
        
        sprint_end = sprint_init + timedelta(days=sprint_length)
        sprint_counter = 0
        sprint_end_timebox = sprint_end + timedelta(days=5)

        while sprint_counter <= sprint_qtd:
            while hoje_today > sprint_end_timebox:
                sprint_end = sprint_end + timedelta(days=sprint_length)
                sprint_end_timebox = sprint_end + timedelta(days=5)
                sprint_atual += 1
            sprint_counter += 1

        if sprint_atual > sprint_qtd:
            return print('Todas as sprints foram finalizadas! Retornando...\n')
        
        elif hoje_today < sprint_end or hoje_today > sprint_end_timebox:
            print(f'Não é possível realizar avaliações da Sprint {sprint_atual}!!',
                  f'\nPeríodo avaliativo:',
                  f'\nDe {sprint_end} até {sprint_end_timebox}\n')
            return False
        
        print(f'Iniciando avaliação da Sprint {sprint_atual}')
        return (turma, turma_nome, sprint_atual)
    