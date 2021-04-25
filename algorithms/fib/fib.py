"""#fibonacci numbers module
0,1,1,2,3,5,8,13
f(n) = f(n-1)+f(n-2)
"""


def fib(n):

    if n <= 1:
        return n
    else:
        arg1 = fib(n-1)
        arg2 = fib(n-2)
        return arg1 + arg2