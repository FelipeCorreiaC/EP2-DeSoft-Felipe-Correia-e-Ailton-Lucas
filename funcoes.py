def posiciona_frota(frota):
    tabuleiro = []

    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tabuleiro.append(linha)

    for navios in frota.values():
        for navio in navios:
            for pos in navio:
                linha, coluna = pos
                tabuleiro[linha][coluna] = 1

    return tabuleiro