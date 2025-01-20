# def criar_tabuleiro():
#     tabuleiro = [['.' for _ in range(8)] for _ in range(8)]
#     return tabuleiro

def criar_tabuleiro():
    tabuleiro = [['.' for _ in range(8)] for _ in range(8)]
    return tabuleiro

def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(' '.join(linha))

tabuleiro = criar_tabuleiro()
mostrar_tabuleiro(tabuleiro)

