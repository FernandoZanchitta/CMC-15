from grid import Node, NodeGrid
from math import inf
import heapq


class PathPlanner(object):
    """
    Represents a path planner, which may use Dijkstra, Greedy Search or A* to plan a path.
    """
    def __init__(self, cost_map):
        """
        Creates a new path planner for a given cost map.

        :param cost_map: cost used in this path planner.
        :type cost_map: CostMap.
        """
        self.cost_map = cost_map
        self.node_grid = NodeGrid(cost_map)

    @staticmethod
    def construct_path(goal_node):
        """
        Extracts the path after a planning was executed.

        :param goal_node: node of the grid where the goal was found.
        :type goal_node: Node.
        :return: the path as a sequence of (x, y) positions: [(x1,y1),(x2,y2),(x3,y3),...,(xn,yn)].
        :rtype: list of tuples.
        """
        node = goal_node
        # Since we are going from the goal node to the start node following the parents, we
        # are transversing the path in reverse
        reversed_path = []
        while node is not None:
            reversed_path.append(node.get_position())
            node = node.parent
        return reversed_path[::-1]  # This syntax creates the reverse list


    def a_star(self, start_position, goal_position):
        """
        Plans a path using A*.

        :param start_position: position where the planning stars as a tuple (x, y).
        :type start_position: tuple.
        :param goal_position: goal position of the planning as a tuple (x, y).
        :type goal_position: tuple.
        :return: the path as a sequence of positions and the path cost.
        :rtype: list of tuples and float.
        """
		# Todo: implement the A* algorithm
		# The first return is the path as sequence of tuples (as returned by the method construct_path())
		# The second return is the cost of the path
        self.node_grid.reset()
        node_start = self.node_grid.get_node(start_position[0], start_position[1])
        node_goal = self.node_grid.get_node(goal_position[0], goal_position[1])
        node_start.g = 0
        node_start.f = node_start.distance_to(goal_position[0], goal_position[1])
        pq = []
        heapq.heappush(pq, (node_start.f, node_start))
        while len(pq) > 0:
            current_distance, node = heapq.heappop(pq)
            if node.closed:
                continue
            node.closed = True

            if node.i == goal_position[0] and node.j == goal_position[1]:
                break
            # Check for the minimum distance and update in heapq
            for successor in self.node_grid.get_successors(node.i, node.j):
                child = self.node_grid.get_node(successor[0], successor[1])
                if child.closed:
                    continue
                if child.f > node.g + self.node_grid.cost_map.get_edge_cost([node.i, node.j], [child.i, child.j]) + child.distance_to(node_goal.i, node_goal.j):
                    child.g = node.g + self.node_grid.cost_map.get_edge_cost([node.i, node.j], [child.i, child.j])
                    child.f = child.g + child.distance_to(node_goal.i, node_goal.j)
                    child.parent = node
                    heapq.heappush(pq, (child.f, child))

        # get path from Start to goal:
        node_path = self.node_grid.get_node(goal_position[0], goal_position[1])
        path = self.construct_path(node_path)
        return path, node_path.f
