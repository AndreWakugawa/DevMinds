#Imports internos
import os
import csv
import sys

#Imports de terceiros

#imports de arquivos
from login_module import login_check
from test import aval

login_check(os, csv)

while True:
    print('\nO que deseja fazer?\n'
        '1.Gerenciar cadastros\n'
        '2.Realizar avaliação\n'
        '3.Analisar dashboards\n'
        '4.Sair\n')
    opção = int(input(''))
    if opção == 1:
        print('\nGerenciar cadastro\n') # Função cadastro
    elif opção == 2:
        aval(os, sys, csv) # Função avaliação
    elif opção == 3:
        print ('\nDashboards\n') # Função dashboards
    elif opção == 4:
        sys.exit('Adios!!') # Termina execução
    else:
        print('Opção inválida!')
        break