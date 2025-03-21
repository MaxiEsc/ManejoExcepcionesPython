'''En este caso ponemos a prueba el resultado de la excepcion luego de la ejecucion en consola'''

resultado = None
try:
    a = int(input('Primer número: '))
    b = int(input('Segundo número: '))
    resultado = a/b
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {e} , {type(e)}')
except TypeError as e:
    print(f'TypeError - Ocurrió un error: {e} , {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {e} , {type(e)}')
else:
    print('No se arrojó ninguna excepción')
finally:
    print('Ejecución del bloque finally')

print(f'Resultado: {resultado}')
print('Continuamos...')