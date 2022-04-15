# DEASIFIO: GERENCIADOR DE TAREFAS
# DATA: 09/04/2022
# by SOUALEQUES (Alex Nascimento)©

tarefas = []
def arquivoExiste(nome):
    try:
        arquivo = open(nome, "rt")
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
if not arquivoExiste('tarefas.txt'):
    print('Arquivo nao existe... criando')
    arq = open('tarefas.txt', 'w+')
        
else:
    print('Arquivo ja existe.') 
    
      
def novaTarefa():
    add = str(input('NOVA TAREFA: '))
    tarefas.append(add)
    for tarefa in tarefas:
        with open('tarefas.txt', 'at') as arq:
            arq.write(f'{tarefa}\n')
            

def tarefaFeita():
    t = int(input('INDICE DA TAREFA FEITA: '))
    try:
        with open('tarefas.txt', 'rt') as fr:
            # reading line by line
            lines = fr.readlines()
            
            # pointer for position
            ptr = 0
        
            # opening in writing mode
            with open('tarefas.txt', 'w') as fw:
                for line in lines:
                    
                    # we want to remove 5th line
                    if ptr != t:
                        fw.write(line)
                    ptr += 1
        print("Deleted")
    except:
        print("Oops! someting error")
        
        
def verTarefas():
    print('-='*15)
    print('indice            tarefas')
    print('-='*15)
    arq = open('tarefas.txt', 'rt')
    for ind,linha in enumerate(arq):
        print(ind,       linha)
            
        
        
while True:
    print('-=' * 30)
    print('GERENCIADOR DE TAREFAS DO ALEX')
    print('-=' * 30)
    print()
    print('''1 - nova tarefa
2 - concluir tarefa
3 - ver tarefas
4 - sair''')
    escolha = int(input('ESCOLHA: '))
    if escolha == 1:
        novaTarefa()
    elif escolha == 2:
        tarefaFeita()
    elif escolha == 3:
        verTarefas()
    elif escolha == 4:
        break
    else:
        print('ERRO!')


