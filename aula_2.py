a = 10
b = 5
a = int(input('Entre com o 1° número: '))
b = int(input('Entre com o 2° número: 1'))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b   #resto
#teste            #para realizarmos comentário em python utilizamos os #
print(type(soma)) #verificando o tipo do resultado da soma (Inteira)
soma = str(soma)    #convertendo a soma em Inteiro
print(type(soma))
print('soma: ' + str(soma))  #concatenando texto + função
print('soma: {}' .format(soma)) #Exemplo de formatação independente do tipo + concatenação
print('soma: {}. subtracao {}.' .format(soma, subtracao)) #Exemplo de formatação independente do tipo + concatenação Obs: precisa estar na ordem correta para nao conter erros
print('soma: {soma}. \nSubtração: {subtracao}. '
      '\nMultiplicação: {multiplicacao} '
      '\nResto: {resto}' .format(soma=soma,
                         subtracao=subtracao,
                         resto=resto,
                         divisao=divisao,
                         multiplicacao=multiplicacao))
# ou
resultado = ('Soma: {soma}. \nSubtração: {subtracao}. '
      '\nMultiplicação: {multiplicacao}'
      '\nDivisao: {divisao}'
      '\nResto: {resto}' .format(soma=soma,
                         subtracao=subtracao,
                         resto=resto,
                         divisao=divisao,
                         multiplicacao=multiplicacao))
print(resultado)

print(soma)
print(subtracao)
print('subtracao:' + str(subtracao))  #concatenando texto + função
print(multiplicacao)
print(int(divisao)) #retira as casas decimais do resultado
print(divisao)
print(type(divisao)) #verificando o tipo do resultado da soma (float = decimal)
print(resto)
# x = '1'
# soma2 = int(x) + 1
# print(soma2)

