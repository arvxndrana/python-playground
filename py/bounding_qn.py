def f(x,y):
    return 18*x + 7*y - 483

m_upper_bound = 483 // 18 + 1
n_upper_bound = 483 // 7 + 1

answers = []
for m in range(m_upper_bound):
    for n in range(n_upper_bound):
        if (f(m,n) == 0):
            answers.append([m,n])

print(answers)
