# Detalhes desta Aula

#Criando uma lista
#Manipular Listas
#Realizar Operações com a Lista
#O que é uma tupla
#Como interagir com as tuplas
#Conversões de listas e tuplas


lista = [1, 3, 5, 7] #a lista sempre estará dentro de um colchetes
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
#print(type (lista))
print(lista_animal[1]) #no python começamos a contar a partir do 0, portanto nesta lista a palavra gato seria a posição 1, assim sucessivamente

#for x in lista_animal: #sempre no final do for, while, else, elif e etc finalizar com o símbolo de :

# soma = 0
# for x in lista: #sempre no final do for, while, else, elif e etc finalizar com o símbolo de :
#     print(x)
#     soma += x
#     print(soma)

#print(sum(lista)) #somar os valores da lista acima
#print(max(lista)) #encontrando o maior valor dessa lista
#print(min(lista)) #encontrando o menor valor dessa lista

# print(max(lista_animal)) #encontrando o maior valor dessa lista,em caso de string ele olha a letra do alfabeto (letra g)
# print(min(lista_animal)) #encontrando o menor valor dessa lista,em caso de string ele olha a letra do alfabeto ( letra c)


#Usando Condicionais

# if 'lobo' in lista_animal:
#     print('Existe um lobo na lista')
# else:
#     print('Não existe um lobo na lista')

# #Incluindo o lobo na lista
# if 'lobo' in lista_animal:
#     print('Existe um lobo na lista')
# else:
#     print('Não existe um lobo na lista')
#     lista_animal.append('lobo') #o append é uma função da lista
#     print(lista_animal)

#Retirando um elemento da lista
# if 'lobo' in lista_animal:
#     print('Existe um lobo na lista')
# else:
#     print('Não existe um lobo na lista')
#     lista_animal.append('lobo') #o append é uma função da lista
#     print(lista_animal)
# lista_animal.pop() #o pop faz tipo uma pilha e retira o elemento final
# print(lista_animal)

#Retirando um elemento da lista conforme a posição escolhida
# if 'lobo' in lista_animal:
#     print('Existe um lobo na lista')
# else:
#     print('Não existe um lobo na lista')
#     lista_animal.append('lobo') #o append é uma função da lista
#     print(lista_animal)
# lista_animal.pop(1) #neste caso o gato estava na posição 1, portanto foi retirado
# print(lista_animal)

#Retirando um elemento da lista conforme conhecido
# if 'lobo' in lista_animal:
#     print('Existe um lobo na lista')
# else:
#     print('Não existe um lobo na lista')
#     lista_animal.append('lobo') #o append é uma função da lista
# #     print(lista_animal)
# lista_animal.remove('elefante') #a palavra elefante foi removida e as demais mantidas
# print(lista_animal)

#Multiplicando uma lista
# nova_lista = lista_animal * 3
# print(nova_lista)


#Ordenação de listas
# lista.sort()
# lista_animal.sort()
# print(lista_animal)
# print(lista)

# #Ordenação de listas
# lista.reverse()
# lista_animal.reverse() #o reverse ordena do final para o começo
# print(lista_animal)
# print(lista)


#TUPLAS (tupla ( é imutável), já a lista é mutável)
#
# lista_animal[0] = 'macaco'
# print(lista_animal)
#
# tupla = (1,10,12,14)

# #Para saber quantas posições eu possuo na tupla
#
# lista_animal[0] = 'macaco'
# print(lista_animal)
#
# tupla = (1,10,12,14)
# print(len(tupla))
# print(len(lista_animal))

# Convertendo uma lista para uma Tupla

# tupla = (1,10,12,14)
# print(len(tupla))
# print(len(lista_animal))
# tupla_animal = tuple(lista_animal)
# print(type(tupla_animal))
# print(tupla_animal)


# Convertendo uma tupla para uma lista

tupla = (1,10,12,14)
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100 #neste caso a posição 0 que neste exempplo é o número 1, será substituido pelo número 100
print(lista_numerica)



