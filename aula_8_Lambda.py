# Detalhes desta Aula

# Como realizar importação de módulos ( lambda)
# Entendendo a importancia de se trabalhar com vários módulos
# Acessando métodos e classes de um módulo
# Entendendo e trabalhando com funções anônimas

contador_letras = lambda lista: [len(x) for x in lista] #lista utilizo colchetes lens, quantidade de letras que tem no x
lista_animais = ['cachorro','gato','elefante','cachorro']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
multiplicacao = lambda a, b: a * b
divisao = lambda a, b: a / b
print(soma(5,10))
print(subtracao(5,10))
print(multiplicacao(5,10))
print(divisao(5,10))

calculadora = {
    'soma': lambda a,b:a + b,
    'subtracao': lambda a,b:a - b,
    'multiplicacao': lambda a,b:a * b,
    'divisao': lambda a,b:a / b,
}

print(type(calculadora))
soma = calculadora['soma']
subtracao =  calculadora['subtracao']
multiplicacao = calculadora['multiplicacao']
divisao = calculadora['divisao']
print('A Soma é: {}'.format(soma(10,5)))
print('A Multiplicação é: {}'.format(multiplicacao(10,5)))
print('A Divisão é: {}'.format(divisao(10,5)))
print('A Subtração é: {}'.format(subtracao(10,5)))




