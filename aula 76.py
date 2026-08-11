'''
Operadores úteis:]
união | união(union) - Une
Intersecção & (intersection) - itens presentes em ambos
diferença - itens presentes apenas no set da esquerda
diferença simétrica ^- Itens qu enão estão em ambos
'''
s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s1 ^ s2
print(s3)