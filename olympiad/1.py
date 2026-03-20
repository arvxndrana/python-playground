"""
    How many three-digit numbers which are multiples of 7 end with 4?
"""

count = 0
for i in range(100,1000):
    if (i % 10 == 4 and i % 7 == 0):
        count += 1

print(f"Ans: {count}")
