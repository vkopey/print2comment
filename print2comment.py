# -*- coding: utf-8 -*-
"""
Створює копію модуля Python 2, у якій усі виведення функцією print() додаються в наступний рядок після її виклику у вигляді коментарів. Наприклад є модуль test.py:

    from __future__ import print_function
    from print2comment import prnt as print
    print('test')

В результаті його виконання командою

    python test.py

буде створено модуль test_comments.py:

    from __future__ import print_function
    from print2comment import prnt as print
    print('test')
    #test

Протестовано на Python 2.7. На Python 3 не працює! Працює також в тих випадках коли функція print викликається в середині інших функцій, або в циклі for. Створено на основі питання: https://stackoverflow.com/questions/38231131/annotating-python-print-output-with-comments Перевагою цього методу є те, що в код потрібно тільки додати `from print2comment import prnt as print`.
"""
from __future__ import print_function
import sys,os,inspect,atexit,StringIO
caller = inspect.currentframe().f_back #або sys._getframe(1) 
caller = os.path.basename(caller.f_globals['__file__']) # модуль, який викликав цей модуль
def save():
    "Зберігає файл модуля з доданими коментарями"   
    oldLines=open(caller,'r').readlines() # початкові рядки коду
    keys=sorted(comments.keys(), reverse=True) # номера рядків коду, де викликається print()
    for key in keys:
        if key==len(oldLines): oldLines.append('\n'+comments[key]) # для останнього рядка
        else: oldLines.insert(key, comments[key]) # вставити коментарі
    with open(os.path.splitext(caller)[0]+'_comments.py','w') as f:
        f.writelines(oldLines) # зберегти код з коментарями

atexit.register(save) # виконує save під час завершення виконання
comments={} # словник з парами (номер рядка : коментар)

def prnt(*args, **kwargs):
    "Аналог стандартної функції print(), але зберігає усі виведення в comments"
    info = inspect.getouterframes(inspect.currentframe())
    ln=info[-1][2] # рядок коду, де викликається ця функція
    s=StringIO.StringIO()
    print(*args, file=s, **kwargs) # виведення у пам'ять
    comment='#'+s.getvalue()[:-1].replace('\n', '\n#')+'\n' # додати символи коментаря на початку рядків
    if ln in comments: # якщо такий номер вже є
        comments[ln]+=comment # об'єднати
    else:
        comments[ln]=comment
    print(*args, **kwargs) # виклик стандартної функції print
