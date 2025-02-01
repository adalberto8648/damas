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

def movimento_valido(tabuleiro, origem, destino):
    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino

    peca = tabuleiro[linha_origem][coluna_origem]  # Pega a peça na posição original

    # Imprime o estado do tabuleiro e as variáveis de origem e destino
    print(f"Tabuleiro: {tabuleiro}")
    print(f"Origem: {origem}, Destino: {destino}")
    print(f"Peça: {peca}, Casa de destino: {tabuleiro[linha_destino][coluna_destino]}")

    # Verifica se o destino está dentro do tabuleiro
    if not (0 <= linha_destino < 8 and 0 <= coluna_destino < 8):
        return False

    # Verifica se a casa de destino está vazia
    if tabuleiro[linha_destino][coluna_destino] != '.':
        return False

    # Verifica o movimento válido da peça
    if peca == 'g' and linha_destino == linha_origem + 1 and abs(coluna_destino - coluna_origem) == 1:
        return True
    if peca == 'w' and linha_destino == linha_origem - 1 and abs(coluna_destino - coluna_origem) == 1:
        return True

    # Verifica se é um movimento válido em linha diagonal para mais de uma casa
    if peca == 'g' and linha_destino > linha_origem and abs(coluna_destino - coluna_origem) == 1:
        return True
    if peca == 'w' and linha_destino < linha_origem and abs(coluna_destino - coluna_origem) == 1:
        return True

    return False





peca_selecionada = None
def clique(event, canvas, tabuleiro):
    global peca_selecionada
    tamanho_casa = 60
    coluna = event.x // tamanho_casa
    linha = 7 - (event.y // tamanho_casa)

    print(f"Click detectado na posição: ({linha}, {coluna})")

    if 0 <= linha < 8 and 0 <= coluna < 8:
        if peca_selecionada is None:
            if tabuleiro[linha][coluna] in ['w', 'g']:
                peca_selecionada = (linha, coluna)
                print(f"Peça selecionada: {peca_selecionada}")
        else:
            destino = (linha, coluna)
            print(f"Tentando mover para: {destino}")
            
            if movimento_valido(tabuleiro, peca_selecionada, destino):
                print("Movimento permitido!")
                
                # Mover a peça
                peca = tabuleiro[peca_selecionada[0]][peca_selecionada[1]]
                tabuleiro[peca_selecionada[0]][peca_selecionada[1]] = '.'
                tabuleiro[destino[0]][destino[1]] = peca
                
                # Se foi uma captura, remover a peça capturada
                if abs(peca_selecionada[0] - destino[0]) == 2:
                    linha_meio = (peca_selecionada[0] + destino[0]) // 2
                    coluna_meio = (peca_selecionada[1] + destino[1]) // 2
                    tabuleiro[linha_meio][coluna_meio] = '.'
                    print(f"Peça capturada em ({linha_meio}, {coluna_meio})")
                
                # Atualizar tabuleiro
                canvas.delete("all")
                mostrar_tabuleiro(canvas, tabuleiro)
            else:
                print("Movimento inválido!")

            peca_selecionada = None  # Resetar seleção




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


