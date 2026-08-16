#try,except, else e finally
#a = 18
#b = 0
#c = a / b
#string = 'Luiz'
#print(isinstance(string, str))

try: 
    a = 10
    b = 0
    #print(b[0])
    # print('Linha 1' [1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e: 
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Varival não definida')
except (TypeError, IndexError) as error:
    print('TypeError +  IndexError')
    print('MSG:', error)
    print('Nome', error.__class__.__name__)

except Exception:
    print('Erro desconhecido')

print('CONTINUAR')