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

# Comparativo de idades simples

minha_idade = 22
idade_amor = 22

if minha_idade < idade_amor:
    print("Seu amor é mais velho que você.")
elif minha_idade > idade_amor:
    print("Você é mais velha que seu amor.")
else:
    print("Você e seu amor têm a mesma idade.")