import tkinter as tk

#lógica da montagem
def criar_tabuleiro():
    tabuleiro = [['.' for linha in range(8)] for coluna in range(8)]

    for linha in range(3):
        for coluna in range(8):
            if (linha + coluna) % 2 == 1:
                tabuleiro[linha][coluna] = 'p'
    return tabuleiro

#exibição
def mostrar_tabuleiro(canvas, tabuleiro):
    tamanho_casa = 60
    for linha in range(8):
        for coluna in range(8):
            x1 = linha * tamanho_casa
            y1 = coluna * tamanho_casa
            x2 = x1 + tamanho_casa
            y2 = y1 + tamanho_casa

            #soma dos loops pra formar as cores
            if (linha + coluna) % 2 == 0:
                cor = 'white'
            else:
                cor = 'black'
            #montagem da grade pelo canvas
            canvas.create_rectangle(x1, y1, x2, y2, fill=cor, outline='gray')

            if tabuleiro[coluna][linha] == 'p' and cor == 'black':  # Se tiver uma peça preta
                canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill='white')

def criar_janela():
    janela = tk.Tk()
    janela.title("Jogo de Damas")

    canvas = tk.Canvas(janela, width=480, height=480)
    canvas.pack()

    tabuleiro = criar_tabuleiro()
    mostrar_tabuleiro(canvas, tabuleiro)

    janela.mainloop()

criar_janela()


