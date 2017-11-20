import hooke_jeeves

def main():
    x_start =[]
    h = []
    while 1:
        try:
            n = int(input('Input nuvber of variables: '))
            break
        except ValueError:
            print('Error. Incorrect input data! Try again...')
            print('==========================================')
    while 1:
        try:
            for i in range(n):
               # print()
                x = float(input("Enter x_{0}: ".format(i+1)))
                x_start.append(x)
            break
        except ValueError:
            print('Error. Incorrect input data! Try again...')
            print('==========================================')
    while 1:
        try:
            for i in range(n):
               # print()
                h_varible = float(input("Enter h_{0}: ".format(i+1)))
                h.append(h_varible)
            break
        except ValueError:
            print('Error. Incorrect input data! Try again...')
            print('==========================================')
    while 1:
        try:
            alpha = float(input('Enter coefficient of step: '))
            break
        except ValueError:
            print('Error. Incorrect input data! Try again...')
            print('==========================================')
    while 1:
        try:
            eps = float(input('Enter precision (eps): '))
            break
        except ValueError:
            print('Error. Incorrect input data! Try again...')
            print('==========================================')

    #h = [1 for i in range(n)]
    return hooke_jeeves.image_search(x_start, h, alpha, eps, hooke_jeeves.f)

print('Vector of basic point: ', main())