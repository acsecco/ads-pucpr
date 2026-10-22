# Iteração por uma string
nome = input("Digite seu nome: ")

for n in nome:
    print(n)

print()

# Somando 3 valores

soma = 0

for i in range(3):
    num = int(input("Digite o " + str(i + 1) + " número: "))
    soma = soma + num
print("A soma dos números é:", soma)

# Simplificado

soma = 0

for i in range(3):
    num = int(input("Digite o " + str(i + 1) + " número: "))
    soma += num
print("A soma dos números é:", soma)