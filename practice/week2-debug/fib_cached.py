#!/usr/bin/env python
from functools import lru_cache
def fib0(): return 0
def fib1(): return 1
s = """@lru_cache(1)
def fib{}(): return fib{}() + fib{}()"""
if __name__ == '__main__':
    for n in range(2, 10):
        exec(s.format(n, n-1, n-2))
    print("cached fib9() =", eval("fib9()"))
