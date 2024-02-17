#a = input('Primeiro Valor: ')  #formato em string necessario conversao
#b = input('Segundo Valor: ') #formato em string necessario conversao

a = int(input('Primeiro Valor: '))  #formato em string necessario conversao
b = int(input('Segundo Valor: ')) #formato em string necessario conversao
c = int(input('Segundo Valor: ')) #formato em string necessario conversao

if a > b and a > c: # os dois pontos representam o final do if (precisa ser verdadeiro + verdadeiro)
    print('O maior número é {}'.format(a)) #através da identação eu utilizo o tab
elif b > a and b > c:  #caso b for maior que a ou c
    print('O maior número é {}' .format(b))
else:  # se não ( caso c for maior que a e b
    print('O maior número é {}' .format(c))


    print('final do programa') #caso esse trecho estivesse dentro da identação do bloco acima ele não iria aparecer,por isso está separado para identificar o final do programa