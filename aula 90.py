import sys

# Generator expression(funções que sabem pausar), Iterables(responsabilidade reter o valor) e Iterators(entregar o próximo valor) em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__
lista = [n for n in range(100)]
generator = (n for n in range(10))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(next(generator))