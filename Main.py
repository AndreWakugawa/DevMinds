import os
import csv
import sys

from packages.login_auth_module import login_check
from packages.aval_module import aval
from packages.team_edit_modules import mudartime
from packages.turma_mgmt_module import turma_mgmt
from packages.sprint_mgmt_module import date_check
import packages.user_edit_modules as uc
import packages.sprint_mgmt_module as spr

while True:
    id_user = []
    nome = []
    turma = []
    login_info = login_check(id_user, nome, turma)

    if login_info:
        id_user, nome, turma = login_info
        file_path = os.path.abspath('usersDB.csv')

        with open(file_path, mode='r') as csv_file:
            level_reader = csv.reader(csv_file, delimiter=',')
            next(level_reader, None)

            for linha in level_reader:
                if linha[0] == id_user:
                    if linha[6] == '1':
                        user_level = 1
                    elif linha[6] == '0':
                        user_level = 0
            break

    print("Dados de Login ou Senha incorretos, tente novamente")

opcoes_aluno = ['Realizar avaliação',
                'Sair']
opcoes_adm = ['Gerenciar Cadastros',
              'Gerenciar Sprints',
              'Gerenciar Turmas',
              'Analisar Dashboards',
              'Sair']

if user_level == 0:

    while True:
        print(f"Olá, {nome}! O que deseja fazer?\n"
                        f"1.{opcoes_aluno[0]}\n"
                        f"2.{opcoes_aluno[1]}\n")
        opcao = input("Insira o número da opção: ")
        print()

        if opcao == "1":
            sprint_atual = ''
            turma_nome = ''
            sprint_info = date_check(turma, turma_nome, sprint_atual)
            
            if sprint_info:
                turma, turma_nome, sprint_atual = sprint_info
                aval(id_user, nome, turma_nome, sprint_atual)

        elif opcao == "2":
            sair = input("Deseja mesmo sair? [Y/N]").lower()

            if sair == "y":
                sys.exit()

        else:
            print("Opção inválida!")

elif user_level == 1:

    while True:
        print(f'Olá, {nome}! O que deseja fazer?\n\n'
                            f'1.{opcoes_adm[0]}\n'
                            f'2.{opcoes_adm[1]}\n'
                            f'3.{opcoes_adm[2]}\n'
                            f'4.{opcoes_adm[3]}\n'
                            f'5.{opcoes_adm[4]}\n')
        opcao = input("Insira o número da opção: ")
        print()

        if opcao == "1":
            opcoes_userMgmt = ['Cadastrar usuário.',
                                'Buscar usuário pela ID.',
                                'Apagar usuário.',
                                'Alterar time de usuário.',
                                'Voltar']
            
            print('Gerenciameto de usuário:\n')
            
            print (f'1.{opcoes_userMgmt[0]}\n'
                   f'2.{opcoes_userMgmt[1]}\n'
                   f'3.{opcoes_userMgmt[2]}\n'
                   f'4.{opcoes_userMgmt[3]}\n'
                   f'5.{opcoes_userMgmt[4]}\n')
            
            opções_userSelect = int(input("Insira o número da opção:"))
            if opções_userSelect == 1:
                uc.add_cad()

            elif opções_userSelect == 2:
                uc.buscar_usuario() 

            elif opções_userSelect == 3:
                uc.excluir_usuario()

            elif opções_userSelect == 4:
                mudartime()

            elif opções_userSelect == 5:
                print()
                continue

        elif opcao == "2":
            spr.sprint_check()

        elif opcao == "3":
            turma_mgmt()
            
        elif opcao == "4":
            print("\nDashboards em desenvolvimento\n")

        elif opcao == "5":
            sair = input("Deseja mesmo sair? [Y/N]").lower()

            if sair == "y":
                sys.exit()

        else:
            print("Opção inválida!")
            break