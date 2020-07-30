#   Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
#   (C × 9/5) + 32

temp = int(input('Digite a temperatura atual em Celsius: '))

calculo = (temp * 9/5) + 32

print(f'A temperatura convertida é de {calculo} Farenheit.')
