#   Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#     o produto do dobro do primeiro com metade do segundo .
#     a soma do triplo do primeiro com o terceiro.
#     o terceiro elevado ao cubo.

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))

calc1 = valor1 * 2 + (valor2 / 2)
print(calc1)
calc2 = valor1 * 3 + valor3
print(calc2)
calc3 = valor3 * valor3 * valor3
print(calc3)
