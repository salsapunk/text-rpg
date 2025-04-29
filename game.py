from random import randint
from time import sleep
import os
from data import *
from functions import *
from sistema import *

#A ideia é fazer um text-rpg em python com sistema de dados, perícias, atributos, miss, dano variado e etc, baseado no sistema de ordem paranormal

#jogo
def game():
        os.system('clear')
        print('Bem-vinde ao projeto de Text-RPG infinito baseado no sistema de Ordem')
        a = int(input('O que você deseja fazer?' \
        '\n'
        '1-Começar \n'
        '2-Configurações \n'
        '3-Ajuda \n'
        '-> '))
        sleep(0.4)
        if a == 1:
            #player, atributos_player, pericias_player = criar_player()
            #print(f'Sobre o jogador: \n {player}')
            #print(f'Atributos do jogador: \n {atributos_player}')
            #print(f'Perícias do jogador: \n {pericias_player}')

            while True:
                inimigo = criar_inimigo(True)
                print(inimigo)

        elif a == 2:
            #configuracoes()
            input('Pressione qualquer tecla para continuar.')
            limpar_tela()
            game()
        elif a == 3:
            #ajuda()
            input('Pressione qualquer tecla para continuar.')
            limpar_tela()
            game()
        else:
            erro_clear()
            game()

game()