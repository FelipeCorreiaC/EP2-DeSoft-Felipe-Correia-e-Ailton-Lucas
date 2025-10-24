def define_posicoes(linha, coluna, orientacao, tamanho):
    l_posicoes = []
    if orientacao == 'vertical':
        for i in range(tamanho):
            l_posicoes.append([linha + i, coluna])
    elif orientacao == 'horizontal':
        for i in range(tamanho):
            l_posicoes.append([linha, coluna + i])
    return l_posicoes


def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    
    if nome_navio not in frota:
        frota[nome_navio] = []
    
    frota[nome_navio].append(posicoes)
    
    return frota


def faz_jogada(tabuleiro, linha, coluna):

    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'

    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
        
    return tabuleiro


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


def afundados(frota, tabuleiro):
    navios_afundados = 0

    for navios in frota.values():
        for navio in navios:
            afundado = True
            for pos in navio:
                linha, coluna = pos
                if tabuleiro[linha][coluna] != 'X':
                    afundado = False
                    break
            if afundado:
                navios_afundados += 1

    return navios_afundados


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