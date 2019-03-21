# -*- coding: utf-8 -*-
from __future__ import print_function
from print2comment import prnt as print
def f(s):
    print('fn test')
    print(s)
print('test1', [1,2], sep=';')
f('fn test2')
print('newline\ntest3')
f('fn test4')
for c in 'test':
    print(c)