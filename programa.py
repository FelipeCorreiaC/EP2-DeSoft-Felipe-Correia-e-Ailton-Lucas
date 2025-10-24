from funcoes import posicao_valida, preenche_frota

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
        valido = False
        while not valido:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
            linha = int(input())
            coluna = int(input())

            if nome == "submarino":
                orientacao = "horizontal"
            else:
                orientacao = input()
                if orientacao == "1":
                    orientacao = "vertical"
                elif orientacao == "2":
                    orientacao = "horizontal"

            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                valido = True
            else:
                print("Esta posição não está válida!")

print(frota)