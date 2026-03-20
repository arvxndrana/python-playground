def summa_lamma(a):
    la = len(a)
    k = 0
    returna = []
    while (k+1 < la):
        summa = a[k] + a[k+1]
        k += 1
        returna.append(summa)
    return returna
