# a = int(input('Entre com um número: '))
# for x in range(1, a + 1):
#     resto = a % x
#     print(resto)

# for x in range(101):
#     print(x)


# a = int(input('Entre com um número: '))
#
# div = 0
# for x in range(1, a + 1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div = div + 1
# if div == 2:
#     print('Número {} é primo' .format(a))
# else:
#     print('Número {} não é primo' .format(a))

# a = int(input('Entre com um número: '))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#     #print(x, resto)
#         if resto == 0:
#             div += 1 #concatena com 1
#     if div == 2:
#          print(num)

# nota = int(input('Entre com a nota: '))
# while nota > 10:
#     nota = int(input('Nota Inválida. Entre com a nota correta: '))
# print(nota)


# a = 0
# while a <= 10:
#     print(a)
#     a += 1


a = int(input('Primeiro Bimestre: '))
while a > 10:
    a = int(input('Você digitou errado. Primeiro Bimestre: '))

b = int(input('Segundo Bimestre: '))
while b > 10:
    b = int(input('Você digitou errado. Segundo Bimestre: '))

c = int(input('Terceiro Bimestre: '))
while c > 10:
  c = int(input('Você digitou errado. Terceiro Bimestre: '))

d = int(input('Quarto Bimestre: '))
while d > 10:
  d = int(input('Você digitou errado. Quarto Bimestre: '))
media = (a + b + c + d ) / 4
print('media {}' .format(media))