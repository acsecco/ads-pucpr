# 1. Filtro de idade para tirar a CNH

print("Seja bem-vindo ao site do Detran-PR")
idade = int(input("Por favor insira sua idade:"))

if idade > 18:
    print("Sendo redirecionado para a tela de inscrição do teste da CNH...")
else:
    print("Idade insufiente, volte quando atingir a maioridade.")

print("------------------------------------------")

# 2. Filtro para quantidade de caractere

print("CADASTRE SEU CARTÃO DE CRÉDITO")

while True:

    nome = input("Digite seu nome (máximo: 20 caracteres):")

    if len(nome) > 20:
        print("Seu nome está extenso demais, tente novamente abreviando algum sobrenome.")
        continue
    else:
        print("Cartão de crédito cadastrado com sucesso!")
        break

print("------------------------------------------")

# 3. Filtro de par ou ímpar

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"O valor {numero} é par.")
else:
    print(f"O valor {numero} é ímpar.")

print("------------------------------------------")

# 4. Cálculo de abono de fim de ano

salario = float(input("Para calcular o abono de fim de ano, insira seu salário:"))

if salario < 5000:
    salario * 0.15
    print(f"Seu abono de fim de ano será de R${salario * 0.15}")
else: 
    salario * 0.10
    print(f"Seu abono de fim de ano será de R${salario * 0.10}")

print("------------------------------------------")

# 5. Inserir turno de trabalho

turno = input("Informe seu turno de trabalho seguindo a lista abaixo como referência:\nM - Manhã\nT - Tarde\nN - Noite\nInforme seu turno:")

if turno == "M":
    print("Bom dia!")
elif turno == "T":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Turno inválido.")

print("------------------------------------------")

# 6. Calculadora básica

num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
op = input("Informe a operação a ser executada com esses valores (adição/subtração/multiplicação/divisão): ").lower()
result = 0

if op == "adição":
    result = num1 + num2
elif op == "subtração":
    result = num1 - num2
elif op == "multiplicação":
    result = num1 * num2
elif op == "divisão":
    result = num1 / num2
else:
    op = "erro"
if op == "erro":
    print("Operação inválida!")
else:
    print(f"O resultado da operação {op} entre os valores {num1} e {num2} é: {result}")
        
print("------------------------------------------")

