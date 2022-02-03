from Monstro import Monstro, MonstroTestSpy
from Ataque import Ataque, AtaqueTestSpy
from Jogador import Jogador
import unittest

class Jogo:
    def __init__(self, monstro, jogador):
        self.monstro = monstro
        self.vitoria = False
        self.jogador = jogador

    def __del__(self):
        del self.monstro
        self.vitoria = False

    def atacar(self, ataque):
        if self.monstro.defesa == []:
            self.monstro.gerarDefesa()
           
        self.vitoria = ataque.conferirAtaque(self.monstro.defesa)

        if not self.vitoria:
            self.jogador.vidasDoJogador -= 1

class Test(unittest.TestCase):
    def setUp(self):
        self.jogador = Jogador(5)
        self.monstro = MonstroTestSpy()
        self.vitoria = False
        self.sut = Jogo(self.monstro, self.jogador)

    def tearDown(self):
        del self.jogador
        del self.monstro
        del self.vitoria
        del self.sut
        
#1.Dado um monstro sem defesa, quando for atacar, então é gerado uma defesa
#para o monstro(classe Jogo)

    def teste_givenMonstroSemDefesa_whenAtacar_thenDefenda(self):
        armas = [1,2,3,4]
        ataque = Ataque(armas)
        self.monstro.defesa = []

        self.sut.atacar(ataque)

        self.assertTrue(self.monstro.chamouGerarDefesa)
#2.Dado um monstro com defesa, quando for atacar, então não é gerado uma
#defessa para o monstro (Classe Jogo)

    def teste_givenComDefesa_whenAtacar_thenNaoDefenda(self):
        armas = [1,2,3,4]
        ataque = Ataque(armas)
        self.monstro.defesa = [1,2,3,4]

        self.sut.atacar(ataque)

        self.assertFalse(self.monstro.chamouGerarDefesa)

#3.Dado 2 armas certas na posição errada e 2 armas certas nas posições certas,
#quando for atacar, então o ataque possui 2 armas certas nas posições certas e
#chamou a função acertouAtaque duas vezes (classe Jogo). 

    def teste_given2ArmasCertasPosicoesErradas2ArmasCertasPosicoesCertas_whenAcertou2(self):
        armas = [1,2,3,4]
        ataque = AtaqueTestSpy(armas)
        self.monstro.defesa = [1,3,2,4]

        self.sut.atacar(ataque)

        self.assertEqual(ataque.chamouAcertouAtaque, 2)
        self.assertEqual(ataque.armasCorretasNaPosicaoCorreta, 2)
        self.assertEqual(ataque.armasCorretasNaPosicaoErrada, 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)