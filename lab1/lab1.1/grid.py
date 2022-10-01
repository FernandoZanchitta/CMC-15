from turtle import right
import numpy as np
import random
from math import inf, sqrt

class CostMap(object):
    """
    Represents a cost map where higher values indicates terrain which are harder to transverse.
    """
    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.grid = np.ones((height, width))

    def get_cell_cost(self, i, j):

        return self.grid[i, j]

    def get_edge_cost(self, start, end):

        diagonal = (start[0] != end[0]) and (start[1] != end[1])
        factor = sqrt(2) if diagonal else 1.0
        return factor * (self.get_cell_cost(start[0], start[1]) + self.get_cell_cost(end[0], end[1])) / 2.0

    def is_occupied(self, i, j):

        return self.grid[i][j] < 0.0

    def is_index_valid(self, i, j):

        return 0 <= i < self.height and 0 <= j < self.width

    def add_obstacle(self, rectangle):

        self.add_rectangle(rectangle, -1.0)

    def add_rectangle(self, rectangle, value):

        left = rectangle[0]  - rectangle[2] // 2
        right = rectangle[0] + rectangle[2] // 2
        top = rectangle[1] - rectangle[3] // 2
        bottom = rectangle[1] + rectangle[3] // 2
        for j in range(left, right):
            for i in range(top, bottom):
                if self.is_index_valid(i, j) and not self.is_occupied(i, j):
                    self.grid[i, j] = value


    def create_exercise_map(self, obstacle_width, obstacle_height):

        GRIDBLOCK = [
        [1, 9],[1, 17],[1, 29],
        [3, 9],[3, 17],[3, 19],[3, 27],[3, 35],
        [5, 15],[5, 19],[5, 21],[5, 31],[5, 35],[5, 15],[7, 5],
        [7, 7],[7, 21],
        [9, 3],[9, 7],[9, 37],
        [11, 7],[11, 13],[11, 25],
        [13, 19],[13, 21],[13, 23],[13, 31],
        [15, 15],[15, 35],[15, 37],
        [17, 7],[17, 9],[17, 33],
        [19, 23],[19, 25],[19, 31],[19, 35],[19, 37],
        [21, 1],[21, 3],[21, 13],[21, 17],[21, 27],[21, 41],
        [23, 13],[23, 15],[23, 19],[23, 23],[23, 29],
        [25, 3],[25, 29],[25, 37],
        [27, 5],[27, 31],
        [29, 1],[29, 5],[29, 27],[29, 41],
        [33, 25],[33, 31],
        [35, 5],[35, 19],[35, 25],
        [37,25],[37,31],[37,35],
        [39,3],[39,7], [39,35],
        [41,17], [41, 35],[41,41],
        [43, 13],[43, 23],[43, 25],[43,33],[43, 37],
        [45,9], [45,19], [45,31], [45,35],
        [47, 1],[47, 3],[47, 11],[47,23],[47,27],

        ]
        for block in GRIDBLOCK:
            self.add_obstacle((block[0], block[1], obstacle_width, obstacle_height))

class NodeGrid(object):
    """
    Represents a grid of graph nodes used by the planning algorithms.
    """
    def __init__(self, cost_map):

        self.cost_map = cost_map
        self.width = cost_map.width
        self.height = cost_map.height
        self.grid = np.empty((self.height, self.width), dtype=Node)
        for i in range(np.size(self.grid, 0)):
            for j in range(np.size(self.grid, 1)):
                self.grid[i, j] = Node(i, j)

    def reset(self):

        for row in self.grid:
            for node in row:
                node.reset()

    def get_node(self, i, j):

        return self.grid[i, j]

    def get_successors(self, i, j):

        successors = []
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if [di,dj] != [0,0] and [di,dj] != [1,1] and [di,dj] != [-1,-1] and [di,dj] != [-1,1] and [di,dj] != [1,-1]:
                    if self.cost_map.is_index_valid(i + di, j + dj) and not self.cost_map.is_occupied(i + di, j + dj):
                        successors.append((i + di, j + dj))
        return successors


class Node(object):
    """
    Represents a node of a graph used for planning paths.
    """
    def __init__(self, i=0, j=0):

        self.i = i
        self.j = j
        self.f = inf
        self.g = inf
        self.closed = False
        self.parent = None

    def get_position(self):

        return self.i, self.j

    def set_position(self, i, j):

        self.i = i
        self.j = j

    def reset(self):

        self.f = inf
        self.g = inf
        self.closed = False
        self.parent = None

    def distance_to(self, i, j):

        return sqrt((self.i - i) ** 2 + (self.j - j) ** 2)

    def __lt__(self, another_node):
        if self.i < another_node.i:
            return True
        if self.j < another_node.j:
            return True
        return False

