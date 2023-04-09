from mock_data import mock_users

# Funcao para buscar colegas de time, dado usuario
# Para visualizar use a funcao exemplo
def get_colegas_de_time(user, users = mock_users):
  return [colega for colega in users if colega["time"] == user["time"] and colega["nome"] != user["nome"]]

def example():
  resultado = [
    ["Avaliador", "Avaliados", "Time"],
    ["---------", "---------", "----"]
  ]
  for user in mock_users:
    colegas = get_colegas_de_time(user)
    resultado.append([user["nome"], [colega["nome"] for colega in colegas], user["time"]])

  # So utilizado para realizar o pretty print da matriz no exemplo
  # Fonte: https://stackoverflow.com/questions/13214809/pretty-print-2d-list
  s = [[str(e) for e in row] for row in resultado]
  lens = [max(map(len, col)) for col in zip(*s)]
  fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
  table = [fmt.format(*row) for row in s]
  print('\n'.join(table))

example()
