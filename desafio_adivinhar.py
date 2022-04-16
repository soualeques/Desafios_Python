# DEASIFIO: ADIVINHAÇÃO
# DATA: 09/04/2022
# by SOUALEQUES (Alex Nascimento)©

from random import randint,choices # importação para gerar o numero aleatório e escolher aleatóriamente uma frase das que criei.
from time import sleep # importação para dar um tempo nas respostas as tentativas do usúario a fim de criar um ar de jogo.

# tuplas com frases caso o usúario ganhe, chute um numero menor ou menor.
# usando a função choices para ela selecionar uma frase aleatória das tuplas.
frases_ganhou = choices(('Parabéns! Você acertou na mosca.',
         'Uau! Você é bom nisso mesmo, como adivinhou?!',
         'Nossa! como descobriu?!... você é o Sherlock Holmes?!',
         'Parabéns! número correto.'))
frases_menor = choices(('Hummm... um pouco menos.',
                      'Não foi dessa vez... tente um número menor',
                      'Número muito alto...tente um menor.'))
frases_maior = choices(('Número muito baixo... tente um maior.',
                      'Quase hein... tente um número maior.',
                      'Hummm... número muito baixo, tente um maior'))

# criado uma função com o código principal do jogo.
def jogo(numero_secreto, frase_ganhou, frase_menor, frase_maior, dificuldade):
        tentativas = 0
        while True:    
            try:    
                # a cada palpite do usúario o número de tentativas recebe ela mesma + 1
                jogador = int(input('\033[1;32mSua tentativa: \033[m'))
                print('\033[1;36m-=\033[m' * 30)
                tentativas += 1
                # variavel criada para criar função onde vai mostrar o número de tentativas restantes de acordo com a dificuldade escolhida.
                tent_faltantes = dificuldade - tentativas
                # caso o usúario chegue ao limite de tentativas o programa mostra a mensagem e para.
                if dificuldade == tentativas:
                    sleep(1)
                    print('\033[1;33mNão foi dessa vez, talvez tenha mais sorte na próxima\033[m')
                    break
                # caso o usúario acerte o número.
                if jogador == numero_secreto:
                    for frase in frase_ganhou:
                        sleep(1)
                        print(F'\033[1;32m{frase}\033[m')
                    break
                # caso o usúario chute um número maior
                elif jogador > numero_secreto:
                    for frase in frase_menor:
                        sleep(1)
                        print(F'\033[1;33m{frase}\033[m')
                    print(f'Faltam \033[1;31m{tent_faltantes}\033[m tentativas!')
                # caso o usúario chute um número menor
                elif jogador < numero_secreto:
                    for frase in frase_maior:
                        sleep(1)
                        print(F'\033[1;33m{frase}\033[m')
                    print(f'Faltam \033[1;31m{tent_faltantes}\033[m tentativas!')
                print('\033[1;36m-=\033[m' * 30)
                # irá perguntar se quer mais tentativas até acertar ou vhegar no limite de tentativas.
                res = str(input('Quer mais uma tentativa? [S/N]: ')).strip().upper()[0]
                while res not in "SN":
                    res = str(input('\033[1;31mERRO DE DIGITAÇÃO!...\033[mQuer mais uma tentativa? [S/N]: ')).strip().upper()[0]
                # se resposta for sim o código volta o loop.
                if res == "S":
                    continue
                # se resposta for não o loop será interrompido.
                elif res == "N":
                    sleep(1)
                    print('\033[1;33mTudo bem desistir... pelo menos você tentou :)\033[m')
                    break
            # tratamento de erros.
            except:
                print('\033[1;31;44mAÇÃO NÃO PERMITIDA!\033[m')
        # irá mostrar no final do loop o total de tentativas do usúario.        
        print(f"Número de tentativas: \033[1;36m{tentativas}\033[m.")

        
# randint para gerar o número inteiro secreto do jogo.
numero_secreto1 = randint(1,10)

# loop infinito para trabalhar a escolha de dificuldade do jogo.
while True:
    print('-=' * 30)
    print(f'\033[1;34m{"JOGO DA ADIVINHAÇÃO":^49}\033[m')
    print('-=' * 30)
    print()
    try:
        # usúario irá escolher o nível de dificuldade de acordo com os indices.
        dificuldade = int(input('''NIVEL DE DIFICULDADE:\n\033[1;32m1 para Fácil\033[m (tentativas = infinitas)
\033[1;33m2 para Normal\033[m (tentativas = 9)
\033[1;31m3 para Díficil\033[m (tentativas = 3)
    \nSUA ESCOLHA: '''))
        print('\033[1;36m-=\033[m' * 30)
        # dificuldade fácil com infinitas tentativas.
        if dificuldade == 1:
            print('\033[1;34mOlá! Sou seu computador...\nEstou pensando em um numero de 1 à 10, consegue adivinhar qual é?\033[m')
            jogo(numero_secreto1,frases_ganhou,frases_menor,frases_maior)
            print('\033[1;36m-=\033[m' * 30)
            res = str(input('quer jogar novamente? [S/N]: ')).strip().upper()[0]
            while res not in 'SN':
                res = str(input('\033[1;31mERRO DE DIGITAÇÃO...\033[mquer jogar novamente? [S/N]: ')).strip().upper()[0]
            if res == 'N':
                break
        # dificuldade normal com 9 tentativas, por isso foi criado a variavel "df" e colocado como parametro na função "jogo".
        elif dificuldade == 2:
            df = 9
            print('\033[1;34mOlá! Sou seu computador...\nEstou pensando em um numero de 1 à 10, consegue adivinhar qual é?\033[m')
            jogo(numero_secreto1,frases_ganhou,frases_menor,frases_maior, df)
            print('\033[1;36m-=\033[m' * 30)
            res = str(input('quer jogar novamente? [S/N]: ')).strip().upper()[0]
            while res not in 'SN':
                res = str(input('\033[1;31mERRO DE DIGITAÇÃO...\033[mquer jogar novamente? [S/N]: ')).strip().upper()[0]
            if res == 'N':
                break
        # dificuldade díficil com 3 tentativas, mesmo esquema da anterior.
        elif dificuldade == 3:
            df = 3
            print('\033[1;34mOlá! Sou seu computador...\nEstou pensando em um numero de 1 à 10, consegue adivinhar qual é?\033[1;34m')
            jogo(numero_secreto1,frases_ganhou,frases_menor,frases_maior, df)
            print('\033[1;36m-=\033[m' * 30)
            res = str(input('quer jogar novamente? [S/N]: ')).strip().upper()[0]
            while res not in 'SN':
                res = str(input('\033[1;31mERRO DE DIGITAÇÃO...\033[mquer jogar novamente? [S/N]: ')).strip().upper()[0]
            if res == 'N':
                break
        # tratamento de erro caso o usúario escolha um número além dos disponiveis.
        else:
            print('\033[1;31mERRO! ESCOLHA INVÁLIDA.\033[m')
    # tratamento de erro caso o usúario digite alguma tecla além de números inteiros.
    except ValueError:
        print('\033[1;31mERRO! aceiito apenas numeros inteiros :)\033[m')
    # tratamento de erro caso o usúario faça gambiarra de usar "Ctrl + C" para sair... dica que peguei na reunião dia 13/04/22 do grupo de projetos no telegram.
    # a próposito: obrigado pela dica hehe.
    except KeyboardInterrupt:
        print('\n\033[1;31mPROIBIDO sair assim hehe...\033[m')
#fim do programa com espera de 1 segundo e emoji no final :) .
print('Finalizando programa...')
sleep(1)
print('-=' * 30)
print(f'\033[1;34m{"FIM DO JOGO, OBRIGADO POR JOGAR!":^49}\U0001F601\033[m')
print('-=' * 30)