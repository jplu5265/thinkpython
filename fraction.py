def fractional(n):
    if not isinstance(n, int):
        print('Fractional is only defined for integers.')
        return None
    elif n < 0:
        print('Fractional is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        #recurse = fractional(n-1)
        #result = n * recurse
        #return result
        return n * fractional(n-1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
