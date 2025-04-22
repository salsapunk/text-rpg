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

ataques_fisicos = {
    
}

#dicionário armas

    #nome, modificador, dano, alcance e munições

#dicionário descrições

#dicionário loot


#dicionário inimigos

classe_inimigo_ocultista = {
    'Classe': 'Ocultista',
    'Level': player_level + randint(0, 1),
    'HP-Max': 10 + 2*player_level,
    'HP-Atual': 10 + 2*player_level,
    'Sanidade': 15 + 2*player_level,
    'PE': 5 + 2*player_level,
    'Defesa': 8 + 2*player_level,
    'Agilidade': 2,
    'Força': 1,
    'Inteligência': 2,
    'Presença': 3,
    'Vigor': 0,
}

classe_inimigo_combatente = {
    'Classe': 'Combatente',
    'Level': player_level + randint(0, 1),
    'HP-Max': 15 + 2*player_level,
    'HP-Atual': 15 + 2*player_level,
    'Sanidade': 8 + 2*player_level,
    'PE': 3 + 2*player_level,
    'Defesa': 10 + 2*player_level,
    'Agilidade': 1,
    'Força': 3,
    'Inteligência': 0,
    'Presença': 1,
    'Vigor': 3,
}

classe_inimigo_especialista = {
    'Classe': 'Especialista',
    'Level': player_level + randint(0, 1),
    'HP-Max': 12 + 2*player_level,
    'HP-Atual': 12 + 2*player_level,
    'Sanidade': 10 + 2*player_level,
    'PE': 4 + 2*player_level,
    'Defesa': 8 + 2*player_level,
    'Agilidade': 2,
    'Força': 1,
    'Inteligência': 3,
    'Presença': 1,
    'Vigor': 2,
}

def saber():
    sort_classe = randint(1, 3)
    if sort_classe == 1:
        print(classe_inimigo_ocultista)
    elif sort_classe == 2:
        print(classe_inimigo_combatente)
    else:
        print(classe_inimigo_especialista)

saber()