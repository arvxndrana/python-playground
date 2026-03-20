#!/usr/bin/env python3

def randint_n(n):

    import random as r

    start = "1" + "0" * (n - 1)
    start_int = int(start)

    end = "9" * n
    end_int = int(end)

    return_value = r.randint(start_int, end_int)

    return return_value

def digital_root(N):
    str_N = str(N)
    while (len(str_N) > 1):
        N_arr = [int(n) for n in str_N]
        str_N = str(sum(N_arr))
    return int(str_N)

if __name__ == "__main__":
    for _ in range(10):
        k = randint_n(10)
        mod = k % 9
        # print(k)
        # print(digital_root(k))
        # print(mod)
        print(digital_root(k),mod, digital_root(k) == mod)

# Reference: https://en.wikipedia.org/wiki/Digital_root
# i suck at programming but it works
