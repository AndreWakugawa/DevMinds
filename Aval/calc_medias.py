import statistics
#CODIGO DAS MEDIAS PARA LINKAR COM O ARQUIVO CSV

#PUXAR VARIAVEIS DE NOTA DO ARQUIVO "AVALTIME"
avaliacao = []

#PUXAR INTEGRANTES DO TIME
integrantes = []

notas_aluno1 = []
notas_aluno2 = []
notas_aluno3 = []

for pessoa in integrantes:
    if pessoa == "Aluno 1":
        notas_aluno1.append(avaliacao)
    elif pessoa == "Aluno 2":
        notas_aluno2.append(avaliacao)
    elif pessoa == "Aluno 3":
        notas_aluno3.append(avaliacao)
medias = ["media do aluno 1", "media do aluno 2", "media do aluno 3"]
media_aluno1 = statistics.mean(notas_aluno1)
media_aluno2 = statistics.mean(notas_aluno2)
media_aluno3 = statistics.mean(notas_aluno3)

for media in medias:
    aluno = int(input("Qual aluno voce deseja ver a média?\n(1) Aluno 1 (2) Aluno 2 (3) Aluno 3\n"))
    if aluno == 1:
        print (media_aluno1)
    elif aluno == 2:
        print (media_aluno2)
    elif aluno == 3:
        print (media_aluno3)
    else:
        print ("Aluno inexistente.")
