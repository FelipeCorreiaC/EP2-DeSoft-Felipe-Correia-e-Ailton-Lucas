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