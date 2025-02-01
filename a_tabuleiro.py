import tkinter as tk
from b_movimentos import movimento_valido, fazer_movimento

#lógica da montagem
def criar_tabuleiro():
    tabuleiro = [['.' for linha in range(8)] for coluna in range(8)]
    for linha in range(3):
        for coluna in range(8):
            if (linha + coluna) % 2 == 1:
                tabuleiro[linha][coluna] = 'g'
    for linha in range(5, 8):
        for coluna in range(8):
            if (linha + coluna) % 2 == 1:
                tabuleiro[linha][coluna] = 'w'
    return tabuleiro

#exibição
def mostrar_tabuleiro(canvas, tabuleiro):
    tamanho_casa = 60
    for linha in range(8):
        for coluna in range(8):
            x1 = coluna * tamanho_casa
            y1 = (7 - linha) * tamanho_casa
            x2 = x1 + tamanho_casa
            y2 = y1 + tamanho_casa

            if (linha + coluna) % 2 == 0:
                cor = 'white'
            else:
                cor = 'black'

            canvas.create_rectangle(x1, y1, x2, y2, fill=cor, outline='white')

            if tabuleiro[linha][coluna] == 'w':
                canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill='green')
            elif tabuleiro[linha][coluna] == 'g':
                canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill='white')

#criar a janela do jogo
def criar_janela(clique):
    janela = tk.Tk()
    janela.title("Jogo de Damas")

    canvas = tk.Canvas(janela, width=480, height=480)
    canvas.pack()

    tabuleiro = criar_tabuleiro()
    mostrar_tabuleiro(canvas, tabuleiro)

    canvas.bind("<Button-1>", lambda event: clique(event, canvas, tabuleiro))

    janela.mainloop()



