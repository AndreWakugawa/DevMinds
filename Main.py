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
from packages.signup_module import add_cad

while True:
    id = []
    nome = []
    login_info = login_check(id, nome)
    if login_info:
        id, nome = login_info
        file_path = os.path.abspath('data_sample/login_data.csv')

        with open(file_path, mode='r') as csv_file:
            level_reader = csv.reader(csv_file, delimiter=',')
            next(level_reader, None) # Ignora headers
            for linha in level_reader:
                if linha[0] == id:
                    if linha[4] == '1':
                        user_level = 1
                    elif linha[4] == '0':
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
            eval()
        elif opcao == "2":
            sair = input("Deseja mesmo sair? (s/n)")
            if sair == "s":
                sys.exit()
        else:
            print("Opção inválida!")
            break
elif user_level == 1:
    while True:
        print(f"Olá, {nome}! O que deseja fazer?\n")
        print(f"1. {opcoes_adm[0]}\n2. {opcoes_adm[1]}\n3. {opcoes_adm[2]}\n4. {opcoes_adm[3]}")
        opcao = input("Insira o número da opção: ")
        if opcao == "1":
            add_cad()
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