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

# 5. Inserir turno de trabalho
