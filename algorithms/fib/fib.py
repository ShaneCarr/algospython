"""#fibonacci numbers module
0,1,1,2,3,5,8,13
f(n) = f(n-1)+f(n-2)
"""
from graphviz import Digraph
from visualiser.visualiser import Visualiser as vs
@vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def fib(n):
    if n <= 1:
        return n

    return fib(n=n-1) + fib(n=n-2)
