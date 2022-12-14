from os import minor
from turtle import width
import numpy as np
import matplotlib.pyplot as plt
from path_planner import PathPlanner
from grid import CostMap
from math import inf
import random
import time

# Select planning algorithm
algorithm = 'a_star'

# Number of path plannings used in the Monte Carlo analysis
num_iterations = 1
# num_iterations = 100  # Monte Carlo

# Plot options
save_fig = True  # if the figure will be used to the hard disk
show_fig = True  # if the figure will be shown in the screen
fig_format = 'png'
# Recommended figure formats: .eps for Latex/Linux, .svg for MS Office, and .png for easy visualization in Windows.
# The quality of .eps and .svg is far superior since these are vector graphics formats.


def plot_path(cost_map, start, goal, path, filename, save_fig=True, show_fig=True, fig_format='png'):
    """
    Plots the path.

    :param cost_map: cost map.
    :param start: start position.
    :param goal: goal position.
    :param path: path obtained by the path planning algorithm.
    :param filename: filename used for saving the plot figure.
    :param save_fig: if the figure will be saved to the hard disk.
    :param show_fig: if the figure will be shown in the screen.
    :param fig_format: the format used to save the figure.
    """
    plt.matshow(cost_map.grid)
    ax = plt.gca()
    # minor_ticks_height = np.arange(0, HEIGHT, 2)
    # minor_ticks_width = np.arange(0, WIDTH, 2)

    # major_ticks_height = np.arange(0, HEIGHT, 10)
    # major_ticks_width = np.arange(0, WIDTH, 10)

    # ax.set_xticks(minor_ticks_width,minor = True)
    # ax.set_yticks(minor_ticks_height,minor = True)
    # ax.set_xticks(major_ticks_height,major = True)
    # ax.set_yticks(major_ticks_width,major = True)
    # ax.grid(which='both')

    x = []
    y = []
    for point in path:
        x.append(point[1])
        y.append(point[0])
    plt.plot(x, y, linewidth=1)
    plt.plot(start[1], start[0], 'y*', markersize=5)
    plt.plot(goal[1], goal[0], 'rx', markersize=5)

    plt.xlabel('x / j')
    plt.ylabel('y / i')
    if 'dijkstra' in filename:
        plt.title('Dijkstra')
    elif 'greedy' in filename:
        plt.title('Greedy Best-First')
    else:
        plt.title('A*')

    if save_fig:
        plt.savefig('%s.%s' % (filename, fig_format), format=fig_format)

    if show_fig:
        plt.show()

    plt.close()


# Environment's parameters
WIDTH = 49
HEIGHT = 43
OBSTACLE_WIDTH = 2
OBSTACLE_HEIGHT = 2
NUM_OBSTACLES = 70

cost_map = CostMap(WIDTH, HEIGHT)
# Initializing the random seed so we have reproducible results
# Please, do not change the seed
random.seed(23)
# Create a random map

# cost_map.create_random_map(OBSTACLE_WIDTH, OBSTACLE_HEIGHT, NUM_OBSTACLES)
cost_map.create_exercise_map(OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
# Create the path planner using the cost map
path_planner = PathPlanner(cost_map)
# These vectors will hold the computation time and path cost for each iteration,
# so we may compute mean and standard deviation statistics in the Monte Carlo analysis.
times = np.zeros((num_iterations, 1))
costs = np.zeros((num_iterations, 1))
for i in range(num_iterations):
    problem_valid = False
    while not problem_valid:
        # Trying to generate a new problem
        start_position = (1, 1)
        goal_position = (41,47)
        # If the start or goal positions happen to be within an obstacle, we discard them and
        # try new samples
        if cost_map.is_occupied(start_position[0], start_position[1]):
            continue
        if cost_map.is_occupied(goal_position[0], goal_position[1]):
            continue
        if start_position == goal_position:
            continue
        problem_valid = True
    tic = time.time()
    path, cost = path_planner.a_star(start_position, goal_position)
    # if path is not None and len(path) > 0:
    path_found = True
    toc = time.time()
    times[i] = toc - tic
    costs[i] = cost
    plot_path(cost_map, start_position, goal_position, path, '%s_%d' % (algorithm, i), save_fig, show_fig, fig_format)


# Print Monte Carlo statistics
print(r'Compute time: mean: {0}, std: {1}'.format(np.mean(times), np.std(times)))
if not (inf in costs):
    print(r'Cost: mean: {0}, std: {1}'.format(np.mean(costs), np.std(costs)))
