from node import State, StatusGame, Node
# class to resolve by satisfacao restricao

class SatisfacaoRestricao:
    def __init__(self, graph):
        self.graph = graph

    def resolve(self):
        list_nodes_4 = self.get_nodes_by_state(State.P4, self.graph)
        list_rows_columns_iluminate = []
        for node in list_nodes_4:
            self.graph[node.row][node.column - 1].state = State.LANTERNA
            list_rows_columns_iluminate.append((node.row, node.column-1))
            self.graph[node.row][node.column + 1].state = State.LANTERNA
            list_rows_columns_iluminate.append((node.row, node.column+1))
            self.graph[node.row - 1][node.column].state = State.LANTERNA
            list_rows_columns_iluminate.append((node.row-1, node.column))
            self.graph[node.row + 1][node.column].state = State.LANTERNA
            list_rows_columns_iluminate.append((node.row+1, node.column))
        self.iluminate(list_rows_columns_iluminate, self.graph)
        stateResult, graphResult = self.backtracking(self.copy_graph(self.graph))
        if stateResult == StatusGame.CONCLUIDO:
            return graphResult
        return self.graph
    
    def backtracking(self, graph):
        graphResult = graph
        for i in range(len(graph)):
            for j in range(len(graph)):
                if self.check_new_lanterna(i, j, graph):
                    graph_copy = self.copy_graph(graph)
                    graph_copy[i][j].state = State.LANTERNA
                    self.iluminate([(i, j)], graph_copy)
                    # print("\ni e j:", i, j)
                    stateResultIntermediate, graphResultIntermediate = self.backtracking(graph_copy)
                    if stateResultIntermediate == StatusGame.CONCLUIDO:
                        return StatusGame.CONCLUIDO, graphResultIntermediate
        if not self.check_valid_graph(graph):
            return StatusGame.ERRO, graphResult
        return StatusGame.CONCLUIDO, graphResult
    
    def copy_graph(self, graph):
        graph_copy = []
        for i in range(len(graph)):
            linha = []
            for j in range(len(graph)):
                node = Node(graph[i][j].state, i, j, len(graph))
                linha.append(node)
            graph_copy.append(linha)
        return graph_copy
    
    def check_new_lanterna(self, i, j, graph):
        if graph[i][j].state != State.LIVRE:
            return False
        for vizinho in graph[i][j].list_vizinhos:
            if graph[vizinho[0]][vizinho[1]].state == State.P0:
                return False
            if graph[vizinho[0]][vizinho[1]].state == State.P1:
                for vizinhop in graph[vizinho[0]][vizinho[1]].list_vizinhos:
                    if graph[vizinhop[0]][vizinhop[1]].state == State.LANTERNA:
                        return False
            if graph[vizinho[0]][vizinho[1]].state == State.P2:
                count = 0
                for vizinhop in graph[vizinho[0]][vizinho[1]].list_vizinhos:
                    if graph[vizinhop[0]][vizinhop[1]].state == State.LANTERNA:
                        count += 1
                if count >= 2:
                    return False
            if graph[vizinho[0]][vizinho[1]].state == State.P3:
                count = 0
                for vizinhop in graph[vizinho[0]][vizinho[1]].list_vizinhos:
                    if graph[vizinhop[0]][vizinhop[1]].state == State.LANTERNA:
                        count += 1
                if count >= 3:
                    return False
        return True

    def check_valid_graph(self, graph):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if graph[i][j].state == State.LIVRE:
                    return False
        for nodep0 in self.get_nodes_by_state(State.P0, graph):
            for vizinho in nodep0.list_vizinhos:
                if graph[vizinho[0]][vizinho[1]].state == State.LANTERNA:
                    return False
        for nodep1 in self.get_nodes_by_state(State.P1, graph):
            count1 = 0
            for vizinho in nodep1.list_vizinhos:
                if graph[vizinho[0]][vizinho[1]].state == State.LANTERNA:
                    count1+=1
            if count1 != 1:
                return False
        for nodep2 in self.get_nodes_by_state(State.P2, graph):
            count2 = 0
            for vizinho in nodep2.list_vizinhos:
                if graph[vizinho[0]][vizinho[1]].state == State.LANTERNA:
                    count2+=1
            if count2 != 2:
                return False
        for nodep3 in self.get_nodes_by_state(State.P3, graph):
            count3 = 0
            for vizinho in nodep3.list_vizinhos:
                if graph[vizinho[0]][vizinho[1]].state == State.LANTERNA:
                    count3+=1
            if count3 != 3:
                return False
        return True
    
    def get_nodes_by_state(self, state, graph):
        list_nodes = []
        for i in range(len(graph)):
            for j in range(len(graph)):
                if graph[i][j].state == state:
                    list_nodes.append(graph[i][j])
        return list_nodes
    
    def iluminate(self, list_bulbs, graph):
        for bulb in list_bulbs:
            row = bulb[0]
            column = bulb[1]
            for i in range(row-1, -1, -1):
                if graph[i][column].state == State.LIVRE:
                    graph[i][column].state = State.ILUMINADO
                elif graph[i][column].state == State.ILUMINADO:
                    continue
                else:
                    break
            for i in range(row+1, len(graph)):
                if graph[i][column].state == State.LIVRE:
                    graph[i][column].state = State.ILUMINADO
                elif graph[i][column].state == State.ILUMINADO:
                    continue
                else:
                    break
            for j in range(column-1, -1, -1):
                if graph[row][j].state == State.LIVRE:
                    graph[row][j].state = State.ILUMINADO
                elif graph[row][j].state == State.ILUMINADO:
                    continue
                else:
                    break
            for j in range(column+1, len(graph)):
                if graph[row][j].state == State.LIVRE:
                    graph[row][j].state = State.ILUMINADO
                elif graph[row][j].state == State.ILUMINADO:
                    continue
                else:
                    break