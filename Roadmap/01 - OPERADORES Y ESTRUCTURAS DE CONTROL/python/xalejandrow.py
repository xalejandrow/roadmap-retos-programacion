# #01 OPERADORES Y ESTRUCTURAS DE CONTROL
#### Dificultad: Fácil | Publicación: 02/01/24 | Corrección: 08/01/24

## Ejercicio

'''
/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
'''

#  OPERADORES 

# Aritmeticos ( +, -, *, /, %, **, // )
mi_var_1 = 10
mi_var_2 = 7
print(f'Suma: {mi_var_1 + mi_var_2}')               # devuelve la suma
print(f'Resta: {mi_var_1 - mi_var_2}')              # devuelve la resta
print(f'Multiplicacion: {mi_var_1 * mi_var_2}')     # devulve la multiplicacion
print(f'Division: {mi_var_1 / mi_var_2}')           # devuelve el cociente (inclye decimales)
print(f'Modulo: {mi_var_1 % mi_var_2}')             # devuelve el resto/residuo
print(f'Potencia: {mi_var_1 ** mi_var_2}')          # devuelve el numero en potencia
print(f'Division entero: {mi_var_1 // mi_var_2}')   # devuelve el cociente entero


# Logicos  Booleanos -> AND, OR, NOT
print(True and True)        # devuelve True
print(True and False)       # devuelve False
print(True or False)        # devuelve True
print(not True)             # devuelve False
print(not False)            # devuelve True
print(not 0)                # cero es igual a False, entonces devuelve True
print(not 1)                # uno es igual a True, entonces devuelve False


# Comparacion ( >, <, ==, >=, <=, !=, ) 
print(f'Mayor que: {mi_var_1 > mi_var_2}')              # devuelve True
print(f'Menor que: {mi_var_1 < mi_var_2}')              # devuelve False
print(f'Igual que: {mi_var_1 == mi_var_2}')             # devuelve False
print(f'Mayor o igual que: {mi_var_1 >= mi_var_2}')     # devuelve True
print(f'Menor o igual que: {mi_var_1 <= mi_var_2}')     # devuelve False
print(f'Distinto que: {mi_var_1 != mi_var_2}')          # devuelve True


# Asignacion ( =, +=, -=, *=, /=, %=, **=, //= ) -> asignar valores a una variable
a = 5
print(f'Variable a: {a}')
a += 10 # es lo mismo que a = a + 10
print(f'Sumando 10 a la variable a: {a}')
a -= 10 # es lo mismo que a = a - 10
print(f'Restando 10 a la variable a: {a}')
a *= 10 # es lo mismo que a = a * 10
print(f'Multiplicando 10 a la variable a: {a}')
a /= 10 # es lo mismo que a = a / 10
print(f'Dividiendo 10 a la variable a: {a}')
b = 45
b %= 10 # es lo mismo que a = a % 10
print(f'Modulo 10 a la variable b: {b}')
b **= 10
print(f'Potencia 10 a la variable b: {b}')
b //= 5
print(f'Division entera 10 a la variable b: {b}')


# Indentidad ( is, is not) -> comprobar si dos variables emplean la misma ubicacion en memoria
a = 10
b = 10
c = 15
print(a is b)               # devuelve True
print(a is not b)           # devuelve False
print( a is c)              # devuelve False
print( a is not c)          # devuelve True


# Pertenencia ( in, not it) -> para indicar pertenencia a alguna secuencia (listas, tuplas, strings)
lista = [1, 2, 3, 4, 5]
print(3 in lista)           # devuelve True
print(15 not in lista)      # devuelve True

string = 'Hola mundo'
print('mun' in string)      # devuelve True
print('de' in string)       # devuelve False
print('Ho' in string)       # devuelve True
print('ho' in string)       # devuelve False, distingue entre mayusculas y minusculas, es case sensitive



#---  ESTRUCTURAS DE CONTROL ( Condicionales, iterativas, excepciones... )  ---#

# CONDICIONAL
# If, elif, else ( controlar si se cumple 1 o varias condiciones -> utilizar operadores de comparacion y logicos)
total_compra = 120

if total_compra <= 100:
    print('Pago en efectivo')
elif total_compra > 100 and total_compra < 500:
    print('Pago con targeta de debito')
else:
    print('Pago con targeta de credito')


# ITERACION
# While - se ejecuta mientras la condicion sea verdadera.
numero = 0
while numero <= 10:
    print(numero)
    numero += 1


# For  itera sobre un conjunto de valores
colores = ('blanco','negro','azul','verde','rojo','amarillo')
for color in colores:
    print(color)


# EXCEPCION
while True:
    # control de la excepcion
    try:
        var_num = int(input('Ingrese un numero: '))
        break # valor valido termina la ejecucion
    
    # valor invalido, devuelve el error
    except ValueError:
        print('Error! No ha insertado un valor valido. Intentelo de nuevo')


# DIFICULTAD EXTRA 
for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)


