# DESAFIO: SIMULADOR DE DADOS.
# DATA: 11/04/2022
# by SOUALEQUES (Alex Nascimento do Carmo)©

    
from random import randint # importação da biblioteca para gerar os números aléatorios do(s) dado(s).
from time import sleep # importação da biblioteca para dar um tempo para aparecer os valores (para deixar mais legal)

print('-=' * 30)
print(f'\033[;1;33m{"SIMULADOR DE DADOS":^49}\033[m')
print('-=' * 30)

# Loop infinito onde acontece o programa
while True:
    try:
        res = int(input('Quer rodar 1 ou 2 dados!? '))
        if res == 1:
            dado_1 = randint(1,6)
            print(f'O valor do dado deu: ')
            sleep(1)
            print('.')
            sleep(1)
            print('.')
            sleep(1)
            print('.')
            sleep(1)
            print(f'-=-= \033[1;31m{dado_1}\033[m =-=-')
            sair = str(input('Quer rodar novamente? [S/N] ')).upper().strip()[0]
            while sair not in "SN":
                sair = str(input('Quer rodar novamente? [S/N] ')).upper().strip()[0]
            if sair == "S":
                pass
            elif sair == "N":
                break
        elif res == 2:
            dado_1 = randint(1,6)
            dado_2 = randint(1,6)
            print('O valor do dado 1 e dado 2 deu: ')
            sleep(1)
            print('.')
            sleep(1)
            print('.')
            sleep(1)
            print('.')
            sleep(1)
            print(f'-=-= \033[1;31m{dado_1}\033[m e \033[1;31m{dado_2}\033[m=-=-')
            sleep(0.5)
            print(f'Que somados dão: \033[1;32m{dado_1 + dado_2}\033[m')
            sair = str(input('Quer rodar novamente? [S/N] ')).upper().strip()[0]
            while sair not in "SN":
                sair = str(input('Quer rodar novamente? [S/N] ')).upper().strip()[0]
            if sair == "S":
                pass
            elif sair == "N":
                break
        # Tratamento de erro caso o usuario digite outro numero além de 1 ou 2.
        else:
            print('\033[1;31mERRO! digite somente 1 ou 2...\033[m')
    # Tratamento de erro caso o usuario digite algo além de numeros inteiros
    except ValueError:
        print('\033[1;31mDigite somente numeros inteiros!!!\033[m')
        
        
print('\033[1;33mFinalizando programa...\033[m')
sleep(1)
print('-=' * 30)
print(f'\033[;1;33m{"<< OBRIGADO POR JOGAR, VOLTE SEMPRE! >>":^59}\033[m')
print('-=' * 30)
