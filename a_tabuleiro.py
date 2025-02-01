import tkinter as tk

#criando tabuleiro
def criar_tabuleiro():
    #criação da matriz 8x8, cada lugar será representando por '.'
    tabuleiro = [['.' for linha in range(8)] for coluna in range(8)]
    #as pretas ocupam as linhas 0, 1, 2
    for linha in range(3):
        for coluna in range(8):
            #só as casas escuras recebem peças (Verdes)
            if (linha + coluna) % 2 == 1:
                tabuleiro[linha][coluna] = 'g'
    #as brancas ocupam as linhas 5, 6, 7
    for linha in range(5, 8):
        for coluna in range(8):
            #só as casas escuras recebem peças (Brancas)
            if (linha + coluna) % 2 == 1:
                tabuleiro[linha][coluna] = 'w'
    return tabuleiro

#mostrando o tabuleiro
#canvas para desenhar o tabuleiro que do return do criar_tabuleiro
def mostrar_tabuleiro(canvas, tabuleiro):
    #tamanho de cada casa pixels
    tamanho_casa = 60
    #loop percorre as casa
    for linha in range(8):
        for coluna in range(8):
            #1 canto superior esquerdo do quadrado
            x1 = coluna * tamanho_casa
            #inversão pra exibição do formato correto
            y1 = (7 - linha) * tamanho_casa
            #2 canto inferior direito do quadrado
            x2 = x1 + tamanho_casa
            y2 = y1 + tamanho_casa
            #onde o cálculor for resto 0 fica branca, para criar o xadrez
            if (linha + coluna) % 2 == 0:
                cor = 'white'
            else:
                cor = 'black'
            #canvas criando os quadrados do tabuleiro
            canvas.create_rectangle(x1, y1, x2, y2, fill=cor, outline='white')
            #verifica se há uma peça na casa
            if tabuleiro[linha][coluna] == 'w':
                #desenha um círculo dentro da casa
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



