def movimento_valido(tabuleiro, origem, destino, turno):
    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino

    # Verifica se a célula de destino está vazia
    if tabuleiro[linha_destino][coluna_destino] != '.':
        return False
    
    # Verifica a direção do movimento com base na cor da peça
    if turno == 'w':  # Se for o jogador 'w' (branco)
        if linha_destino >= linha_origem:  # A peça não pode ir para trás
            return False
    elif turno == 'g':  # Se for o jogador 'g' (preto)
        if linha_destino <= linha_origem:  # A peça não pode ir para trás
            return False

    # Verifica se o movimento é diagonal (só movimentos diagonais são permitidos)
    if abs(linha_destino - linha_origem) != abs(coluna_destino - coluna_origem):
        return False

    # Verifica se a peça está pulando uma peça adversária
    meio_linha = (linha_origem + linha_destino) // 2
    meio_coluna = (coluna_origem + coluna_destino) // 2
    if abs(linha_destino - linha_origem) == 2:  # Verifica se a peça está pulando
        if tabuleiro[meio_linha][meio_coluna] == '.' or tabuleiro[meio_linha][meio_coluna] == turno:
            return False  # Não pode pular se o meio estiver vazio ou se a peça no meio for do mesmo jogador

    return True  # Se todas as condições forem atendidas, o movimento é válido


def fazer_movimento(tabuleiro, origem, destino):
    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino

    # Realiza o movimento
    tabuleiro[linha_destino][coluna_destino] = tabuleiro[linha_origem][coluna_origem]
    tabuleiro[linha_origem][coluna_origem] = '.'

    # Se foi uma captura (movimento de 2 casas), remove a peça adversária
    if abs(linha_destino - linha_origem) == 2:
        meio_linha = (linha_origem + linha_destino) // 2
        meio_coluna = (coluna_origem + coluna_destino) // 2
        tabuleiro[meio_linha][meio_coluna] = '.'  # Remove a peça adversária

