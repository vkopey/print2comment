# -*- coding: utf-8 -*-
from __future__ import print_function
from print2comment import prnt as print
def f(s):
    print('fn test')
    print(s)
print('test1', [1,2], sep=';')
#test1;[1, 2]
f('fn test2')
#fn test
#fn test2
print('newline\ntest3')
#newline
#test3
f('fn test4')
#fn test
#fn test4
for c in 'test':
    print(c)
#t
#e
#s
#t
