primeiro_valor = float(input("Digite o primeiro valor: "))
segundo_valor = float(input("Digite o segundo valor: "))

soma = primeiro_valor + segundo_valor
subtracao = primeiro_valor - segundo_valor
multiplicacao = primeiro_valor * segundo_valor
divisao = primeiro_valor / segundo_valor
resto = primeiro_valor % segundo_valor

print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(resto)

#Exemplos da função print 
'''
print("Olá! Seja bem-vindo.")
print("O primeiro valor digitado é", primeiro_valor)
print("Veja que", segundo_valor, "foi o segundo valor digitado.")
print(f"O resultado da soma é {soma}, e da subtração é {subtracao}.")
print("O resultado da multiplicação é " + str(multiplicacao) + ".")
print(divisao)
print("Resto: " + str(resto))
'''

# Formatação com operador de modulação (%)

num = 6/7

print('Resultado: %f' % num)
print('Resultado: %.3f' % num)
print('Resultado: %8.2f' % num)
print('Resultado: %d' % num)
print('Resultado: %s' % num)

# Formatação com strings literais formatadas

num = 6/7
outro_num = 10
t1 = "Hello"
t2 = "World"
print(f'Resultado: {num:f}')
print(f'Resultado: {num:.2f}')
print(f'Resultado: {num:8.2f}')
print(f'Resultado: {outro_num:8d}')
print(f'{t1:10}{t2:10}')
print(f'{t1:^10}{t2:^10}')
print(f'{t1:>10}{t2:>10}')

# Formatação com o método format()

num = 6/7
outro_num = 10
t1 = "Hello"
t2 = "World"
print('Resultado: {0:f}'.format(num))
print('Resultado: {0:.2f}'.format(num))
print('Resultado: {0:8.2f}'.format(num))
print('Resultado: {0:8d}'.format(outro_num))
print('{0:10}{1:10}'.format(t1, t2))
print('{0:^10}{1:^10}'.format(t1, t2))
print('{0:>10}{1:>10}'.format(t1, t2))