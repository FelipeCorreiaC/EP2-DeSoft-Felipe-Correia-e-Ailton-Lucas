def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])
    elif orientacao == "horizontal":
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    return posicoes


def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    for (r, c) in posicoes:
        if not (0 <= r <= 9 and 0 <= c <= 9):
            return False

    for tipo in frota:
        for navio in frota[tipo]:
            for (r_exist, c_exist) in navio:
                if [r_exist, c_exist] in posicoes:
                    return False

    return True
