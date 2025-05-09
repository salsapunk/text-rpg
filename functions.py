from random import randint
from time import sleep
import os
from data import *

#definindo os atributos dos players
def definir_atributos_player():
    print('Sobre os atributos: \n' \
    'Os atibutos começam em 1, podendo ser zerados para adicionar um ponto extra a outro atributo. \n' \
    'Agilidade, força, inteligência e vigor são autoexplicativos, já presença se trata de perícias com o sobrenatural. \n' \
    'Recomendo que calcule seus atributos antes de inseri-los no jogo.' \
    '')
    while True:
        pontos = 3
        print(pontos)
        valor_agilidade = int(input('Digite o valor da sua agilidade: '))
        if valor_agilidade == 0:
            pontos = pontos + 1
            agilidade = 0
        elif 3 < valor_agilidade:
            print('Digite o número certo!')
            continue
        elif 0 > valor_agilidade:
            print('Digite o número certo!')
            continue
        else:
            agilidade = valor_agilidade
            pontos = pontos - (valor_agilidade-1)
        print(f'pontos = {pontos}')
        valor_forca = int(input('Digite o valor da sua força: '))
        if valor_forca == 0:
            pontos = pontos + 1
            forca = 0
        elif 3 < valor_forca:
            print('Digite o número certo!')
            continue
        elif 0 > valor_forca:
            print('Digite o número certo!')
            continue
        else:
            forca = valor_forca
            pontos = pontos - (valor_forca-1)
        print(f'pontos = {pontos}')
        valor_inteligencia = int(input('Digite o valor da sua inteligência: '))
        if valor_inteligencia == 0:
            pontos = pontos + 1
            inteligencia = 0
        elif 3 < valor_inteligencia:
            print('Digite o número certo!')
            continue
        elif 0 > valor_inteligencia:
            print('Digite o número certo!')
            continue
        else:
            inteligencia = valor_inteligencia
            pontos = pontos - (valor_inteligencia-1)
        print(f'pontos = {pontos}')
        valor_presenca = int(input('Digite o valor da sua presença: '))
        if valor_presenca == 0:
            pontos = pontos + 1
            presenca = 0
        elif 3 < valor_presenca:
            print('Digite o número certo!')
            continue
        elif 0 > valor_presenca:
            print('Digite o número certo!')
            continue
        else:
            presenca = valor_presenca
            pontos = pontos - (valor_presenca-1)
        print(f'pontos = {pontos}')
        valor_vigor = int(input('Digite o valor do seu vigor: '))
        if valor_vigor == 0:
            pontos = pontos + 1
            vigor = 0
        elif 3 < valor_vigor:
            print('Digite o número certo!')
            continue
        elif 0 > valor_vigor:
            print('Digite o número certo!')
            continue
        else:
            vigor = valor_vigor
            pontos = pontos - (valor_vigor-1)
        print(f'pontos = {pontos}')
        if pontos < 0:
            print('Defina seus pontos corretamente!')
            continue
        return  agilidade, forca, inteligencia, presenca, vigor

#defina a classe do player
def definir_classe():
            while True:
                classe_n = int(input('Escolha sua classe: ' \
                '\n' \
                '1- Combatente \n' \
                '2- Especialista \n' \
                '3- Ocultista \n' \
                '4- Ajuda \n' \
                '-> '))
                if classe_n == 1:
                    classe = 'Combatente'
                    hpmax = 15
                    sanidade = 8
                    pe = 3
                    defesa = 10
                    break
                elif classe_n == 2:
                    classe = 'Especialista'
                    hpmax = 12
                    sanidade = 10
                    pe = 4
                    defesa = 8
                    break
                elif classe_n == 3:
                    classe = 'Ocultista'
                    hpmax = 10
                    sanidade = 15
                    pe = 5
                    defesa = 8
                    break
                elif classe_n == 4:
                    print('' \
                    'As classes definem sua vida, sanidade, pontos de esforço e defesa. \n' \
                    'Combatente: foca na vida e na defesa, para enfrentar o perigo. \n' \
                    'Especialista: foca em pontos de esforço e defesa, para fugir do perigo. \n' \
                    'Ocultista: foca em sanidade e pontos de esforço, para enfrentar o sobrenatural.' \
                    '')
                    sleep(7)
                    continue
            return classe, hpmax, sanidade, pe, defesa

def pericias_player():
    print('Agora escolha três perícias que você será treinado (ganha +5): ')
    print('1-Atualidades \n', '2-Ciência \n',
          '3-Diplomacia \n', '4-Enganação \n',
          '5-Furtividade \n', '6-Intimidação \n',
          '7-Intuição \n', '8-Investigação \n',
          '9-Luta \n', '10-Medicina \n',
          '11-Ocultismo \n', '12-Percepção \n',
          '13-Pontaria \n', '14-Reflexos \n',
          '15-Tecnologia \n', '16-Vontade')
                                
    try:
        p1 = int(input('Digite o número da sua primeria perícia: '))
        p2 = int(input('Digite o número da sua segunda perícia: '))
        p3 = int(input('Digite o número da sua terceira perícia: '))
    except:
        print('Digite o número certo!')
        p1, p2, p3 = None
        input('Precione qualquer tecla para continuar...')
        pericias_player()
    for p in [p1, p2, p3]:
        match p:
            case 1:
                pericias_player['Atualidades'] = 5
            case 2:
                pericias_player['Ciência'] = 5
            case 3:
                pericias_player['Diplomacia'] = 5
            case 4:
                pericias_player['Enganação'] = 5
            case 5:
                pericias_player['Furtividade'] = 5
            case 6:
                pericias_player['Intimidação'] = 5
            case 7:
                pericias_player['Intuição'] = 5
            case 8:
                pericias_player['Investigação'] = 5
            case 9:
                pericias_player['Luta'] = 5
            case 10:
                pericias_player['Medicina'] = 5
            case 11:
                pericias_player['Ocultismo'] = 5
            case 12:
                pericias_player['Percepção'] = 5
            case 13:
                pericias_player['Pontaria'] = 5
            case 14:
                pericias_player['Reflexos'] = 5
            case 15:
                pericias_player['Tecnologia'] = 5
            case 16:
                pericias_player['Vontade'] = 5

#cria o player
def criar_player():
                    nome = str(input('Digite o nome do seu personagem: '))
                    sleep(0.4)
                    
                    classe, hpmax, sanidade, pe, defesa = definir_classe()
                    player_level = 1

                    player = {
                        'Nome': nome,
                        'Classe': classe,
                        'Level': player_level,
                    }
                    
                    sleep(0.4)
                    agilidade, forca, inteligencia, presenca, vigor = definir_atributos_player()
                    atributos_player = {
                        'Agilidade': agilidade,
                        'Força': forca,
                        'Inteligência': inteligencia,
                        'Presença': presenca,
                        'Vigor': vigor
                    }
                    
                    player['HP Máximo'] = hpmax+vigor
                    player['Sanidade'] = sanidade
                    player['Pontos de Esforço'] = pe
                    player['Defesa'] = defesa
                    player['Iniciativa'] = d20 + agilidade

                    player_pericias = pericias_player()

                    return player, atributos_player, player_pericias 

#funções inimigo

#sorteia o level do inimigo
def sortear_level(player_level):
    level = randint(1, player_level+1)
    return level

#define se o inimigo é monstro ou humano
def humano_x_monstro():
    if round(d4/2) == 1:
        humano = True
    else: 
        humano = False
    return humano

#classe, atributos e perícias do inimigo
#define os atributos do inimigo
def classe_e_pericias_inimigo():
    match randint(1, 3):
        case 1:
            classe_inimigo = classe_inimigo_ocultista
            pericias_inimigo = pericias_ocultista
        case 2:
            classe_inimigo = classe_inimigo_combatente
            pericias_inimigo = pericias_combatente
        case 3:
            classe_inimigo = classe_inimigo_especialista
            pericias_inimigo = pericias_especialista
    return classe_inimigo, pericias_inimigo

def sortear_nome():
    nome = nomes[d100]
    return nome

def sortear_arma(level_inimigo):
    if level_inimigo <= 2:
        arma = armas[d4]['Arma']
    else:
        arma = armas[d8]['Arma']
    return arma

def tipo_e_elemento_monstro():
    elemento = d4
    if elemento == 1:
        elemento = 'Sangue'
    elif elemento == 2:
        elemento = 'Morte'
    elif elemento == 3:
        elemento = 'Energia'
    elif elemento == 4:
        elemento = 'Conhecimento'
    return elemento

#cria o inimigo
def criar_inimigo(humano):
    if humano == True:
        inimigo, pericias_inimigo = classe_e_pericias_inimigo()
        inimigo['Nome'] = sortear_nome()
        inimigo['Arma'] = sortear_arma(inimigo['Level'])
        return inimigo, pericias_inimigo
    else:
        inimigo, pericias_inimigo = tipo_e_elemento_monstro() #a ser definido

def acoes_inimigo(inimigo, player):
    vida_inimigo = inimigo['HP']
    nome = inimigo['Nome']
    arma = inimigo['Arma']
    if vida_inimigo >= vida_inimigo/2:
        if inimigo['PE'] > 0:
            acao = round(d4/2)
            if acao == 1: #ataque
                calcular_dano(inimigo, player)
            elif acao == 2: #rituais 
                ritual_dano()
        else:
            print(f'{nome} te ataca com {arma}')
            calcular_dano(inimigo, player)
    else:
        acao = round(d6/2)
        if acao == 1:
            calcular_dano(inimigo, player)
        if acao == 2: #rituais
            None
        else: 
            fugir_inimigo()

def fugir_inimigo():
    direcao = d4
    match direcao:
        case 1:
            direcao = 'Norte'
        case 2:
            direcao = 'Oeste'
        case 3:
            direcao = 'Sul'
        case 4:
            direcao = 'Leste'
    print(f'O inimigo fugiu para o {direcao}')

def calcular_dano(atacante, defensor):
    dano_base = atacante['Força']
    arma = atacante['Arma']

    dano_arma = armas[arma]['Dano']
    dano_total = dano_base + dano_arma

    defesa = defensor['Defesa']
    dano_final = max(dano_total - defesa, 0)

    defensor['HP'] -= dano_final
    if defensor['HP'] <= 0:
        print(f"{defensor['Nome']} foi derrotado!")
    #botar um cheque de pra ver se o defensor é o player, caso sim, game over e inicia de novo
    else:
        print(f"{defensor['Nome']} recebeu {dano_final} de dano.")

def ritual_dano():
    None