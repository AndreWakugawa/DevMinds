#Imports padrão (acompanham python)
import os
import csv
import sys
import uuid

#Imports de terceiros (precisam de pip install)
import pwinput as pw # Transforma senha em asterisco / pip install pwinput

#Imports de arquivos
from packages.login_auth_module import login_check
from packages.aval_module import aval
from packages.team_edit_modules import mudartime
from packages.dashboard_module import dash_adm
from packages.dashboard2_module import dash_times
from packages.dashboard3_module import dash_cleber
from packages.dashboard4_module import dash_user, dash_time
import packages.user_edit_modules as uc

while True:
    id_user = None
    nome = []
    login_info = login_check(id_user, nome)
    if login_info:
        id_user, nome = login_info
        file_path = os.path.abspath('usersDB.csv')

        with open(file_path, mode='r') as csv_file:
            level_reader = csv.reader(csv_file, delimiter=',')
            next(level_reader, None) # Ignora headers
            for linha in level_reader:
                if linha[0] == id_user:
                    if linha[6] == '1':
                        user_level = 1
                    elif linha[6] == '0':
                        user_level = 0  # Checa o nível do usuário
            break
    print("Dados de Login ou Senha incorretos, tente novamente")

opcoes_aluno = ['Realizar avaliação', 'Seu Dashboard', 'Sair']
opcoes_adm = ['Gerenciar cadastros', 'Realizar avaliação', 'Analisar dashboards', 'Sair']
opcoes_dash = ['Você X Time', 'Voce X Turma']
opcoes_dash_adm = ['Aluno X Turma', 'Comparação de times', 'Aluno x Time']
if user_level == 0:
    while True:
        print(f"Olá, {nome}! O que deseja fazer?\n")
        print(f"1. {opcoes_aluno[0]}\n2. {opcoes_aluno[1]}\n3. {opcoes_aluno[2]}")
        opcao = input("Insira o número da opção: ")
        if opcao == "1":
            aval(id_user, nome)
        elif opcao == "2":
            dash = input(f"1. {opcoes_dash[0]}\n2. {opcoes_dash[1]}\nInsira o número da opção: ")
            if dash == '1':
                dash_time(id_user)
            elif dash == '2':
                dash_user(id_user)
            else:
                print("Opção inválida")
        elif opcao == "3":
            sair = input("Deseja mesmo sair? (s/n)")
            if sair == "s":
                sys.exit()
        else:
            print("Opção inválida!")
elif user_level == 1:
    while True:
        print(f"Olá, {nome}! O que deseja fazer?\n")
        print(f"1. {opcoes_adm[0]}\n2. {opcoes_adm[1]}\n3. {opcoes_adm[2]}\n4. {opcoes_adm[3]}")
        opcao = input("Insira o número da opção: ")
        if opcao == "1":  #Manipulação de usuário
            opções_userM = ['Cadastrar um usuário.','Procurar um usuário pela ID.','Deletar um usuário.','Alterar a qual time um usuário está associado']
            print(f'\n{nome}, o que deseja mudar em relação aos usuários?\n')
            print (f'1.{opções_userM[0]}\n2.{opções_userM[1]}\n3.{opções_userM[2]}\n4.{opções_userM[3]}')
            opções_userSelect = int(input('\n'"Insira o número da opção:"))
            if opções_userSelect == 1:
                print('\n'"Bem vindo a função de cadastrar usuário! Se atente aos dados informados."'\n')
                uc.add_cad() # Funcao cadastro
            elif opções_userSelect == 2:
                uc.buscar_usuario() 
            elif opções_userSelect == 3:
                uc.excluir_usuario()
            elif opções_userSelect == 4:
                mudartime()
            #Fim da manipulação de usuário
        elif opcao == "2":
            aval(id_user, nome)
        elif opcao == "3":
            dash = input(f"1. {opcoes_dash_adm[0]}\n2. {opcoes_dash_adm[1]}\n3. {opcoes_dash_adm[2]}\nInsira o número da opção: ")
            if dash == '1':
                dash_adm()
            elif dash == '2':
                dash_times()
            elif dash == '3':
                dash_cleber()
            else:
                print("Opção inválida")
        elif opcao == "4":
            sair = input("Deseja mesmo sair? (s/n)")
            if sair == "s":
                sys.exit()
        else:
            print("Opção inválida!")
            break