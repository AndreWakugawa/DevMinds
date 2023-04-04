email = input("Insira seu e-mail:")
password = input("Insira sua senha:")
conf_password = input("Confirme sua senha:")
lista_cadastro = []

if conf_password == password:
    print ("Registro bem sucedido!")
else:
    print ("Senha incorreta!")

lista_cadastro.append(email)
lista_cadastro.append(password)

import csv
with open("cadastro.csv","a", newline='') as csvfile:
    csvcadastro = csv.writer(csvfile)
    csvcadastro.writerow(lista_cadastro)