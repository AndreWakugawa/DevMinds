import statistics

comun1 = 3
comunn = 2
comun0 = 2
engaj1 = 4
engajn = 3
engaj0 = 3
conhec1 = 4
conhecn = 1
conhec0 = 0
result1 = 3
resultn = 2
result0 = 2
autogestao1 = 4
autogestaon = 2
autogestao0 = 1

media_aluno1 = [comun1, engaj1, conhec1, result1, autogestao1]
media_aluno2 = [comunn, engajn, conhecn, resultn, autogestaon]
media_aluno3 = [comun0, engaj0, conhec0, result0, autogestao0]

medias = [media_aluno1, media_aluno2, media_aluno3]

for i, media in enumerate(medias):
    media_aluno = statistics.mean(media)
    print(f"Média do aluno {i+1}: {media_aluno}")
