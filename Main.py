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
from packages.evalcad_module import evalcad

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
    
    if opção == 1:
        add_cad() # Funcao cadastro
        evalcad()
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