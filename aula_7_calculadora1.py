# Detalhes desta aula

# Contruindo métodos e funções
# Como declarar métodos e funções
# Vantagens de se utilizar métodos e funções
# Como implementar o Class
# Vantagens de se utilizar classes

#Função ( tudo o que retorna valor) | método ( é aquilo que não retorna valor e no python é chamado definição (def)
#
# def soma (a,b):
#     return a + b
#
# def subtracao (a,b):
#     return  a - b
#
# def multiplicacao (a,b):
#     return  a * b
#
# def divisao (a,b):
#     return  a / b
#
# def resto (a,b):
#     return  a % b
#
# print(soma(1, 2))
# print(soma(3, 4))
# print(subtracao(3, 4))
# print(multiplicacao(3, 4))
# print(divisao(3, 4))
# print(resto(3, 4))
# print(subtracao(3, 4))


#Para facilitar eu posso utilizar classes
class Calculadora:
    def __init__(self,num1,num2): #sempre que eu for instanciar a classe calculadora ele passará pelo método __init__
        self.a = num1
        self.b = num2

    def soma (self):
        return  self.a + self.b

    def subtracao (self):
        return  self.a - self.b

    def multiplicacao (self):
        return  self.a * self.b
    def divisao (self):
        return  self.a / self.b

    def resto (self):
        return self.a % self.b
    
#Instanciando uma classe:

calculadora = Calculadora(10,2) #ao instanciar a calculadora eu não informo valor nenhum
print(calculadora.a)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(calculadora.divisao())
print(calculadora.resto())
