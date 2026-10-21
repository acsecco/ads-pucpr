# Comparador de 3 números utilizando Operadores Lógicos

while True:

    print("Por favor, insira três números diferentes:")
    num1 = float(input("Digite o primeiro número:"))
    num2 = float(input("Digite o segundo número:"))
    num3 = float(input("Digite o terceiro número:"))

    if num1 == num2 or num1 == num3 or num2 == num3:
        print("Os números inseridos não são diferentes.")
        continue

    if num1 < num2 and num1 < num3:
        print(f"O menor número é: {num1}")
        break
    elif num2 < num3:
        print(f"O menor número é: {num2}")
        break
    else:
        print(f"O menor número é: {num3}")
        break