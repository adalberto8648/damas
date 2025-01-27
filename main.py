import tkinter as tk

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

#validar movimentos válidos
def movimento_valido(tabuleiro, origem, destino):
    linha_origen, coluna_origem = origem
    linha_destino, coluna_destino = destino

    if not (0 <= linha_destino < 8 and 0 <= coluna_destino < 8):
        return False
    if tabuleiro[linha_destino][coluna_destino] != '.':
        return False

    peca = tabuleiro[linha_origen][coluna_origem]
    if peca == 'w' and linha_destino == linha_origen + 1 and abs(coluna_destino - coluna_origem) == 1:
        return True
    if peca == 'g' and linha_destino -- linha_origen - 1 and abs(coluna_destino - coluna_origem) == 1:
        return True
        
    return False

    if abs(linha_destino - linha_origen) == 2 and abs(coluna_destino) == 2:
        linha_meio = (linha_origen + linha_destino) // 2
        coluna_meio = (coluna_origem + coluna_destino) // 2
        peca_capturada = tabuleiro[linha_meio][coluna_meio]
        if peca == 'w' and peca_capturada == 'g' and linha_destino == linha_origen + 2:
            return True
        if peca == 'g' and peca_capturada == 'w' and linha_destino == linha_origen - 2:
            return True

    return False

#detectar cliques no tabuleiro
peca_selecionada = None
def clique(event, canvas, tabuleiro):
    global peca_selecionada
    tamanho_casa = 60
    coluna = event.x // tamanho_casa
    linha = 7 - (event.y // tamanho_casa)

    if 0 <= linha < 8 and 0 <= coluna < 8:
        conteudo = tabuleiro [linha][coluna]
        if peca_selecionada is None:
            if conteudo in ['w', 'g']:
                peca_selecionada = (linha, coluna)
                print(f"Clique detectado na linha {linha}, coluna {coluna}")
        else:
            destino = (linha, coluna)
            if tabuleiro[destino[0]][destino[1]] == '.':
                peca = tabuleiro[peca_selecionada[0]][peca_selecionada[1]]
                tabuleiro[peca_selecionada[0]][peca_selecionada[1]] = '.'
                tabuleiro[destino[0]][destino[1]] = peca
                peca_selecionada = None
                canvas.delete("all")
                mostrar_tabuleiro(canvas, tabuleiro)
            else:
                print("movimento inválido. casa ocupada.")
                peca_selecionada = None

#criar a janela do jogo
def criar_janela():
    janela = tk.Tk()
    janela.title("Jogo de Damas")

    canvas = tk.Canvas(janela, width=480, height=480)
    canvas.pack()

    tabuleiro = criar_tabuleiro()
    mostrar_tabuleiro(canvas, tabuleiro)

    canvas.bind("<Button-1>", lambda event: clique(event, canvas, tabuleiro))

    janela.mainloop()

criar_janela()


