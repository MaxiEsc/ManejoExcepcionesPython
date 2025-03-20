'''Distintos niveles de las excepciones seguidas de manera personalizadas'''

resultado = None
a = '10'
b = 0
try:
    resultado = a/b
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {e} , {type(e)}')
except TypeError as e:
    print(f'TypeError - Ocurrió un error: {e} , {type(e)}')
except Exception as e: #Esta es la excepcion que mas tipos de excepcion pero es importante que se revise al ultimo si no las demas no se ejecutaran
    print(f'Exception - Ocurrió un error: {e} , {type(e)}')

print(f'Resultado: {resultado}')
print('Continuamos...')