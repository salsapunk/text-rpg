from random import randint
level_inicial = 1
player_level = level_inicial


#dados
d100 = randint(1, 100)
d20 = randint(1, 20)
d12 = randint(1, 12)
d10 = randint(1, 10)
d8 = randint(1, 8)
d6 = randint(1, 6)
d4 = randint(1, 4)


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

armas = {
    'Desarmado': {
        'Dano': d6,
        'Alcance': 1
    },
    'Faca': {
        'Dano': d6,
        'Alcance': 1
    },
    'Barra de ferro': {
        'Dano': d6,
        'Alcance': 1
    },
    'Pedaço de madeira': {
        'Dano': d6,
        'Alcance': 1
    },
    'Espada': {
        'Dano': d12,
        'Alcance': 1
    },
    'Pistola': {
        'Dano': d10,
        'Alcance': 5,
        'Municoes': 6
    },
    'Doze': {
        'Dano': 2*d12,
        'Alcance': 10,
        'Municoes': 2
    },
    'Rifle': {
        'Dano': 2*d10,
        'Alcance': 10,
        'Municoes': 5
    }
}

    #nome, modificador, dano, alcance e munições

#dicionário descrições

#dicionário loot


#dicionário inimigos

classe_inimigo_ocultista = {
    'Nome': None,
    'Classe': 'Ocultista',
    'Level': player_level + randint(0, 1),
    'Arma': None,
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

pericias_ocultista = {
    'Atualidades': 0, 'Ciência': 0, 'Diplomacia': 0, 'Enganação': 0,
    'Furtividade': 0, 'Intimidação': 0, 'Intuição': 5, 'Investigação': 0,
    'Luta': 0, 'Medicina': 0, 'Ocultismo': 5, 'Percepção': 0,
    'Pontaria': 0, 'Reflexos': 0, 'Tecnologia': 0, 'Vontade': 5
}

classe_inimigo_combatente = {
    'Nome': None,
    'Classe': 'Combatente',
    'Level': player_level + randint(0, 1),
    'Arma': None,
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

pericias_combatente = {
    'Atualidades': 0, 'Ciência': 0, 'Diplomacia': 0, 'Enganação': 0,
    'Furtividade': 0, 'Intimidação': 5, 'Intuição': 0, 'Investigação': 0,
    'Luta': 5, 'Medicina': 0, 'Ocultismo': 0, 'Percepção': 0,
    'Pontaria': 0, 'Reflexos': 5, 'Tecnologia': 0, 'Vontade': 0
}

classe_inimigo_especialista = {
    'Nome': None,
    'Classe': 'Especialista',
    'Level': player_level + randint(0, 1),
    'Arma': None,
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

pericias_especialista = {
    'Atualidades': 0, 'Ciência': 0, 'Diplomacia': 0, 'Enganação': 0,
    'Furtividade': 5, 'Intimidação': 0, 'Intuição': 0, 'Investigação': 5,
    'Luta': 0, 'Medicina': 0, 'Ocultismo': 0, 'Percepção': 0,
    'Pontaria': 5, 'Reflexos': 0, 'Tecnologia': 0, 'Vontade': 0
}

nomes = {
1: 'Adriano',
2: 'Aline',
3: 'Amanda',
4: 'Ana',
5: 'André',
6: 'Antônio',
7: 'Arthur',
8: 'Beatriz',
9: 'Bernardo',
10: 'Bianca',
11: 'Bruno',
12: 'Caio',
13: 'Camila',
14: 'Carla',
15: 'Carlos',
16: 'Carolina',
17: 'Cauê',
18: 'Célia',
19: 'César',
20: 'Clara',
21: 'Daniel',
22: 'Danilo',
23: 'Davi',
24: 'Diego',
25: 'Eduardo',
26: 'Elisa',
27: 'Enzo',
28: 'Esther',
29: 'Felipe',
30: 'Fernanda',
31: 'Flávia',
32: 'Francisco',
33: 'Gabriel',
34: 'Gabriela',
35: 'Giovanna',
36: 'Guilherme',
37: 'Gustavo',
38: 'Helena',
39: 'Henrique',
40: 'Igor',
41: 'Isabel',
42: 'Isabela',
43: 'Isadora',
44: 'Ivan',
45: 'João',
46: 'Júlia',
47: 'Juliana',
48: 'Laura',
49: 'Leonardo',
50: 'Letícia',
51: 'Lívia',
52: 'Lorena',
53: 'Lucas',
54: 'Luís',
55: 'Luíza',
56: 'Manuela',
57: 'Marcela',
58: 'Márcio',
59: 'Marco',
60: 'Marcos',
61: 'Maria',
62: 'Mariana',
63: 'Marina',
64: 'Mário',
65: 'Matheus',
66: 'Miguel',
67: 'Natália',
68: 'Nathália',
69: 'Nicole',
70: 'Otávio',
71: 'Pablo',
72: 'Patrícia',
73: 'Paulo',
74: 'Pedro',
75: 'Rafael',
76: 'Raquel',
77: 'Rebeca',
78: 'Renata',
79: 'Ricardo',
80: 'Roberto',
81: 'Rodrigo',
82: 'Samuel',
83: 'Sara',
84: 'Sofia',
85: 'Talita',
86: 'Tatiana',
87: 'Thiago',
88: 'Tiago',
89: 'Valéria',
90: 'Vanessa',
91: 'Vicente',
92: 'Victor',
93: 'Vinícius',
94: 'Vitor',
95: 'William',
96: 'Yago',
97: 'Yasmin',
98: 'Sérgio',
99: 'Maurício',
100: 'Cláudio'
}