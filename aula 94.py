#try, except, else, e finally
try:
    print('Abrir arquivo')
    8/0
except ZeroDivisionError:
    print('DIVIDIU ZERO')
except (NameError, ImportError):
    print('DIVIDIU ZERO')
except IndexError as error:
    print('IndexError')
else:
    print('Não deu erro')
finally:
    print('Fechar arquivo')
