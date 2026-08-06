# Manipulando chaves e valores

pessoa = {}

##
##

chave = 'nome'


pessoa[chave] = 'Rafael Alves'
lista = []


print(pessoa[chave])
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('Não Existe')
else:
    print(pessoa ['sobrenome'])

pessoa [chave] = 'Maira' 
