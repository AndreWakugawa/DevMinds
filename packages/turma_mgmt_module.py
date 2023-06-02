import csv
import os


def turma_mgmt ():
    global filename
    filename = os.path.abspath('turmasDB.csv')

    with open(filename,'r', newline='',encoding='utf-8') as turmasDB:
        reader_turmas = csv.reader(turmasDB, quoting=csv.QUOTE_NONE)
        next(reader_turmas, None)
        print ("TURMAS CADASTRADAS:")
        for linha in reader_turmas:
            turmaID = linha[0]
            turmaNome = linha[1]
            print(f"| ID: {turmaID} -> Turma: '{turmaNome}'")
    print()
    opcoesTurma = ["Criar uma Turma", "Mudar nome de uma Turma", "Deletar uma Turma", "Voltar"]
    opcaoInput = int(input("O que você deseja fazer?\n"
                           f"1. {opcoesTurma[0]}\n"
                           f"2. {opcoesTurma[1]}\n"
                           f"3. {opcoesTurma[2]}\n"
                           f"4. {opcoesTurma[3]}\n"
                           "Insira o número da opção: "
                          )
                    )
    if opcaoInput == 1:
        turmaNew()
    if opcaoInput == 2:
        turmaChangeNome()
    if opcaoInput == 3:
        turmaDel()
    if opcaoInput == 4:
        print()
        return


def turmaNew():

    newTurmaNome = input("Qual o nome da nova Turma?: ")

    with open(filename,'r+', newline='',encoding='utf-8') as turmasDB:
        reader_turmas = csv.reader(turmasDB, quoting=csv.QUOTE_NONE)
        writer_turmas = csv.writer(turmasDB, quoting=csv.QUOTE_NONE)


        for linha in reader_turmas:
            if linha[1].lower() == newTurmaNome.lower():
                print(f"Turma com nome '{newTurmaNome}' já existente, retornando...\n")
                return turma_mgmt()

        turmasDB.seek(0)
        id_turma = 0

        for i,row in enumerate(reader_turmas):
            if i == 0:
                continue
            last_turma_id = int(row[0])
        id_turma = last_turma_id + 1

        newTurmaRow = [id_turma,newTurmaNome,"","",""]
        turmasDB.seek(0, 2)
        writer_turmas.writerow(newTurmaRow)
        print (f"Turma '{newTurmaNome}' criada com sucesso.\n")

    return turma_mgmt()
        

def turmaChangeNome():

    nomeTurma = input("Qual o nome da turma que deseja renomear?: ")
    with open(filename,'r+', newline='',encoding='utf-8') as turmasDB:
        reader_turmas = csv.reader(turmasDB, quoting=csv.QUOTE_NONE)
        writer_turmas = csv.writer(turmasDB, quoting=csv.QUOTE_NONE)
    
        turmas_data = [i for i in reader_turmas]
        turmasDB.seek(0)
        
        turmaEncontrada = False

        for linha in turmas_data:
            if linha[1] == nomeTurma:
                turmaEncontrada = True
                break
        if not turmaEncontrada:
            print("Turma inexistente. Retornando...\n")
            return turma_mgmt()
        
        turmaNomeUpdate = input("Qual o novo nome desejado?: ")

        for linha in turmas_data:
            if linha[1] == turmaNomeUpdate:
                print(f"Turma com nome '{turmaNomeUpdate}' já existente. Retornando...\n")
                return turma_mgmt()

        for linha in turmas_data:
            if linha[1] == nomeTurma:
                turmaNomeOrig = linha[1]
                turmaChangeNameCheck = input(f"O novo nome para '{turmaNomeOrig} será '{turmaNomeUpdate}', deseja confirmar [Y/N]?: ")
                if turmaChangeNameCheck.lower() == "y":
                    linha[1] = str(turmaNomeUpdate)

        writer_turmas.writerows(turmas_data)
        
    return turma_mgmt()


def turmaDel():

    nomeTurma = input("Qual o nome da turma que deseja deletar?: ")
    with open(filename,'r+', newline='',encoding='utf-8') as turmasDB:
        reader_turmas = csv.reader(turmasDB, quoting=csv.QUOTE_NONE)
        writer_turmas = csv.writer(turmasDB, quoting=csv.QUOTE_NONE)    

        header = next(reader_turmas)
        turmas_data = [i for i in reader_turmas]
        turmasDB.seek(0)
        
        turmaEncontrada = False

        for linha in turmas_data:
            if linha[1] == nomeTurma:
                turmaEncontrada = True
                turmas_data.remove(linha)
        if not turmaEncontrada:
            print("Turma inexistente. Retornando...\n")
            return turma_mgmt()
        
        turmasDB.truncate()
        writer_turmas.writerow(header)
        writer_turmas.writerows(turmas_data)

    return turma_mgmt()
