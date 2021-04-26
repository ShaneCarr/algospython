# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from algorithms.fib.fib import *
from algorithms.fib.fibit import *
from visualiser.visualiser import Visualiser as vs
from graphviz import Digraph

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

#print("fibit")
#for i in range(6):
#  print(fibit(i))

print("fib")
#for i in range(6):
   # print(fib(i))

print(fib(n=6))
vs.make_animation("fibonacci.gif", delay=2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
