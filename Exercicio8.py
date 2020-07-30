#   Faça um Programa que pergunte quanto você ganha por hora e o número
#   de horas trabalhadas no mês.
#   Calcule e mostre o total do seu salário no referido mês.

horaValor = int(input('Quanto que você ganha por hora trabalhada? '))
horas = int(input('Quantas horas você trabalha por mês? '))

calculo = horas * horaValor

print(f'Você ganha {calculo} reais por mês.')
