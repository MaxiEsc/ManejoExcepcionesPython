'''
  En Python se dispone de una gran cantidad de clases que manejan las excepciones
  Siendo la clase BaseExcepcion la clase padre que maneja todas las excepciones.
  Luego asu la clase que seguiria es Exception
  que de alli derivan las demas clases
  como:
  AritmeticError --> ZeroDivisionError
  OSError ---> FilenotFoundError, PermisionError
  RuntimeError
  SyntaxError
  LockupError --> KeyError, IndexError

'''

#En otros Lenguajes se manejan como Try{}Catch{}
try:
    10/0
except Exception as e:
    print(f'Ocurrió un error: {e}')