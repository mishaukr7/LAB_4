import hooke_jeeves

def main():
    x_start =[]
    h = []
    error_text = 'Error. Incorrect input data! Try again...\n' \
                 '=========================================='
    while 1:
        try:
            n = int(input('Input number of variables: '))
            break
        except ValueError:
            print(error_text)
    while 1:
        try:
            i = 0
            for i in range(n):
                x = float(input("Enter x_{0}: ".format(i+1)))
                x_start.append(x)
            break
        except ValueError:
            print(error_text)
    while 1:
        try:
            i = 0
            while i < n:
                h_variable = float(input("Enter h_{0} interval value: (0; 10): ".format(i+1)))
                if (0 < h_variable < 10):
                    h.append(h_variable)
                    i += 1
                else:
                    print(error_text)
            break
        except ValueError:
            print(error_text)
    while 1:
        try:
            alpha = float(input('Enter coefficient of step interval value (1; 10]: '))
            if (1 < alpha <= 10):
                break
            else:
                print(error_text)
        except ValueError:
            print(error_text)
    while 1:
        try:
            eps = float(input('Enter precision (eps>10^-6): '))
            if eps <= 10**(-6):
                print(error_text)
            else:
                break
        except ValueError:
            print(error_text)

    return hooke_jeeves.image_search(x_start, h, alpha, eps, hooke_jeeves.f)

print('Vector of basic point: ', main())