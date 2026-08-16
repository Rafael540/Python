# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy
produtos = [
    {'nome' : 'Produto 5', 'preco' : 10.00},
    {'nome' : 'Produto 1', 'preco' : 22.32},
    {'nome' : 'Produto 3', 'preco' : 10.11},
    {'nome' : 'Produto 2', 'preco' : 105.87},
    {'nome' : 'Produto 4', 'preco' : 69.90}
]

produtos_copiados = copy.deepcopy(produtos)

# Ordens os produtos por nome descrescente (do maior para menor)
# Gere produtos_ordernados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)


def porcentagem_produto(porcentagem):
    for produto in produtos_copiados:
        valor_calculado = produto['preco'] * porcentagem
        print(f'{produto['nome']}: {valor_calculado}')



def ordenar_produtos_crescente():
    produtos_ordenados = sorted(produtos_copiados, key=lambda item: item["preco"])

    for item in produtos_ordenados:
        print(item)


def ordenar_produtos_descrescente():
    produtos_ordenados = sorted(produtos_copiados, key=lambda item: item["preco"], reverse=True)

    for item in produtos_ordenados:
        print(item)


 

porcentagem_produto(0.10)
print('-------------')
ordenar_produtos_crescente()
print('-------------')
ordenar_produtos_descrescente()

