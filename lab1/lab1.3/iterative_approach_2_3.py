import numpy as np

def f_x_y(x, y):
    part_1 =  4 * np.exp(-((x-1) ** 2 + (y-1) ** 2))
    part_2 =  np.exp(-((x-3) ** 2 + (y-3) ** 2))
    part_3 = np.exp(-((x+3) ** 2 + (y-3) ** 2))
    part_4 = np.exp(-((x-3) ** 2 + (y+3) ** 2))
    part_5 = np.exp(-((x+3) ** 2 + (y+3) ** 2))

    return part_1 + part_2 + part_3 + part_4 + part_5

def hessian_f_x_y(x, y):
    part_1_x = -8 * (x-1) * np.exp(-((x-1) ** 2 + (y-1) ** 2))
    part_2_x = -2 * (x-3) * np.exp(-((x-3) ** 2 + (y-3) ** 2))
    part_3_x = -2 * (x+3) * np.exp(-((x+3) ** 2 + (y-3) ** 2))
    part_4_x = -2 * (x-3) * np.exp(-((x-3) ** 2 + (y+3) ** 2))
    part_5_x = -2 * (x+3) * np.exp(-((x+3) ** 2 + (y+3) ** 2))
    part_1_y = -8 * (y-1) * np.exp(-((x-1) ** 2 + (y-1) ** 2))
    part_2_y = -2 * (y-3) * np.exp(-((x-3) ** 2 + (y-3) ** 2))
    part_3_y = -2 * (y-3) * np.exp(-((x+3) ** 2 + (y-3) ** 2))
    part_4_y = -2 * (y+3) * np.exp(-((x-3) ** 2 + (y+3) ** 2))
    part_5_y = -2 * (y+3) * np.exp(-((x+3) ** 2 + (y+3) ** 2))
    return np.array([part_1_x+part_2_x+part_3_x+part_4_x+part_5_x, part_1_y+part_2_y+part_3_y+part_4_y+part_5_y])

def gradient_descent(learning_rate = 0.001, max_iter= 10000, max_iters_without_improvement=500):
    x_0, y_0 = np.random.random(1), np.random.random(1)
    curr_x, curr_y = x_0, y_0
    curr_f_x_y = f_x_y(x_0, y_0)
    curr_gradient= hessian_f_x_y(x_0, y_0)
    iters_without_improvement = 0
    for i in range(max_iter):
        curr_x = curr_x + learning_rate * curr_gradient[0]
        curr_y = curr_y + learning_rate * curr_gradient[1]
        if (f_x_y(curr_x, curr_y) < curr_f_x_y):
            iters_without_improvement += 1
        else:
            iters_without_improvement = 0
        curr_f_x_y = f_x_y(curr_x, curr_y)
        curr_gradient = hessian_f_x_y(curr_x, curr_y)
        if (iters_without_improvement >= max_iters_without_improvement):
            break
    print("solution: x = {}, y = {}, f(x,y) = {}".format(curr_x, curr_y, curr_f_x_y))
    print("max iterations without improvement: {}".format(max_iters_without_improvement))
    print("max iterations: {}".format(max_iter))
    print("learning rate: {}".format(learning_rate))
    return curr_x, curr_y, curr_f_x_y

gradient_descent()


