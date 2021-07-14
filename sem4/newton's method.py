num = int(input("enter number to calculate square root"))
def newtonSqrt(n, numberoftimes):
    approx = 0.5 * n
    for i in range(numberoftimes):
        betterapprox = 0.5 * (approx + n/approx)
        approx = betterapprox
    return betterapprox
print(newtonSqrt(num, 10))

