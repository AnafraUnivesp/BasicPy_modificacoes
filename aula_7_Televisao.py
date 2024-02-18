#iremos criar um método e uma classe, um botão de canal e a função, ligar e desligar da tv

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

televisao = Televisao()
print('A televisão está ligada: {}'.format(televisao.ligada)) # 1° eu instanciei e ela apareceu desligada
televisao.power()       # ai eu fui lá e apertei o power e ela ligou (true)
print('A televisão está ligada: {}'.format(televisao.ligada))
televisao.power()       #ai apertei o power novamente e ela foi desligada
print('A televisão está ligada: {}'.format(televisao.ligada))
print('Canal: {}'.format(televisao.canal))
televisao.power()
print('A televisão está ligada: {}'.format(televisao.ligada))
televisao.aumenta_canal()
televisao.aumenta_canal()
print('Canal: {}'.format(televisao.canal))
televisao.diminui_canal()
print('Canal: {}'.format(televisao.canal))



