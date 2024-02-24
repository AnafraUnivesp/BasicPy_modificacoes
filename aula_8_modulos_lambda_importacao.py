from aula_7_Televisao import Televisao
from aula_7_calculadora1 import Calculadora
from aula_8_contador_de_palavras import contador_letra

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letra(lista)
    print(contador_letra(lista))
