import random


def imprime_titulo(txt):
    qtd_caracteres = int((40 - len(txt)) / 2)
    if len(txt) % 2 == 0:
        print('*' * 40)
        print('*' * qtd_caracteres + txt + '*' * qtd_caracteres)
        print('*' * 40)
    else:
        print('*' * 41)
        print('*' * (qtd_caracteres - 1) + txt + '*' * (qtd_caracteres + 3))
        print('*' * 41)

def carrega_palavra_secreta(nome_arquivo):

    arquivo = open(nome_arquivo, 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def mostra_letra_acertada(palavra):

    lista = ['_' for letra in palavra]

    return lista

def chute_usuario():
    chute = str(input('Digite a letra: '))
    chute = chute.strip().upper()
    return chute

def mostra_posicao_chute(letra_chute, letra_acertada, palavra_secreta):

    index = 0

    for letra in palavra_secreta:
        if letra_chute == letra:
            letra_acertada[index] = letra
        index += 1

def imprime_mensagem_ganhador():

    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):

    print("Game Over!!!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):

    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar_forca():

    imprime_titulo('Bem vindo ao jogo de forca')

    palavra_secreta = carrega_palavra_secreta('palavras.txt')

    letra_acertada = mostra_letra_acertada(palavra_secreta)

    print(letra_acertada)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:

        chute = chute_usuario()

        if chute in palavra_secreta:
            mostra_posicao_chute(chute, letra_acertada, palavra_secreta)

        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in letra_acertada

        print(letra_acertada)

    if acertou:
        imprime_mensagem_ganhador()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

if (__name__ == '__main__'):
    jogar_forca()