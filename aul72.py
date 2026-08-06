# Dicionário em Python (tipo dict)
# Dicionários são estruturas de dados do tipo par de "chave" e "Valor"
# Chaves podem ser consideradas como o "índice" que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, ect.
# O valor pode ser de qualquer tipo, incluindo outro dicionário.
# Usamos as chaves - {} - ou a classe dict para criar dicionários.
# Imutáveis:  str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#       'nome' : 'Luiz Otávio',
#       'sobrenome' : 'Miranda'
#       'idade' : 18,
#       'altura' : 1.8, 
#       'enderecos' : [
#           {'rua': 'tal tal', 'número' : 123},
#           {'rua':  'outra rua', 'número' : 321}
#           {'rua':  'outra rua', 'número' : 532}
#           {'rua':  'outra rua', 'número' : 357}
#       ]
# }
#pessoa = dict(nome='Rafael Alves', sobrenome='Rafael')


pessoa = {
    'nome' : 'Rafael Alves',
    'sobrenome' : 'Neves da Silva',
    'idade' :  '32',
    'altura' : '1.7',
    'enderecos' : [
        {'rua': 'tal tal', 'número' : 123}
        ],

} 
#print(pessoa, type(pessoa))
print(pessoa['idade'])

for chave in pessoa:
    print(chave, pessoa[chave])