# DEASIFIO: CADASTRO PESSOAS
# DATA: 09/04/2022
# by SOUALEQUES (Alex Nascimento)©

print('-=' * 30)
print(f'{"CADASTRO DE PESSOAS":^60}')
print('-=' * 30)

#criação do dicionario e da lista para guardar os dados
dados_cadastrados = {}
dados = []

# Coleta de informações.
while True:
    # limpa os dados após o término do ciclo.
    dados_cadastrados.clear()
    dados_cadastrados['NOME']= str(input('NOME: ')).strip()
    dados_cadastrados['IDADE']= int(input('IDADE: '))
    dados_cadastrados['SEXO']= str(input('SEXO [M/F]: ')).strip().upper()[0]
    # validação do Sexo.
    while dados_cadastrados['SEXO'] not in "FM":
        dados_cadastrados['SEXO'] = str(input('\033[1;31merro de digitação!...\033[m SEXO [M/F]: ')).strip().upper()[0]
    dados_cadastrados['CIDADE']= str(input('CIDADE: ')).strip().title()
    # adiciona uma cópia do dicionario à lista.
    dados.append(dados_cadastrados.copy())
    res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    # validação da resposta do usúario para continuar ou não.
    while res not in 'SN':
        res = str(input('\033[1;31merro de digitação!...\033[m  Quer continuar? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
    
# apresentação dos dados 1
print('\033[4;35m-=\033[m' * 35)
print(dados)
print('\033[4;35m-=\033[m' * 35)
# apresentação dos dados 2
for i, pessoas in enumerate(dados):
    print(f'\033[1;33mPessoa\033[m', i+1, pessoas)
print('\033[4;35m-=\033[m' * 36)



    