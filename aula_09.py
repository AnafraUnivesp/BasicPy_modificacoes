

import shutil
def escrever_arquivo(texto):  #metodo escrever arquivo
    diretorio = 'D:/Linux/BasicPy/teste.txt'  #Criando um arquivo em um diretório
    arquivo = open(diretorio, 'w') #abrindo um diretorio
    #arquivo = open('teste.txt',  'w') #cria um novo arquivo onde as informações serão refletidas
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):  #metodo escrever arquivos
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):  #metodo ler arquivos
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):  # metodo médias notas
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')  # split é uma quebra, neste caso caso uma quebra de linha . será necessário tranforma as notas dos alunos em uma lista e utilizar o comando split para que o python não entenda como string ou saia na vertical
    #print(aluno_nota)
    lista_media = []

    for x in aluno_nota: # será realizado um for para acessar cada linha de cada aluno mencionado no passo anterior para gerar suas respectivas médias
        #print(x) #não será possível utilizar o print dessa forma, pois as notas serão exibidas todas na vertical, pois o python esrá entendendo como string
        #precisarei criar um novo split para apresentar os alunos e as notas pela virgula
        lista_notas = x.split(',')
       #print(lista_notas)
        aluno = lista_notas[0]
        lista_notas.pop(0) #para
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas ])/4 #mudando para de string para inteiros e já trazendo a média. utilizando a lambda para retornar tudo em uma única linha
        print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo): #metodo de copiar arquivos
    #import shutil #biblioteca para realizar importação do arquivo para outro diretorio
    shutil.copy(nome_arquivo,'D:/Linux/BasicPy/alunos_notas.txt') #copiar no diretorio mencionado

def move_arquivo(nome_arquivo): #metodo de copiar arquivos
    #import shutil #biblioteca para realizar importação do arquivo para outro diretorio
    #shutil.copy(nome_arquivo,'D:/Linux/BasicPy/alunos_notas.txt') #copiar no diretorio mencionado
    shutil.move(nome_arquivo, 'D:/Linux/')

if __name__ == '__main__': #Chamadas
    copia_arquivo('notas.txt')
    #copia_arquivo('notas.txt')
    # escrever_arquivo('Primeira Linha.\n')
    # aluno = '\nFrancisco 8,6,5,9,10\n' #variável para gerar outras notas precisa apagar o nome e adicionar manualmente
    # atualizar_arquivo('notas.txt',  aluno) #aluno = variável
    # ler_arquivo('teste.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
