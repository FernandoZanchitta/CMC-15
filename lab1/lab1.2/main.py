from node import Node
from sr import SatisfacaoRestricao
import time

def convert_to_node(GAME):
    tabuleiro = []
    for i in range(len(GAME)):
        linha = []
        for j in range(len(GAME)):
            node = Node(GAME[i][j], i, j, len(GAME))
            linha.append(node)
        tabuleiro.append(linha)
    return tabuleiro

def solve(game_matrix):
    tabuleiro = convert_to_node(game_matrix)
    resolve = SatisfacaoRestricao(tabuleiro)
    return resolve.resolve()

def print_graph(graph):
    for i in range(len(graph)):
        linha = []
        for j in range(len(graph)):
            linha.append(graph[i][j].state)
        print(linha, "\n")

# https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/lightup.html#7x7:d1iBb4eBa2e3bBi1d
FIRST_GAME = [['', '', '', '', '1', '', ''],
['', '', '', '', '', '', ''],
['p', '', '', '4', '', '', ''],
['', '', 'p', '', '2', '', ''],
['', '', '', '3', '', '', 'p'],
['', '', '', '', '', '', ''],
['', '', '1', '', '', '', '']]

# https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/lightup.html#7x7:i1aBcBc0dBd4c2c2aBi
SECOND_GAME = [['', '', '', '', '', '', ''],
['', '', '1', '', 'p', '', ''],
['', 'p', '', '', '', '0', ''],
['', '', '', 'p', '', '', ''],
['', '4', '', '', '', '2', ''],
['', '', '2', '', 'p', '', ''],
['', '', '', '', '', '', '']]

# https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/lightup.html#7x7:c1e3i1a1b0b1aBi4eBc
THIRD_GAME = [['', '', '', '1', '', '', ''],
['', '', '3', '', '', '', ''],
['', '', '', '', '', '1', ''],
['1', '', '', '0', '', '', '1'],
['', 'p', '', '', '', '', ''],
['', '', '', '', '4', '', ''],
['', '', '', 'p', '', '', '']]

TEST = [['', 'p', '', '', ''],
['', '', '', '', 'p'],
['', '', '', '', ''],
['1', '', '', '', ''],
['', '', '', '3', '']]

# LIST_GAME = [TEST, FIRST_GAME]
LIST_GAME = [FIRST_GAME, SECOND_GAME, THIRD_GAME]

for game in LIST_GAME:
    print("\n--------------------------------")
    print("\nPROBLEMA:\n")
    for line in game:
        print(line, "\n")
    ini = time.time()
    graph_solution = solve(game)
    fim = time.time()
    print("SOLUÇÃO:\n")
    print_graph(graph_solution)
    print("Tempo de execução(s): ", fim-ini)
    print("\n----------------------------------\n")