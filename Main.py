#Imports padrão (acompanham python)
import os
import csv
import sys
import uuid

#Imports de terceiros (precisam de pip install)
import pwinput as pw # Transforma senha em asterisco / pip install pwinput

#Imports de arquivos
from packages.login_module import login_check
from packages.eval_module import eval
from packages.usersManipu_module import mudartime
import packages.usersChange_module as uc

while True:
    id_user = []
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

opcoes_aluno = ['Realizar avaliação', 'Sair']
opcoes_adm = ['Gerenciar cadastros', 'Realizar avaliação', 'Analisar dashboards', 'Sair']

if user_level == 0:
    while True:
        print(f"Olá, {nome}! O que deseja fazer?\n")
        print(f"1. {opcoes_aluno[0]}\n2. {opcoes_aluno[1]}")
        opcao = input("Insira o número da opção: ")
        if opcao == "1":
            eval(id_user, nome)
        elif opcao == "2":
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
            eval()
        elif opcao == "3":
            print("\nDashboards em desenvolvimento\n")
        elif opcao == "4":
            sair = input("Deseja mesmo sair? (s/n)")
            if sair == "s":
                sys.exit()
        else:
            print("Opção inválida!")
            break