import tkinter as tk

def criar_tabuleiro():
    tabuleiro = [['.' for linha in range(8)] for coluna in range(8)]
    return tabuleiro

def mostrar_tabuleiro(canvas, tabuleiro):
    tamanho_casa = 60
    for linha in range(8): #percorre enumerando 0 a 7 , 8x
        for coluna in range(8): #percorre enumerando as colunas 0 a 7, 8x
            x1 = linha * tamanho_casa #percorre as 8 linhas multiplicando por 60
            y1 = coluna * tamanho_casa #percorre
            x2 = x1 + tamanho_casa
            y2 = y1 + tamanho_casa

            if (linha + coluna) % 2 == 0:
                cor = 'white'
            else:
                cor = 'black'
            canvas.create_rectangle(x1, y1, x2, y2, fill=cor, outline='gray')

def criar_janela():
    janela = tk.Tk()
    janela.title("Jogo de Damas")

    canvas = tk.Canvas(janela, width=480, height=480)
    canvas.pack()

    tabuleiro = criar_tabuleiro()
    mostrar_tabuleiro(canvas, tabuleiro)

    janela.mainloop()

criar_janela()


