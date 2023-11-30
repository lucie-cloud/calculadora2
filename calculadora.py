# interface da calculadora

from calc2 import soma

# apresentação
print('\n\t\t\t -- Calculadora 2 --\n')

# entrada
num1 = int(input('Informe o n1: '))
num2= int(input('Informe o n2: '))

# processamento
total = soma(num1, num2)

# saída
print(f'{num1} + {num2} = {total}')
