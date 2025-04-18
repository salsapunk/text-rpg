from random import randint
from time import sleep

#A ideia é fazer um text-rpg em python com sistema de dados, perícias, atributos, miss, dano variado e etc, baseado no sistema de ordem paranormal

#dados
d100 = randint(1, 100)
d20 = randint(1, 20)
d12 = randint(1, 12)
d10 = randint(1, 10)
d8 = randint(1, 8)
d6 = randint(1, 6)
d4 = randint(1, 4)
d3 = d6/2

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

#funções inimigo
def inimigo_sortear_nome():
    inimigo_nomes = ['Roberto', 'Robson', 'Paulo', 'João', 'Pablo', 'Luís', 'Francisco', 'Yan', 'Marcos', 'Sérgio']
    inimigo_nome = inimigo_nomes[randint(0, len(inimigo_nomes)-1)]
    return inimigo_nome

def sortear_level(player_level):
    level = randint(1, player_level+1)
    return level

def inimigo_sortear_armas(level):
    k = 1
    inimigo_armas = ['desarmado', 'barra de ferro', 'pedaço de madeira', 'pistola', 'doze', 'rifle']
    inimigo_armas_de_fogo = 3 + k
    if level <= 3:
        inimigo_arma = inimigo_armas[randint(0, len(inimigo_armas)-inimigo_armas_de_fogo)]
    else:
        inimigo_arma = inimigo_armas[randint(0, len(inimigo_armas)-k)]
    return inimigo_arma

def criar_inimigo(player_level):
    inimigo_level = sortear_level(player_level)
    inimigo = {
        'nome': inimigo_sortear_nome(),
        'level': inimigo_level,
        'arma': inimigo_sortear_armas(inimigo_level)
    }

    #classe, atributos e perícias do inimigo

    return inimigo

def definir_atributos_inimigo():
    None

#jogo
def game():
    while True:
        a = int(input('O que você deseja fazer?' \
        '\n'
        '1-Começar \n'
        '2-Configurações \n'
        '3-Ajuda \n'
        '-> '))
        sleep(0.4)
        if a == 1:

            nome = str(input('Digite o nome do seu personagem: '))
            sleep(0.4)
            
            classe, hpmax, sanidade, pe, defesa = definir_classe()
            player_level = 1

            player = {
                'Nome': nome,
                'Classe': classe,
                'Level': player_level
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

#Perícias
            pericias_player = {
                'Atualidades': 0, 'Ciência': 0, 'Diplomacia': 0, 'Enganação': 0,
                'Furtividade': 0, 'Intimidação': 0, 'Intuição': 0, 'Investigação': 0,
                'Luta': 0, 'Medicina': 0, 'Ocultismo': 0, 'Percepção': 0,
                'Pontaria': 0, 'Reflexos': 0, 'Tecnologia': 0, 'Vontade': 0
            }

            print('Agora escolha três perícias que você será treinado (ganha +5): ')
            print('1-Atualidades \n', '2-Ciência \n', '3-Diplomacia \n', '4-Enganação \n', '5-Furtividade \n',
                  '6-Intimidação \n', '7-Intuição \n', '8-Investigação \n', '9-Luta \n', '10-Medicina \n',
                  '11-Ocultismo \n', '12-Percepção \n', '13-Pontaria \n', '14-Reflexos \n', '15-Tecnologia \n',
                  '16-Vontade')
            p1, p2, p3 = map(int, input('Digite o número das suas perícias separadas por espaço: ').split())

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

            print(f'Sobre o jogador: \n {player}')
            print(f'Atributos do jogador: \n {atributos_player}')
            print(f'Perícias do jogador: \n {pericias_player}')
            
            inimigo = criar_inimigo()
            print(inimigo)

            break
        elif a == 2:
            print('configurações')
            continue
        elif a == 3:
            print('ajuda')
            continue
        else:
            print('Digite um número entre 1 e 3')
            continue
    
game()