def fazer_movimento(tabuleiro, origem, destino):
    #tuplas com coordenadas de origem e destino
    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino

    # Realiza o movimento
    #a peça que estava na posiição de origem é movido para destino (aqiu ler de trás pra frente)
    tabuleiro[linha_destino][coluna_destino] = tabuleiro[linha_origem][coluna_origem]
    #depois do movimento fica vazio
    tabuleiro[linha_origem][coluna_origem] = '.'

    # Se foi uma captura (movimento de 2 casas), remove a peça adversária
    #abs serve pra retirar o negativo do resultado, sempre será positivo
    #se resultado for igual a 2
    if abs(linha_destino - linha_origem) == 2:
        #após as médias encontradas
        meio_linha = (linha_origem + linha_destino) // 2
        meio_coluna = (coluna_origem + coluna_destino) // 2
        #elimina a peça pulada deixando o campo vazio (.)
        tabuleiro[meio_linha][meio_coluna] = '.'

def movimento_valido(tabuleiro, origem, destino, vez_jogador):
    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino

    # Verifica se a casa de destino está vazia '.'
    if tabuleiro[linha_destino][coluna_destino] != '.':
        return False
    
    # Verifica a direção do movimento com base na cor da peça
    #se for jogador das brancas, se for maior é jogada inválida
    if vez_jogador == 'w':
        if linha_destino >= linha_origem:
            return False
    #se for jogador das verdes, se for menor é jogada inválida
    elif vez_jogador == 'g':
        if linha_destino <= linha_origem:
            return False

    # Verifica se o movimento é diagonal comparando se resultado da subtração são iguais
    if abs(linha_destino - linha_origem) != abs(coluna_destino - coluna_origem):
        return False

    # Verifica se a peça está pulando uma peça adversária
    #dividindo por 2 garante a média das coordenadas de origem e destino
    meio_linha = (linha_origem + linha_destino) // 2
    meio_coluna = (coluna_origem + coluna_destino) // 2
    #se resultado da subtração for exatamente 2
    if abs(linha_destino - linha_origem) == 2:
        #se casa do meio for vazia '.' ou é a mesma cor do jogador da vez
        if tabuleiro[meio_linha][meio_coluna] == '.' or tabuleiro[meio_linha][meio_coluna] == vez_jogador:
            return False

    #retorna válido, se todos forem movimentos válidos
    return True
