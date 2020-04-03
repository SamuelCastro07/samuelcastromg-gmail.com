# Esse arquivo consiste no jogo "DA FORCA"
# Esse arquivo depende do arquivo externo chamado "listadeanimais.txt"

from random import randint, random
from time import sleep
import emoji

brincar = str(input('QUER BRINCAR COMIGO? S/N: ')).upper()

if brincar == 'S':

    print('{:=^40}'.format(' DÊ START DIGITANDO O NÚMERO DA OPÇÃO: '))
    brincadeira = int(input('''
    [ 1 ] START - JOGO DA FORCA
    '''))

    # =============== BRINCADEIRA 04 ===============
    if brincadeira == 1:
        #
        # Abre o arquivo com todas as palavras do jogo a serem adivinhadas
        #
        with open("listadeanimais.txt", "r", encoding="UTF-8") as f:   # arquivo chamado "listadeanimais.txt", no modo de "r" read (leitura), encoding="UTF-8", para arrumar problemas de acentuação
            palavras = f.readlines() #lê todas as linhas
            f.close() # fecha o arquivo
        #
        # esse tipo de looping é chamado do "list comprehension"
        # ele está fazendo a função de retirar todos os '/n' (quebras de linha) do arquivo.
        #
        palavras = [x.rstrip('\n').lower() for x in palavras] 

        #
        # selecionando uma posição aleatória do vetor para ser a palavra a ser adivinhada
        #

        plv = palavras[int(random() * len(palavras))]

        #
        # remove espaços repetidos, entretanto strip() serve para mais coisas
        #
        plv = plv.strip()

        #
        # Dados a serem exibidos para os usuários
        #
        dica = "Animal" # a dica do usuário
        vidas = 5 # quantidade de vida inicial
        restantes = [] # As letras que ainda estão em branco
        teclas = [] #teclas que ja foram digitadas
        
        #
        # Colocando os espaçamentos em branco a serem mostrados para o usuário adivinhar
        #

        for x in plv:
            if x != '-' or x != ' ':
                restantes.append("__")
            else:
                restantes.append(x) #caso tenha algum traço (palavras compostas) ou algum espaço ele seja adicionado

        #
        # iniciando o game
        # Mostrando os dados iniciais
        #

        print("Forca selecionada\n")
        print("!!! LEMBRETE !!!\n Letras com acento estão valendo\n!!! LEMBRETE !!!\n")
        print("\nDica: {}".format(dica))
        print("Vidas restantes: {}".format(vidas))

        #
        # Inicio do looping do game
        #
        while True:
            #
            # Primeiros 2 ifs de conclusão de jogo (perde e ganha)
            #
            
            if "".join(restantes) == plv: # o comando join serve pra transformar ['1','2','3'] em '123'.
                print("\n==========================================")
                print("=============Você GANHOU !! ==============")
                print("==========================================\n")
                break #encerra o looping, logo o jogo acaba

            if vidas <= 0:
                print("\n!!!!Game Over!!!!\n")
                print("A palavra era '{}'\n".format("".join(plv))) # o comando join serve pra transformar ['1','2','3'] em '123'. 
                break #encerra o looping, logo o jogo acaba

            #
            # Informações atualizadas
            #

            print("Teclas digitadas {}\n".format(teclas))
            print("\t{}".format(restantes))

            #
            # Espera o usuário digitar uma tecla
            #

            tecla = str(input("\nDigite uma tecla >> ")).lower() # comando lower() serve para transformar "UP" em "up"

            #
            # verifica se a tecla ja existe no vetor 'teclas'
            #

            if tecla in teclas:
                print("tecla repetida")
                continue # se sim, ele reseta o looping e não perde ponto

            #
            # verifica se a palavra contem a letra digitada
            #

            if tecla in plv: # se sim, adiciona nas teclas digitadas
                teclas.append(tecla)
                for x in range(0, len(plv)): # verifica em quais pontos que essa letra existe, e vai substituindo os espaços em branco por letras
                    if tecla == plv[x]:
                        restantes[x] = tecla # substitui espaço em branco por letras
            else: #senao, remove uma vida
                teclas.append(tecla) # adiciona a letra
                print("Letra Errada :(")
                vidas = vidas - 1 # perde uma vida
                print("----> Vidas restantes: {} <----\n".format(vidas)) #printa as vidas restantes

    else:
        print('Opção inválida!')

else:
    print(emoji.emojize('Tudo bem! Outra hora nós jogamos. :expressionless:', use_aliases=True))

