'''
Exercício para diferenciar input de números pares ou ímpares
Lógica:
numero = 2: o resto da divisão por 2 é 0. Logo, este número é par.
numero = 3: o resto da divisão por 2 é 1. Logo, este número é ímpar.
numero = 4: o resto da divisão por 2 é 0. Logo, este número é par.
numero = 5: o resto da divisão por 2 é 1. Logo, este número é ímpar.
'''

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"O valor {numero} é par.")
else:
    print(f"O valor {numero} é ímpar.")
