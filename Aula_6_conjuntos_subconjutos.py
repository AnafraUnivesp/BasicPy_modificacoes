#Conjuntos Aritméticos

#Para criar um conjunto eu utilizo chaves {}

# conjunto = {1,2,3,4,4,2} #o conjunto não tem duplicidade, mesmo eu imprimindo ele apresentará apenas um dos elementos repetidos
# conjunto.add(5) #adicionando o elemento 5
# conjunto.discard(2) #descartando o elemento 2
# print(conjunto)

#União de dois conjuntos
#
# conjunto = {1,2,.3,4}
# conjunto_2 = {1,2,3}
# conjunto_uniao = conjunto.union(conjunto_2)
# #print(conjunto_uniao)
# print('União: {}'.format(conjunto_uniao))

#Intersecção entre conjuntos (é tudo o que que se repete nos dois conjuntos)

# conjunto = {1,2,.3,4}
# conjunto_2 = {1,2,3}
# conjunto_interseccao= conjunto.intersection(conjunto_2)
# print(conjunto_interseccao)
# print('Intersecção: {}'.format(conjunto_interseccao))

#Diferença entre conjuntos (imprime tudo o que tem diferente nos conjuntos além  dos números repetidos)

# conjunto = {1,2,.3,4}
# conjunto_2 = {1,2,3}
# conjunto_diferenca = conjunto.difference(conjunto_2)
# print(conjunto_diferenca)
# print('Diferença: {}'.format(conjunto_diferenca))


#Diferença entre conjuntos

# conjunto = {1,2,.3,4}
# conjunto_2 = {1,2,3}
# conjunto_diferenca_1 = conjunto.difference(conjunto_2)
# conjunto_diferenca_2 = conjunto_2.difference(conjunto)
# print(conjunto_diferenca_1)
# print(conjunto_diferenca_2)
# print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca_1))
# print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca_2))


#Diferença Simétrica (Tudo o que não tem nos dois conjuntos

# conjunto = {1,2,.3,4}
# conjunto_2 = {1,2,3}
# # conjunto_diferenca_1 = conjunto.difference(conjunto_2)
# # conjunto_diferenca_2 = conjunto_2.difference(conjunto)
# # print(conjunto_diferenca_1)
# # print(conjunto_diferenca_2)
# # print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca_1))
# # print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca_2))
# conjunto_diferenca_simetrica = conjunto.symmetric_difference(conjunto_2)
# print('Diferença Simétrica: {}'.format(conjunto_diferenca_simetrica))


#Pertinência
#Subset ( se um conjunto é um subconjunto de um outro conjunto)

# conjunto_a = {1,2,3}
# conjunto_b = {1,2,3,4,5}
# conjunto_subset = conjunto_a.issubset(conjunto_b)
# print(conjunto_subset)

#Superset ( verificar ao contrário para verificar se os conjuntos são subconjuntos um do outro)
# conjunto_a = {1,2,3} #subconjunto de b
# conjunto_b = {1,2,3,4,5} #superconjunto de a
# conjunto_subset = conjunto_a.issubset(conjunto_b)
# print(conjunto_subset)
# conjunto_subset = conjunto_a.issubset(conjunto_b)
# print('A é subconjunto de A: {}'.format(conjunto_subset))
# conjunto_superset = conjunto_b.issuperset(conjunto_a)
# print(conjunto_superset)
# print('B é subconjunto de A: {}'.format(conjunto_superset))

#Convertendo uma lista para conjunto ( retirando a dupplicidade de uma lista)

lista = ['cachorro', 'cachorro', 'gato', 'gato','elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais) #lista sem as duplicidades
print(lista_animais)
