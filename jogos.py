def escolhe_jogo():

    import forca
    import adivinhacao

    print('Escolha seu jogo!')
    print('(1) Jogo da forca (2) Jogo da adivinhação')
    jogo = int(input('Qual o jogo? '))

    if jogo == 1:
        forca.jogar_forca()
    elif jogo == 2:
        adivinhacao.jogar_adivinhacao()

if (__name__ == '__main__'):
    escolhe_jogo()