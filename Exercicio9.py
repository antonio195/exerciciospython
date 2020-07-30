#   Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
#   C = 5 * ((F-32) / 9).

temp = int(input('Digite a temperatura atual em Farenheit: '))

calculo = 5 * ((temp-32) / 9)

print(f'A temperatura convertida é de {calculo} Celsius.')
