import tkinter as tk

#lógica da montagem
def criar_tabuleiro():
    tabuleiro = [['.' for linha in range(8)] for coluna in range(8)]

    #posiciona peças brancas 'p'
    for linha in range(3):
        for coluna in range(8):
            if (linha + coluna) % 2 == 1:
                tabuleiro[linha][coluna] = 'p'
    
    #posiciona peças vermelhas 'r'
    for linha in range(5, 8):
        for coluna in range(8):
            if (linha + coluna) % 2 == 1:
                tabuleiro[linha][coluna] = 'r'

    return tabuleiro

#exibição
def mostrar_tabuleiro(canvas, tabuleiro):
    tamanho_casa = 60
    for linha in range(8):
        for coluna in range(8):
            x1 = coluna * tamanho_casa
            y1 = linha * tamanho_casa
            x2 = x1 + tamanho_casa
            y2 = y1 + tamanho_casa

            #soma dos loops pra formar as cores
            if (linha + coluna) % 2 == 0:
                cor = 'white'
            else:
                cor = 'black'

            #montagem da grade pelo canvas
            canvas.create_rectangle(x1, y1, x2, y2, fill=cor, outline='gray')

            #desenhar as peças brancas
            if tabuleiro[linha][coluna] == 'p':
                canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill='white')

            #desenhar as peças vermelhas
            elif tabuleiro[linha][coluna] == 'r':
                canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill='green')

def criar_janela():
    janela = tk.Tk()
    janela.title("Jogo de Damas")

    canvas = tk.Canvas(janela, width=480, height=480)
    canvas.pack()

    tabuleiro = criar_tabuleiro()
    mostrar_tabuleiro(canvas, tabuleiro)

    janela.mainloop()

criar_janela()


