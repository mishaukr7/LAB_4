import math


def f(x):
    return ((x[0] + 10*x[1])**2) + 5*(x[2] - x[3])**2 + (x[1] - 2*x[2])**4 + 10*(x[0] - x[3])**4


def exp_search(x_start, h, f):

    step = [x for x in h]
    for count in range(len(x_start)):
        x_plus = [x for x in x_start]
        x_minus = [x for x in x_start]
        x_plus[count] += step[count]
        x_minus[count] -= step[count]
        if f(x_start) > f(x_plus):
            x_start = [x for x in x_plus]
        else:
            x_start = [i for i in x_minus]
    return x_start


def precision(x):
    sum_of_squares = sum(i**2 for i in x)
    return math.sqrt(sum_of_squares)


def first_step(x, h, f):

    while f(exp_search(x, h, f)) > f(x):
        h = [x/2 for x in h]
    return exp_search(x, h, f)


def image_search(x_start, h, coef_alpha, eps, f):

    x_basic = [x_start, exp_search(x_start, h, f)]
    k = 0
    alpha = 1
    while True:
        step = [i / alpha for i in h]
        print('Iteration #', k)
        print('step', step)
        p_1 = []
        i = 0
        for x_k in x_basic[k+1]:
            value = x_basic[k+1][i] + 2 * (x_k - x_basic[k+1][i])
            p_1.append(value)
            i += 1
        x_temporary = [x for x in p_1]
        print('x_temp =', x_temporary)
        print('x_basic = ', x_basic[k + 1])
        print('F(x_basic) =', f(x_basic[k+1]))
        print("-------------------")
        p_1.clear()
        if f(exp_search(x_temporary, step, f)) < f(x_basic[k+1]):
            x_basic.append(exp_search(x_temporary, step, f))
            k += 1
        else:
            if precision(step) < eps:
                return f(x_basic[k])
            else:
                alpha *= coef_alpha


print(image_search([3, -1, 0, 1], [1, 1, 1, 1], 1.9, 0.0001, f))

