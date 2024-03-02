from aula_7_Televisao import Televisao
from aula_7_calculadora1 import Calculadora
from aula_8_contador_letra import contador_letras, teste

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    lista = ['cachorro','gato', 'elefante']
    total_letras =  contador_letras(lista)
    print('total de letras por palavras da lista: {}'.format(total_letras))
    print(teste())

