# no 1
def fibFor(n):
        fib = []
        fib.append(0)
        fib.append(1)
        if n == 0:
            return fib[0]
        elif n == 1:
            return fib[1]
        else:
            for i in range(2, n+1):
                fib.append(fib[i-1]+fib[i-2])
            return fib[n]

#no 2
def pangkat(x):
    if x == 0:
        return 1
    else:
        return 2 * pangkat(x-1)

def pangkatWhile(x):
    npow = 2
    if x == 0:
        return 1
    else :
        while x > 1:
            npow *= 2
            x -= 1
        return npow
    
print(fibFor(7))
print(pangkat(4))
print(pangkatWhile(4))
