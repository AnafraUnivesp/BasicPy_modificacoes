#Se eu não quiser continuar tendo a classe, mas não queira instanciar os objetos

#Calculadora Usando Método Init
# class Calculadora:
#     def __init__(self): # sempre que eu for instanciar a classe calculadora ele passará pelo método __init__
#         pass
#     def soma(self, a, b):
#             return a + b
#
#     def subtracao(self, a, b):
#             return a - b
#
#     def divisao(self, a, b):
#             return a / b
#
#     def multiplicacao(self, a, b):
#             return a * b
#
#     def resto(self, a, b):
#         return a % b
#
# calculadora = Calculadora # ao instanciar a calculadora eu não informo valor nenhum
# print(calculadora.soma(0,3,4))
# print(calculadora.subtracao(0,3,4))
# print(calculadora.multiplicacao(0,3,4))
# print(calculadora.divisao(0,3,4))
# print(calculadora.resto(0,3,4))


#Calculadora sem utilizar o método init
class Calculadora:
    # def __init__(self): # sempre que eu for instanciar a classe calculadora ele passará pelo método __init__
    #     pass
    def soma(self, a, b):
            return a + b

    def subtracao(self, a, b):
            return a - b

    def divisao(self, a, b):
            return a / b

    def multiplicacao(self, a, b):
            return a * b

    def resto(self, a, b):
        return a % b

calculadora = Calculadora # ao instanciar a calculadora eu não informo valor nenhum
print(calculadora.soma(0,3,4))
print(calculadora.subtracao(0,3,4))
print(calculadora.multiplicacao(0,3,4))
print(calculadora.divisao(0,3,4))
print(calculadora.resto(0,3,4))



