import math
import itertools

digits = [x for x in range(10)]
answers = []

for n in itertools.product(digits, repeat=2025):
    if (sum(n) == math.prod(n)):
        answer.append(n)
        print(n)

print(answers)
