from random import randint
level_inicial = 1
player_level = level_inicial

#perícias player

pericias_player = {
    'Atualidades': 0, 'Ciência': 0, 'Diplomacia': 0, 'Enganação': 0,
    'Furtividade': 0, 'Intimidação': 0, 'Intuição': 0, 'Investigação': 0,
    'Luta': 0, 'Medicina': 0, 'Ocultismo': 0, 'Percepção': 0,
    'Pontaria': 0, 'Reflexos': 0, 'Tecnologia': 0, 'Vontade': 0
}

#dicionário ataques

#dicionário armas

    #nome, modificador, dano, alcance e munições

#dicionário descrições

#dicionário loot


#dicionário inimigos
classes_inimigos = {
    1:
    'Ocultista',
    'Level': player_level + randint(0, 1),
    'Agilidade': 2,
    'Força': 1,
    'Inteligência': 2,
    'Presença': 3,
    'Vigor': 0,

    2:
    'Combatente',
    'Level': player_level + randint(0, 1),
    'Agilidade': 1,
    'Força': 3,
    'Inteligência': 0,
    'Presença': 1,
    'Vigor': 3,

    3:
    'Especialista',
    'Level': player_level + randint(0, 1),
    'Agilidade': 2,
    'Força': 1,
    'Inteligência': 3,
    'Presença': 1,
    'Vigor': 2
}

def saber():
    sort_classe = randint(1, 3)
    if sort_classe == 1:
        print(classes_inimigos[1])
    elif sort_classe == 2:
        print(classes_inimigos[2])
    else:
        print(classes_inimigos[3])

saber()