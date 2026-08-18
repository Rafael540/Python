import copy

from dados import produtos


# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordens os produtos por nome descrescente (do maior para menor)
# Gere produtos_ordernados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_copiados = copy.deepcopy(produtos)


def porcentagem_produto(porcentagem):
    for produto in produtos_copiados:
        valor_calculado = round(produto['preco'] * porcentagem,2)
        print(f'{produto['nome']}: {valor_calculado}')



def ordenar_produtos_crescente():
    produtos_ordenados = sorted(produtos_copiados, 
                                key=lambda item: item["nome"])

    for item in produtos_ordenados:
        print(item)


def ordenar_produtos_descrescente():
    produtos_ordenados = sorted(produtos_copiados, 
                                key=lambda item: item["nome"], 
                                reverse=True)

    for item in produtos_ordenados:
        print(item)


 

porcentagem_produto(1.1)
print('-------------')
ordenar_produtos_crescente()
print('-------------')
ordenar_produtos_descrescente()

