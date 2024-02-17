# Verificando se um número é par

# a = int(input('Entre com o primeiro valor: '))
# resto = a % 2
# if resto == 0:
#     print('Número é par: ')
# else:
#     print('Número é ímpar: ')
#
# print('Fim do Programa')

# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
# resto_a = a % 2
# resto_b = a % 2
# if resto_a == 0 or resto_b == 0:
#     print('Foi digitado um número par: ')
# else:
#     print('Nenhum número par foi digitado: ')
#
# print('Fim do Programa')

# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
# resto_a = a % 2
# resto_b = a % 2
# if resto_a == 0 or not resto_b > 0: #usodenot
#     print('Foi digitado um número par: ')
# else:
#     print('Nenhum número par foi digitado: ')
#
# print('Fim do Programa')

a = int(input('Primeiro Bimestre: '))
if a > 10:
    a = int(input('Você digitou errado. Primeiro Bimestre: '))

b = int(input('Segundo Bimestre: '))
if b > 10:
    b = int(input('Você digitou errado. Segundo Bimestre: '))

c = int(input('Terceiro Bimestre: '))
if c > 10:
  c = int(input('Você digitou errado. Terceiro Bimestre: '))

d = int(input('Quarto Bimestre: '))
if d > 10:
  d = int(input('Você digitou errado. Quarto Bimestre: '))
media = (a + b + c + d ) / 4
print('media {}' .format(media))


# if a <= 10  and b <= 10 and c <= 10 and d <= 10:
#     print('media {}' .format(media))
# else:
#     print('Foi informado uma nota errada')
# print('Final do Programa')




