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
from Banco.search_user import buscar_usuario
from Banco.delete_user import excluir_usuario

while True: # Loop do login até ser valido
    id = []
    nome = []
    login_info = login_check(id, nome) # Puxa função
    if login_info: # Checa se é verdadeiro
        break
    print("Dados de Login ou Senha incorretos, tente novamente")

while True: # Loop de opções
    id, nome = login_info
    opções =['Gerenciar cadastros','Realizar avaliação','Analisar dashboards','Sair']
    
    print(f'\nOlá! {nome}, o que deseja fazer?\n')
    print (f'1.{opções[0]}\n2.{opções[1]}\n3.{opções[2]}\n4.{opções[3]}')
    
    opção = int(input("Insira o número da opção:"))
    
    if opção == 1: #Manipulação de usuário
        opções_user = ['Cadastrar um usuário.','Procurar um usuário pela ID.','Deletar um usuário.']
        print(f'\n{nome}, o que deseja mudar em relação aos usuários?\n')
        print (f'1.{opções_user[0]}\n2.{opções_user[1]}\n3.{opções_user[2]}')
        opções_userSelect = int(input("Insira o número da opção:"))
        if opções_userSelect == 1:
            print("Opção 1 escolhida")
            add_cad() # Funcao cadastro
        elif opções_userSelect == 2:
            buscar_usuario() 
        elif opções_userSelect == 3:
            excluir_usuario()
            #Fim da manipulação de usuário
    elif opção == 2:
        eval() # Funcao avaliacao
    elif opção == 3:
        print ('\nDashboards em desenvolvimento\n') # Funcao dashboards
    elif opção == 4:
        sair = input('Deseja mesmo sair?(y/n)')
        if sair in ['y']:
            sys.exit() # Termina execucao
    else:
        print('Opção inválida!')
        break