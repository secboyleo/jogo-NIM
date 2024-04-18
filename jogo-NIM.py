def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        jogada = n % (m + 1)
        if jogada == 0:
            return m
        else:
            return jogada


def usuario_escolhe_jogada(n, m):
    jogada = 0
    while jogada == 0:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada < 1 or jogada > m or jogada > n:
            print("Oops! Jogada inválida! Tente novamente.")
            jogada = 0
    return jogada


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m + 1) == 0:
        print("\nVocê começa!")
        proximo = "usuario"
    else:
        print("\nComputador começa!")
        proximo = "computador"

    while n > 0:
        if proximo == "usuario":
            jogada = usuario_escolhe_jogada(n, m)
            proximo = "computador"
        else:
            jogada = computador_escolhe_jogada(n, m)
            proximo = "usuario"

        n -= jogada
        print(f"\n{'' if proximo == 'usuario' else 'Computador'} tirou {jogada} peça{'s' if jogada > 1 else ''}.")
        print(f"Agora restam {n} peça{'s' if n > 1 else ''} no tabuleiro.")

    print(f"\n{'O computador ganhou!' if proximo == 'usuario' else 'Você ganhou!'}")
    return proximo


def campeonato():
    placar_usuario = 0
    placar_computador = 0
    rodada = 1

    while rodada <= 3:
        print(f"\n**** Rodada {rodada} ****\n")
        vencedor = partida()

        if vencedor == "Você ganhou!":
            placar_usuario += 1
        else:
            placar_computador += 1

        rodada += 1

    print("\n**** Final do campeonato! ****")
    print(f"\nPlacar: Você {placar_usuario} X {placar_computador} Computador")


def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    opcao = int(input())

    if opcao == 1:
        print("\nVocê escolheu uma partida isolada!")
        partida()
    elif opcao == 2:
        print("\nVocê escolheu um campeonato!")
        campeonato()
    else:
        print("\nOpção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
