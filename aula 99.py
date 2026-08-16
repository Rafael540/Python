import importlib
import aula98__m

print(aula98__m.variavel)

for i in range(10):
    importlib.reload(aula98__m)
    print(i)

print('Fim')