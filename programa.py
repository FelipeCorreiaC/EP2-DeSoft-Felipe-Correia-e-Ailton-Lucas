from funcoes import define_posicoes, preenche_frota, posicao_valida

def posiciona_frota_interativa():
    frota = {
        "porta-aviões": [],
        "navio-tanque": [],
        "contratorpedeiro": [],
        "submarino": []
    }

    configuracao = [
        ("porta-aviões", 4, 1),
        ("navio-tanque", 3, 2),
        ("contratorpedeiro", 2, 3),
        ("submarino", 1, 4)
    ]

    for nome, tamanho, quantidade in configuracao:
        for n in range(quantidade):
            while True:
                print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
                linha = int(input("Linha: "))
                coluna = int(input("Coluna: "))

                if nome == "submarino":
                    orientacao = "horizontal"
                else:
                    op = input("[1] Vertical [2] Horizontal > ")
                    orientacao = "vertical" if op.strip() == "1" else "horizontal"

                if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                    preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                    break
                else:
                    print("Esta posição não está válida!")

    print(frota)


if __name__ == "__main__":
    posiciona_frota_interativa()