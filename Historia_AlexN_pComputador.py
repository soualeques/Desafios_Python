# DESAFIO: HISTÓRIA INTERATIVA
'''Imagine que você vai criar uma história onde o protagonista é a pessoa rodando o seu script
e cada pergunta respondida moverá a pessoa na sua história de acordo comina as condições que você determinar.
As possibilidades aqui são infinitas, você pode ter um jogo bem curto com poucos finais
ou uma árvore gigantesca de finais. Receba o valor do usuário e trate a resposta para que respostas não válidas
não quebrem o programa.
Você deverá permitir que o usuário tente novamente quanto ele chegar em um dos possíveis finais.
Encoraje que ele tente várias vezes para ver todos os possíveis finais.'''
# DATA INICIO: 23/04/2022
# by SOUALEQUES (Alex Nascimento do Carmo)©

# possivelmente será necessario instalar a biblioteca 'pyttsx3' (vá ao terminal e digite: "pip install pyttsx3")
import pyttsx3

# OOP para criar o jogo e melhorar o código
class Jogo:
    def __init__(self):
       # LISTA DE CORES PARA USAR PELOS INDICES.
        self.cor = [    '\033[1;30m', # preto
                        '\033[1;31m', # vermelho
                        '\033[1;32m', # verde
                        '\033[1;33m', # amarelo
                        '\033[1;34m', # azul
                        '\033[1;35m', # magenta
                        '\033[1;36m', # ciano
                        '\033[1;37m', # branco
                        '\033[m']     # fechar cor
        
# POSSIVEIS FRASES       
        self.frases = [
#0
f'''Você agora consegue enxergar melhor o que está a sua frente...
parece uma prisão em um tipo de caverna...assustado...
vê seu melhor amigo está acorrentado pelos pés a um tipo de cano...
e você também...O que você faz?''',
#1
f'''Ele diz que não se lembra de como chegou ali, só que estava bebendo em um bar e depois apagou,
quando viu estava aqui, faz mais de uma semana e ninguém aparece...estou faminto e não sei se vou aguentar mais um dia...disse ele...
O que você diz a ele?''',
#2
f'''Seu amigo então se acalma e vocês procuram pelo chão algo que possa ajudar vocês..
então você encontra uns pequenos pedaços de metais que podem usar como lockpick, tecnicas aprendidas na época dos escoteiros...
depois de um bom tempo, vocês estão libertos das correntes, e decidem revirar o local...
nas paredes...olhando mais de perto vocês encontram uma espécie de enigma que diziam que se resolvessem seriam soltos...''',
 #3 FIM 1
f'''Após descobrirem a charada, do nada uma certa parte da parede fica mole e eles então começam a bater nela...
fazendo um buraco e mostrando um tunel para fora da prisão...
eles com muita exaustão...atravessam o tunel e descobrem estar em uma ilha, onde tem um barco os esperando e uma carta...
que dizia:... Vocês foram meus escolhidos para meus teste... obrigado por participarem...e não morreram hahaha...
então vocês vão embora e procuram a polícia...contando tudo, quando voltam a ilha, não tinha nada...
se passaram por loucos... então...decidem procurar os dois por si só até encontrarem o responsável...e esse é o FIM!''',
#4
f'''Você fica esperto com seu amigo, ele começa agir estranho...do nada ele começa amorder sua perna, e te atacar...
vocês lutam e sem pensar...acidentalmente você usa a faca nele, e consequêntemente ele acaba morrendo...
depois de ver o corpo dele cheio de sangue por horas, aparece alguns homens com jalécos brancos e te soltam...
dizendo que issp era um experimento para testar o quanto uma pessoa pode aguentar até chegar ao canibalismo...
você foi só um rato de laboratório...disse eles... então você?''',
#5 FIM 2
f'''Ao entrar na sala de execução você ouve um tiroteio...muitos sons de tiros, então pronto para morrer...
chega um esquadrão da swat para te salvar e os outros iguais a você...
essa operação ocorria a anos mas somente agora encontramos eles...
disse o capitão da operação...e então você volta para casa, e diariamente vai a psicóloga para apagar tudo aquilo da memória...FIM!''',
#6 FIM 3
f'''Levado por dois guardas, você acerta um na garganta com a faca e rouba sua arma e atira no outro antes que ele reaja...
então você vai atrás de todos os cientistas que te prenderam e os fazem pagar...
tendo sua vingança completa, você acaba descobrindo que na verdade eles estavam tentando descobrir uma cura para um vírus onde transforma as pessoas em canibais...
e esse vírus afetou o mundo todo...restando poucos sobreviventes...
após tudo isso você se pergunta...Sou um herói ou vilão?...FIM!''',
#7
f'''Seu amigo vê você com a faca e diz para tomar cuidado, como previsto... as correntes não se partiram...
então você com raiva grita por socorro!... mas ninguem responde... porém alguém joga uma carta pela fechadura da porta da prisão...
o que você faz?''',
#8
f'''Na carta dizia o seguinte:...A sua única chance de escapar esta dentro do seu amigo...
para te ajudar deixei uma faca ai...que os selfs começem hahaha!... sem saber o que fazer você fica com medo de mostrar a carta para seu amigo que estava perguntando o que ela dizia...
entâo, o que você faz?''',
#9 FIM 4
f'''Você então esfaqueia seu amigo e faz brutalidades... até encotrar duas chaves...
uma para seu cadeado que prendia seu pé... outra devia ser para a porta... porém a chave não funcionava... ou seja...
você foi enganado!...então agora você ficará preso e ficará com o que fez na consiência...FIM!''',
#10 FIM 5
f'''Quando você mostrou...seu amigo ficou assustado...porém confiou em você por ter mostrado...
tentando de várias formas de fugir...se passaram horas...então aparece 2 homens mascárados, falando que um de nos poderá ir e o outro terá de ficar...
como você foi leal a seu amigo, ele me forçou a ir...então com agressividade os mascárados te doparam e você acordou em sua casa...
pensando se aquilo foi um sonho ou era real...FIM!''',
#11 FIM 6
f'''Você diz que a carta dizia apenas que não tinha saída, então seu amigo entristecido...
diz... que pena... você era um dos melhores...ele tira uma chave do bolso e se liberta...abre o portão...
e antes de ir embora e te deixar preso ele fala:...eu planejei isso para testar as pessoas... sua lealdade foi testada e você não passou...
Sinto muito...então o que restou a você foi ficar preso ou acabar com isso logo com a faca que tinha...FIM!''',
#12
f'''Com a visão mais clara da cela, você enxerga um barril encostado na parede... com passar do tempo...
quase acabando o dia, você decide revirar os bolsos, e encontra uma chave estranha...nunca vista antes...
aparentemente ela abre apenas um dos cadeados que prendem você e seu amigo... o que você faz?''',
#13 FIM 7
f'''Seu amigo agora esta liberto, e então ele do nada grita: COOOORRTA!, e então aparece vários caras engravatados e com armas na cintura...
seu amigo diz que é da CIA e isso era um teste de lealdade, onde você passou com exito, e agora tambem é um agente...
então vocês voltam para casa e se preparam para sua primeira missão...PARABÉNS agente!...FIM''',
#14
f'''Agora que você esta livre, você anda até o barril, e tem a idéia de empurra-lo, e vê um tunel escuro e tenebroso...
você cogita ir, todo animado você grita que achou uma saída e olha para seu amigo, mas ele acaba de falecer...
e com ele entre seus braços está uma carta... mas esta muito escuro para ler a carta ou para ver aonde o tunel da...
o que você faz?''',
#15 FIM 8
f'''A carta dizia o seguinte:...Caro amigo, você foi meu único amigo esse tempo todo por mais que a situação esteja díficil aqui...
sei que iremos achar uma saída juntos, eu não te abandono e nem você a mim... 
assinado: seu melhor amigo e irmão... (SIM...ele era seu irmão).. com sentimento abalado...
você desiste de encontrar uma saída e decide ficar ao lado de seu irmão...
pois ele era a única familia que tinha... não se sabe quanto tempo passou mas nínguem nunca mais soube de você...FIM!''',
#16 FIM 9
f'''Você se rasteja pelo tunel, o caminho é longo, se pergunta quem fez ele... com o fósforo quase apagando...
você vê uma luz...chegando mais perto... você se depara com alienigenas andando pelas ruas...
aparentemente vocês são prisioneiros deles...
com cautéla...você acerta um que estava distraido e rouba uma chave igual a que estava no seu bolso...
então você volta para libertar seu amigo... porém bem na hora eles abrem a cela e começam a disparar...
acabando com você e seu amigo...com um fechamento triste...aparentemente esse foi seu... FIM!''',
#17 FIM 10
f'''Você entra em um sono profundo e acorda em sua cama...
lembra que bebeu um pouco a mais na noite passada com seu melhor amigo...
Tudo era apenas um sonho!... e você então volta à sua vida normal... FIM!''',
#18
f'''Como fazia dias que seu amigo não se alimentava... ele acaba falecendo...
Você surtado começa Andar pelo lugar...
você encontra um tipo de siringa, ela está um pouco cheio mas não da importância...
você continua andando para ver uma saída e vê a porta da cela...tenta enxergar, porém não vê ninguem...
entediado... você começa a esfregar a faca na parede...logo após isso você ouve alguém gritando do outro lado...
então você:''',
#19
f'''Ela diz que é uma mulher e acordou numa cela escura e gelada...você diz o mesmo, então vocês começam a conversar e trocar informações pessoais...
onde logo após isso, ela mostra fazer parte disso...que estava apenas te enganando para saber mais sobre você e sua familia...
sem saber o que fazer...
você fica remoendo isso na cabeça, que foi enganado e agora sua família corre perigo...então, acidentalmente...
você derruba a seringa, que nela tinha uma mensagem escondida... dizendo... USA-ME...então você:''',
#20 FIM 11
f'''Ao usar a seringa você se sente meio estranho, então vai se apoiar na parede e com o mínimo de esforço a quebra...
você aparentemente ganhou poderes, e vai atrás da mulher que te enganou...
ao encontra-la... você a reconhece pela voz, e ela esta vestida com um jaléco, num laboratório...cheio de cientistas...
ela explica que aquilo era necessário para que você usa-se a seringa... este é um experimento da área cinquenta e um...
onde você concordou em apagarmos sua memória recente e testarmos a nossa nova fórmula do super-soldado...
depois da explicação você foi designado para uma missão ultra-secreta...e você acabou se tornando uma lenda para todo o exército...FIM!{self.cor[8]}''',
#21
f'''Não, eu que pergunto... disse ela, vocês conversam para passar o tempo, até que acham uma fresta entre sua cela e a dela...
pequena mas pode ver um ao outro... vocês continuam conversando por ali até chegar uma carta na cela de cada um...
você vai e lê a carta: que diz... Sua liberdade custa uma vida...
se tirar a vida dela, você estará livre... perto de você tem uma seringa... faça-a tomar, ela não é quem diz ser...
ela é uma assassina e merece morrer pelo que fez...se não fizer...irei atrás do seus parentes...então você:''',
#22 FIM 12
f'''Ela aceita tomar a seringa, desde que prometa que quando sair, irá cuidar da sua filha que não tem mais ninguém além dela...
você então promete e da a seringa atravéz da fresta... e assim foi feito... como prometido você foi solto e foi atrás da filha da mulher...
e foi a melhor coisa que aconteceu para você, você e a criança criaram uma conexão muito grande que fez esquecer tudo aquilo...
e acabou com a solidão que você tinha antes de tudo aquilo...FIM!''',
#23
f'''Ela confessa, mas explica que tudo que fez foi por sua filha... quem nos prendeu aqui é um velho inimigo meu... 
mas eu tenho um geito de escapar...disse ela...("você então ouve um barulho de luta na cela da mulher),..
assustado... você pergunta o que ouve... então do nada ela abre a sua porta e te tira de lá...
então você diz para escapar...porém ela pede sua ajuda para acabar com quem os prendeu aqui... então você:''',
#24 FIM 13
f'''Vocês vão com tudo pra cima do cara, você descobre que ele é um serial killer famoso procurado por toda FBI e antes dela matar ele...
ele diz:... finalmente acabou comigo parceira...
você então começa a surtar e sem pensar duas vezes pega uma arma e atira nela... mas como ela tem mais prática...
ela o acerta primeiro e o deixa morrer ali...dizendo... não era pra ser assim, sinto muito...FIM!''',
#25 FIM 14
f'''Voce decide fugir... e então...anos depois... você reencontra a mulher e sua filha... 
e vocês começam a conversar e criam uma relação muito boa, ela diz que o procurou por que foi a única pessoa que foi sinceira com ela mesmo numa prisão...
a questionando ao invés de força-la a morrer...
e isso valia muito pra ela...então vocês se conhecem melhor e assim termina a história...FIM!''']
# POSSIVEIS ESCOLHAS
        self.escolha = [
#0 
f'''{self.cor[3]}1 - PERGUNTAR A SEU AMIGO O QUE ACONTECEU.
2 - TENTAR CORTAR AS CORRENTES COM A FACA
3 - ACENDER OUTRO FOSFORO PARA VER SE O QUE TEM NO RESTO DA CELA.

escolha: {self.cor[8]}''',
#1
f'''{self.cor[3]}1 - CALMA, VAMOS ACHAR UMA SAÍDA.
2 - ESSA HISTÓRIA NÃO FAZ SENTIDO, VOCE ESTA MENTINDO PARA MIM.

escolha: {self.cor[8]}''',
#2
f'{self.cor[3]}O que é, o que é? Quanto mais se tira mais se aumenta.  DICA: "B_____"{self.cor[8]}',
#3
f'''{self.cor[3]}1 - ACEITA O FATO DE TER MATADO SEU AMIGO E SER EXECUTADO POR ELES.
2 - USA SUA FACA E TODAS HABILIDADES QUE GANHOU NO EXERCITO PARA MASSACRAR TODOS DAQUELE LUGAR.

escolha:{self.cor[8]} ''',
#4
f'''1 - ACENDE SEU ULTIMO FOSFORO E LÊ A CARTA.
2 - DEIXA SEU AMIGO LER A CARTA POIS VOCÊ ESTA UM POUCO SONOLENTO AINDA.
3 - VOCÊS DOIS LEEM A CARTA JUNTOS.

escolha: {self.cor[8]}''',
#5
f'''{self.cor[3]}1 - PRA ESCAPAR VALE TUDO!!!.
2 - MOSTRAR A CARTA PARA SEU AMIGO.
3 - MENTIR PARA SEU AMIGO.

escolha: {self.cor[8]}''',
#6
f'''{self.cor[3]}1 - LIBERTA SEU AMIGO, POIS ELE ESTA MAIS FRACO.
2 - SE LIBERTA PARA TENTAR ACHAR UMA SAÍDA.

escolha: {self.cor[8]}''',
#7
f'''{self.cor[3]}1 - USA O ÚLTIMO FÓSFORO PARA LER A CARTA.
2 - USA O ÚLTIMO FÓSFORO PARA VER AONDE ESSE TUNEL IRÁ DAR.

escolha: {self.cor[8]}''',
#8
f'''{self.cor[3]}1 - PERGUNTA QUEM ELA É
2 - PERGUNTA SE ELA ESTA FAZENDO ISSO COM VOCÊ

escolha: {self.cor[8]}''',
#9
f'''{self.cor[1]}1 - << USA A SERINGA! USA SERINGA!! USA SERINGA!!! >>{self.cor[8]}

{self.cor[3]}escolha: {self.cor[8]}''',
#10
f'''{self.cor[3]}1 - A CONVENCE A TOMAR A SERINGA
2 - PERGUNTA SE É VERDADE O QUE A CARTA DIZIA

escolha:{self.cor[8]} ''',
#11
f'''{self.cor[3]}1 - AJUDAR A MULHER
2 - FUGIR

escolha:{self.cor[8]} '''
]
        
# SISTEMA DE FALA        
    def falar(self,txt):
        self.fala = pyttsx3.init('sapi5')
        self.fala.setProperty('rate', 200)
        self.fala.say(txt)
        self.fala.runAndWait()
        print()
        print('-=' * 30)
# MENU INICIAL DO JOGO        
    def menu_inicial(self):
        while True:    
            try:   
                print('-=' * 30)
                print(f'{self.cor[3]}{"||  << O PRISIONEIRO >>   ||":^59}{self.cor[8]}')
                print('-=' * 30)
                print()
                print(f'''{self.cor[3]}1 - INICIAR HISTÓRIA...
2 - VER FINAIS CONQUISTADOS.{self.cor[8]}''')
                print()   
                opcao = int(input(f'{self.cor[3]}Sua escolha: {self.cor[8]}'))
                print('-=' * 30)
                if opcao == 1:
                                self.falar('ANTES DE COMEÇARMOS... ME DIGA SEU NOME E SEXO.')
                                self.jogador = str(input(f'{self.cor[3]}SEU NOME: {self.cor[8]}')).title()
                                self.sexo = str(input(f'{self.cor[3]}sexo: [M/F]{self.cor[8]} ')).strip().upper()[0]
                                if self.sexo not in "MF":
                                    self.sexo = str(input(f'{self.cor[1]}apenas M ou F{self.cor[8]}...sexo: [M/F] ')).strip().upper()[0]

                                self.iniciohistoria()
                                
                                self.falar(f'''{self.jogador}...{self.jogador}...acorda!... diz seu melhor amigo... meio grogue você acordou em um lugar frio e um pouco escuro...você não lembra de nada que aconteceu ou como chegou ali...a sua frente tem uma caixa de fósforo quase acabando e uma faca, O que você faz?''')
                                print(f'''{self.jogador}...{self.jogador}...acorda!... diz seu melhor amigo... meio grogue você acordou em um lugar frio e um pouco escuro...você não lembra de nada que aconteceu ou como chegou ali...a sua frente tem uma caixa de fósforo quase acabando e uma faca, O que você faz?''')
                                print('-=' * 30)
                elif opcao == 2:
                                pass
                else:
                                print(f'{self.cor[1]}OPÇÃO INVÁLIDA, FAVOR DIGITAR 1 OU 2 APENAS! {self.cor[8]}') 
            except KeyboardInterrupt:
                        print(f'{self.cor[1]}não permitimos SAIR assim!...você será levado ao menu inicial.{self.cor[8]}')
            except ValueError:
                        print(f'{self.cor[1]}valor NÃO aceito!{self.cor[8]}')       
# SABER O NOME E SEXO PARA DAR IMERSÃO AO JOGO                
    def iniciohistoria(self):
        try:
            if self.sexo == "M":
                self.falar(f'ESSA É A HISTÓRIA DO {self.jogador}!')
            elif self.sexo == "F":
                self.falar(f'ESSA É A HISTÓRIA DA {self.jogador}!')
        except KeyboardInterrupt:
                        print(f'{self.cor[1]}não permitimos SAIR assim!{self.cor[8]}')
        except ValueError:
                        print(f'{self.cor[1]}valor NÃO aceito!{self.cor[8]}')
# MOSTRA QUAL FINAL VOCÊ ESCOLHEU        
    def fimhistoria(self,txt):
        print('-=' * 30)
        print(f'{self.cor[3]}FINAL:{self.cor[8]}', end=" ")
        print(f'{self.cor[1]}{txt:^49}{self.cor[8]}')
        print('-=' * 30)
# CÓDIGO PRINCIPAL COM VARIOS IFs KKKK
    def prisioneiro(self):
        self.menu_inicial()
        print('-=' * 30)
        while True: 
            try:
                res = int(input(f'''{self.cor[3]}1 - ACENDER O FÓSFORO E GUARGAR A FACA.
2 - VOLTA A DORMIR.
3 - PROCURAR POR UMA SAÍDA E GUARDAR OS FÓSFOROS E A FACA PARA EMERGÊNCIA.

escolha:{self.cor[8]} '''))
        #---------==========================================- 1 -===================================================----------------------#
                if res == 1:
                            self.falar(self.frases[0])
                            print(self.frases[0])
                            print('-=' * 30)
                            res = int(input(self.escolha[0]))

                            if res == 1:
                                self.falar(self.frases[1])
                                print(self.frases[1])
                                print('-=' * 30)
                                res = int(input(self.escolha[1]))

                                if res == 1:
                                    self.falar(self.frases[2])
                                    print(self.frases[2])
                                    print('-=' * 30)
                                    res = str(input(self.escolha[2]))

                                    if res == "BURACO":
                                        self.falar(self.frases[3])
                                        print(self.frases[3])
                                        print('-=' * 30)
                                        self.fimhistoria('saindo como loucos')
                                        print(f'--== {self.cor[3]}{"1/14"}{self.cor[8]} ==--')
                                        break
                                    else:
                                        print(F'{self.cor[1]}EEEEHR... RESPOSTA DA CHARADA ERRADA!{self.cor[8]}')
                                elif res == 2:
                                    self.falar(self.frases[4])
                                    print(self.frases[4])
                                    print('-=' * 30)
                                    res = int(input(self.escolha[3]))

                                    if res == 1:
                                        self.falar(self.frases[5])
                                        print(self.frases[5])
                                        print('-=' * 30)
                                        self.fimhistoria('salvo pela SWAT')
                                        print(f'--== {self.cor[3]}{"2/14"}{self.cor[8]} ==--')
                                        break
                                    elif res == 2:
                                        self.falar(self.frases[6])
                                        print(self.frases[6])
                                        print('-=' * 30)
                                        self.fimhistoria('herói ou vilão?')
                                        print(f'--== {self.cor[3]}{"3/14"}{self.cor[8]} ==--')
                                        break
                                    else:
                                        print(F'{self.cor[1]}ESCOLHA INVALIDA!{self.cor[8]}')

                                else:
                                    print(F'{self.cor[1]}ESCOLHA INVALIDA!{self.cor[8]}')

                            elif res == 2:
                                self.falar(self.frases[7])
                                print(self.frases[7])
                                print('-=' * 30)
                                res = int(input(self.escolha[4]))
                                if res == 1:
                                    self.falar(self.frases[8])
                                    print(self.frases[8])
                                    print('-=' * 30)
                                    res = int(input(self.escolha[5]))
                                    if res == 1:
                                        self.falar(self.frases[9])
                                        print(self.frases[9])
                                        print('-=' * 30)
                                        self.fimhistoria('brutal')
                                        print(f'--== {self.cor[3]}{"4/14"}{self.cor[8]} ==--')
                                        break
                                elif res == 2:
                                    self.falar(self.frases[10])
                                    print(self.frases[10])
                                    print('-=' * 30)
                                    self.fimhistoria('forçado a ir embora')
                                    print(f'--== {self.cor[3]}{"5/14"}{self.cor[8]} ==--')
                                    break
                                elif res == 3:
                                    self.falar(self.frases[11])
                                    print(self.frases[11])
                                    print('-=' * 30)
                                    self.fimhistoria('reprovado no teste')
                                    print(f'--== {self.cor[3]}{"6/14"}{self.cor[8]} ==--')
                                    break
                                else:
                                    print(F'{self.cor[1]}ESCOLHA INVALIDA!{self.cor[8]}')

                            elif res == 3:
                                self.falar(self.frases[12])
                                print(self.frases[12])
                                print('-=' * 30)
                                res = int(input(self.escolha[6]))

                                if res == 1:
                                    self.falar(self.frases[13])
                                    print(self.frases[13])
                                    print('-=' * 30)
                                    self.fimhistoria('agente da CIA')
                                    print(f'--== {self.cor[3]}{"7/14"}{self.cor[8]} ==--')
                                    break
                                    
                                elif res == 2:
                                    self.falar(self.frases[14])
                                    print(self.frases[14])
                                    print('-=' * 30)
                                    res = int(input(self.escolha[7]))

                                    if res == 1:
                                        self.falar(self.frases[15])
                                        print(self.frases[15])
                                        print('-=' * 30)
                                        self.fimhistoria('adeus meu irmão')
                                        print(f'--== {self.cor[3]}{"8/14"}{self.cor[8]} ==--')
                                        break
                                        
                                    elif res == 2:
                                        self.falar(self.frases[16])
                                        print(self.frases[16])
                                        print('-=' * 30)
                                        self.fimhistoria('invasão alien')
                                        print(f'--== {self.cor[3]}{"9/14"}{self.cor[8]} ==--')
                                        break
                                else:
                                    print(F'{self.cor[1]}ESCOLHA INVALIDA!{self.cor[8]}')
                            else:
                                (F'{self.cor[1]}ESCOLHA INVALIDA!{self.cor[8]}')
        #---------==============================================- 2 -===================================================-----------------#    
                elif res == 2:
                            self.falar(self.frases[17])
                            print(self.frases[17])
                            print('-=' * 30)
                            self.fimhistoria('sonho ou real?')
                            print(f'--== {self.cor[3]}{"10/14"}{self.cor[8]} ==--')
                            break
        #---------===================================================- 3 -==============================================-----------------#
                elif res == 3:
                            self.falar(self.frases[18])
                            print(self.frases[18])
                            print('-=' * 30)
                            res = int(input(self.escolha[8]))
                            
                            if res == 1:
                                self.falar(self.frases[19])
                                print(self.frases[19])
                                print('-=' * 30)
                                res = int(input(self.escolha[9]))
                                
                                if res == 1:
                                    self.falar(self.frases[20])
                                    print(self.frases[20])
                                    print('-=' * 30)
                                    self.fimhistoria('super poderes')
                                    print(f'--== {self.cor[3]}{"11/14"}{self.cor[8]} ==--')
                                    break
                                else:
                                    print(F'{self.cor[1]}ESCOLHA INVALIDA!{self.cor[8]}')
                                    
                            elif res == 2:
                                self.falar(self.frases[21])
                                print(self.frases[21])
                                print('-=' * 30)
                                res = int(input(self.escolha[10]))
                                
                                if res == 1:
                                    self.falar(self.frases[22])
                                    print(self.frases[22])
                                    print('-=' * 30)
                                    self.fimhistoria('comprindo a promessa')
                                    print(f'--== {self.cor[3]}{"12/14"}{self.cor[8]} ==--')
                                    break
                                elif res == 2:
                                    self.falar(self.frases[23])
                                    print(self.frases[23])
                                    print('-=' * 30)
                                    res = int(input(self.escolha[11]))
                                    
                                    if res == 1:
                                        self.falar(self.frases[24])
                                        print(self.frases[24])
                                        print('-=' * 30)
                                        self.fimhistoria('não era para ser assim')
                                        print(f'--== {self.cor[3]}{"13/14"}{self.cor[8]} ==--')
                                        break
                                    elif res == 2:
                                        self.falar(self.frases[25])
                                        print(self.frases[25])
                                        print('-=' * 30)
                                        self.fimhistoria('o reencontro')
                                        print(f'--== {self.cor[3]}{"14/14"}{self.cor[8]} ==--')
                                        break
                                    else:
                                        print(F'{self.cor[1]}ESCOLHA INVALIDA!{self.cor[8]}')
                                else:
                                    print(F'{self.cor[1]}ESCOLHA INVALIDA{self.cor[8]}')
                            else:
                                print(F'{self.cor[1]}ESCOLHA INVALIDA{self.cor[8]}')
                else:
                    print(F'{self.cor[1]}ESCOLHA INVALIDA!{self.cor[8]}')
            except ValueError:
                    print(f'{self.cor[1]}valor NÃo aceito!{self.cor[8]}')
                    continue
            except KeyboardInterrupt:
                    print(f'{self.cor[1]}não permitimos SAIR assim!{self.cor[8]}')
                    continue
# CHAMADA DA CLASSE                
prision = Jogo()
# LOOP PARA VER SE O JOGADOR QUER TENTAR MAIS UMA VEZ
while True:
    prision.prisioneiro()
    print()
    print('-=' * 30)
    r = str(input(f'{prision.cor[3]}VOLTAR AO MENU PARA DESCOBRIR OUTROS FINAIS? [S/N]:{prision.cor[8]} ')).strip().upper()[0]
    while r not in "SN":
        r = str(input(f'{prision.cor[3]}ERRO DE DIGITAÇÃO!...QUER VOLTAR AO MENU PARA DESCOBRIR OUTROS FINAIS? [S/N]: {prision.cor[3]}')).strip().upper()[0]
    if r == "N":
        break
    
