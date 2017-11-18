import math


def f(x):
    return ((x[0] + 10*x[1])**2) + 5*(x[2] - x[3])**2 +(x[1] - 2*x[2])**4 + 10*(x[0] - x[3])**4


def exp_search(x_start, h, f):
    for count in range(len(x_start)):
        x_plus = [x for x in x_start]
        x_minus = [x for x in x_start]
        x_plus[count] += h[count]
        x_minus[count] -= h[count]
        if f(x_start) > f(x_plus):
            x_start = x_plus
        elif f(x_start) > f(x_minus):
            x_start = x_minus
        else:
            x_start = x_start
    return  x_start

#print(exp_search([3, -1, 0, 1], 1, f))

def precision(x):
    sum_of_squares = 0
    for count in x:
        sum_of_squares += count**2
    return math.sqrt(sum_of_squares)



def image_search(x_start, h, eps, f):
    x_search = [x_start]
    k = 0
    while precision(x_search[k]) > eps:
        x_search.append(exp_search(x_search[k], h, f))
        #print(x_search[k])
        #print(f(x_search[k]), f(x_search[k+1]))
        if f(x_search[k+1]) < f(x_search[k]):
            p_1 = []
            i = 0
            for b1 in x_search[k]:
                p_1.append(b1 + 2 * (x_search[k+1][i] - b1))
                i += 1
            x_search.append(p_1)
            print(x_search[k+1])

        else:
            h = [x / 2 for x in h]
        #print(x_search[k])
    return x_search[k]

print(image_search([3, -1, 0, 1], [1, 1, 1, 1], 0.1, f))


def first_step(x, h, f):
    while f(exp_search(x, h, f)) > f(x):
        h = h/2
    return exp_search(x, h, f)

def image(x_start, h, eps, f):
    x_result = [first_step(x_start, h, f)]

    while precision(x_result) < eps:






    k = 0
    while precision(x_result[k]):
        x_search_p = exp_search(x_search[k], h, f)
        if f(x_search_p) < f(x_result[k]):
            x_result.append(exp_search(x_result[k], h, f))
            p_1 = []
            i = 0
            for b1 in x_result[k]:
                p_1.append(b1 + 2 * (x_result[k+1][i] - b1))
                i += 1


