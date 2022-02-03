import random

class Monstro:
    def __init__(self):
        self.defesa = []
    
    def __del__(self):
        self.defesa = []

    def gerarDefesa(self):
        data = range(0, 6)
        random.shuffle(data)
        self.defesa = data[:4]

class MonstroTestSpy(Monstro):
    def __init__(self):
        Monstro.__init__(self)
        self.chamouGerarDefesa = False

    def gerarDefesa(self):
        self.chamouGerarDefesa = True
 