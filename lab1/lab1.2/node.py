class State:
    """
    l = lanterna
    p = parede
    0 = zero lanterna ao redor
    1 = uma lanterna ao redor
    2 = duas lanterna ao redor
    3 = três lanterna ao redor
    4 = quatro lanterna ao redor
    '' = espaço em branco
    '_' = iluminado
    """
    LANTERNA = "l"
    PAREDE = "p"
    P0 = "0"
    P1 = "1"
    P2 = "2"
    P3 = "3"
    P4 = "4"
    LIVRE = ""
    ILUMINADO = "_"

class StatusGame:
    CONCLUIDO = "c"
    INCOMPLETO = "i"
    ERRO = "e"

class Node:
    def __init__(self, state, row, column, len_game):
        self.state = state
        self.row = row
        self.column = column
        self.list_vizinhos = []
        if row == 0:
            if column == 0:
                self.list_vizinhos.extend([(row, column+1), (row+1, column)])
            elif column == len_game-1:
                self.list_vizinhos.extend([(row, column-1), (row+1, column)])
            else:
                self.list_vizinhos.extend([(row, column-1), (row, column+1), (row+1, column)])
        elif row == len_game-1:
            if column == 0:
                self.list_vizinhos.extend([(row, column+1), (row-1, column)])
            elif column == len_game-1:
                self.list_vizinhos.extend([(row, column-1), (row-1, column)])
            else:
                self.list_vizinhos.extend([(row, column-1), (row, column+1), (row-1, column)])
        else:
            if column == 0:
                self.list_vizinhos.extend([(row, column+1), (row-1, column), (row+1, column)])
            elif column == len_game-1:
                self.list_vizinhos.extend([(row, column-1), (row-1, column), (row+1, column)])
            else:
                self.list_vizinhos.extend([(row, column-1), (row, column+1), (row-1, column), (row+1, column)])