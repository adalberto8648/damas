from a_tabuleiro import mostrar_tabuleiro
from b_movimentos import movimento_valido, fazer_movimento

peca_selecionada = None
turno = 'w'

def clique(event, canvas, tabuleiro):
    global peca_selecionada, turno  # Tornar as variáveis globais
    tamanho_casa = 60
    coluna = event.x // tamanho_casa
    linha = event.y // tamanho_casa

    print(f"Click detectado na posição: ({linha}, {coluna})")

    if 0 <= linha < 8 and 0 <= coluna < 8:
        if peca_selecionada is None:
            if tabuleiro[linha][coluna] == turno:  # Verifica se a peça pertence ao jogador
                peca_selecionada = (linha, coluna)
                print(f"Peça selecionada: {peca_selecionada}")
        else:
            destino = (linha, coluna)
            print(f"Tentando mover para: {destino}")
            
            if movimento_valido(tabuleiro, peca_selecionada, destino, turno):
                print("Movimento permitido!")
                
                # Realiza o movimento
                fazer_movimento(tabuleiro, peca_selecionada, destino)
                print(f"Tabuleiro após movimento: {tabuleiro}")
                
                # Atualiza o turno
                turno = 'g' if turno == 'w' else 'w'

                # Atualizar tabuleiro
                canvas.delete("all")
                mostrar_tabuleiro(canvas, tabuleiro)
            else:
                print("Movimento inválido!")

            peca_selecionada = None  # Resetar seleção

