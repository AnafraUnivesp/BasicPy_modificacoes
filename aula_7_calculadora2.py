#Se eu não quiser continuar tendo a classe, mas não queira instanciar os objetos
class Calculadora:
    def __init__(self): # sempre que eu for instanciar a classe calculadora ele passará pelo método __init__

        def soma(self, a, b):
            return a + b

        def subtracao(self, a, b):
            return a - b

        def divisao(self, a, b):
            return a / b

        def multiplicacao(self, a, b):
            return a * b


    calculadora = Calculadora # ao instanciar a calculadora eu não informo valor nenhum
    print(calculadora.soma(2, 3))
    print(calculadora.subtracao(2, 3))
    print(calculadora.divisao(2, 3))
    print(calculadora.multiplicacao(2, 3))