import platform 
import os

sistema_operacional = platform.system()

match sistema_operacional:
    case 'Linux':
        comando_sistema = 'clear'
    case 'Windows':
        comando_sistema = 'cls'

def limpar_tela():
    os.system(comando_sistema)

def erro_clear():
    print('Erro na leitura!')
    input('Aperte qualquer tecla para continuar')
    os.system(comando_sistema)