x_1 = [3, -1, 0, 1]
x_2 = [2, 0, 0, 1]
p_1 = []
k = 0
for b1 in x_1:
    p_1.append(b1 + 2*(x_2[k] - b1))
    k += 1
print(p_1)