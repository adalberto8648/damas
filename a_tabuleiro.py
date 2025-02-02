import tkinter as tk

# Constantes
TAMANHO_CASA = 60
LARGURA_TABULEIRO = 8 * TAMANHO_CASA
ALTURA_TABULEIRO = 8 * TAMANHO_CASA

# Cores
COR_CASA_CLARA = '#f0d9b5'
COR_CASA_ESCURA = '#b3651c'
COR_PECA_PRETA = '#000000'
COR_PECA_BRANCA = '#ffffff'

# Inicialização do tabuleiro
def criar_tabuleiro():
    tabuleiro = []
    for i in range(8):
        linha = []
        for j in range(8):
            if (i + j) % 2 == 1:
                if i < 3:
                    linha.append('P')  # Peças pretas
                elif i > 4:
                    linha.append('B')  # Peças brancas
                else:
                    linha.append('.')  # Casa vazia
            else:
                linha.append('.')  # Casa vazia
        tabuleiro.append(linha)
    return tabuleiro

# Função para desenhar o tabuleiro
def desenhar_tabuleiro(canvas, tabuleiro):
    canvas.delete("all")  # Limpa o tabuleiro antes de redesenhar
    for i in range(8):
        for j in range(8):
            x1, y1 = j * TAMANHO_CASA, i * TAMANHO_CASA
            x2, y2 = x1 + TAMANHO_CASA, y1 + TAMANHO_CASA
            cor = COR_CASA_CLARA if (i + j) % 2 == 0 else COR_CASA_ESCURA
            canvas.create_rectangle(x1, y1, x2, y2, fill=cor, outline=cor)

            if tabuleiro[i][j] == 'P':
                canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill=COR_PECA_PRETA, outline=COR_PECA_PRETA)
            elif tabuleiro[i][j] == 'B':
                canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill=COR_PECA_BRANCA, outline=COR_PECA_BRANCA)

# Função para mover peças
def mover_peca(tabuleiro, x1, y1, x2, y2):
    peca = tabuleiro[x1][y1]
    if peca == '.':
        return False  # Não há peça para mover

    if peca == 'P' and x2 <= x1:
        return False  # Peça preta não pode mover para trás
    if peca == 'B' and x2 >= x1:
        return False  # Peça branca não pode mover para frente

    if abs(x2 - x1) == 1 and abs(y2 - y1) == 1:
        if tabuleiro[x2][y2] == '.':
            tabuleiro[x1][y1] = '.'
            tabuleiro[x2][y2] = peca
            return True
    return False

# Função para comer peças
def comer_peca(tabuleiro, x1, y1, x2, y2):
    peca = tabuleiro[x1][y1]
    if peca == '.':
        return False  # Não há peça para mover

    if abs(x2 - x1) == 2 and abs(y2 - y1) == 2:
        x_meio, y_meio = (x1 + x2) // 2, (y1 + y2) // 2
        peca_meio = tabuleiro[x_meio][y_meio]
        if peca_meio != '.' and peca_meio != peca:
            tabuleiro[x1][y1] = '.'
            tabuleiro[x_meio][y_meio] = '.'
            tabuleiro[x2][y2] = peca
            return True
    return False

# Função para verificar movimentos obrigatórios
def verificar_movimentos_obrigatorios(tabuleiro, jogador, x=None, y=None):
    movimentos_obrigatorios = []
    
    # Se x e y forem passados, verifica apenas aquela peça específica
    casas_para_verificar = [(x, y)] if x is not None and y is not None else [
        (i, j) for i in range(8) for j in range(8) if tabuleiro[i][j] == jogador
    ]

    for i, j in casas_para_verificar:
        for dx, dy in [(-2, -2), (-2, 2), (2, -2), (2, 2)]:
            x2, y2 = i + dx, j + dy
            if 0 <= x2 < 8 and 0 <= y2 < 8:
                if comer_peca(tabuleiro, i, j, x2, y2):
                    movimentos_obrigatorios.append(((i, j), (x2, y2)))
                    # Desfaz a captura temporária
                    tabuleiro[i][j] = jogador
                    tabuleiro[(i + x2) // 2][(j + y2) // 2] = 'B' if jogador == 'P' else 'P'
                    tabuleiro[x2][y2] = '.'

    return movimentos_obrigatorios

# Função principal do jogo
def jogar_damas():
    root = tk.Tk()
    root.title("Jogo de Damas")

    canvas = tk.Canvas(root, width=LARGURA_TABULEIRO, height=ALTURA_TABULEIRO)
    canvas.pack()

    tabuleiro = criar_tabuleiro()
    desenhar_tabuleiro(canvas, tabuleiro)

    jogador_atual = 'P'  # Começa com as peças pretas
    selecionado = None  # Nenhuma peça selecionada inicialmente

    def on_click(event):
        nonlocal selecionado, jogador_atual
        x, y = event.x // TAMANHO_CASA, event.y // TAMANHO_CASA

        movimentos_obrigatorios = verificar_movimentos_obrigatorios(tabuleiro, jogador_atual)
        
        # Bloqueia movimentos normais se houver capturas obrigatórias
        if movimentos_obrigatorios and not any((y, x) == move[0] for move in movimentos_obrigatorios):
            print("Você deve capturar uma peça!")
            selecionado = None
            return

        if selecionado is None:
            if tabuleiro[y][x] == jogador_atual:
                selecionado = (y, x)
        else:
            y1, x1 = selecionado
            if (y, x) == (y1, x1):
                selecionado = None  # Desselecionar a peça
            else:
                if comer_peca(tabuleiro, y1, x1, y, x):
                    desenhar_tabuleiro(canvas, tabuleiro)

                    # Verifica se pode capturar novamente com a mesma peça
                    if verificar_movimentos_obrigatorios(tabuleiro, jogador_atual, y, x):
                        selecionado = (y, x)  # Continua jogando com a mesma peça
                    else:
                        jogador_atual = 'B' if jogador_atual == 'P' else 'P'  # Passa o turno
                        selecionado = None

                elif mover_peca(tabuleiro, y1, x1, y, x):
                    desenhar_tabuleiro(canvas, tabuleiro)
                    jogador_atual = 'B' if jogador_atual == 'P' else 'P'  # Passa o turno
                    selecionado = None
                else:
                    print("Movimento inválido!")
                    selecionado = None

    canvas.bind("<Button-1>", on_click)
    root.mainloop()

# Iniciar o jogo
jogar_damas()
