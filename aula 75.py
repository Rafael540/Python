'''
Sets - conjuntos de Python (tipo set)
Conjuntos são ensinados na matemática
Representados graficamente pelo diagrama de Venn
Sets em Python são mutáveis, porém aceitam apenas 
tipos imutáveis como valor interno.

Criando um set
set(iterável) ou (1,2,3)
'''
s1 = set('Luiz')
print(s1, type(s1))

'''''
Sets são eficientes para remover valores duplicados
de iteráveis.
 - eles não tem indexes;
 - eles não garantem ordem;
 - eles são iterávies ( for, in , not in)
 
Métodos úteis:
add, update, clear, discord
'''