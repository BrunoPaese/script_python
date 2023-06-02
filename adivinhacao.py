def jogar_adivinhacao():

    import random

    numero_secreto = random.randrange(101)
    total_de_tentativas = 0
    pontos = 1000

    print('Selecione o nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Define o nível: '))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for i in range(1, total_de_tentativas + 1):

        chute = int(input('Digite um número entre 1 e 100: '))

        if chute < 1 or chute > 100:
            print('Você deve digitar um número entre 1 e 100')
            continue
        elif numero_secreto == chute:
            print('Você acertou! Fez {} pontos'.format(pontos))
            break
        else:
            print('Você errou!')

            if chute < numero_secreto:
                print('O número secreto é maior que {}. Tentativa {} de {}'.format(chute, i, total_de_tentativas))
                if i == total_de_tentativas:
                    print('O número secreto era {} e você fez {} pontos.'.format(numero_secreto, pontos))
            else:
                print('O número secreto é menor que {}. Tentativa {} de {}'.format(chute, i, total_de_tentativas))
                if i == total_de_tentativas:
                    print('O número secreto era {} e você fez {} pontos.'.format(numero_secreto, pontos))

            pontos_perdidos = abs((numero_secreto - chute))
            pontos = pontos - pontos_perdidos

    print('Fim de jogo!')

if (__name__ == '__main__'):
    jogar_adivinhacao()





