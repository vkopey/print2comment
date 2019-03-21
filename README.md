# print2comment

Python 2.7 only!
Based on question https://stackoverflow.com/questions/38231131/annotating-python-print-output-with-comments

Usage:

    from __future__ import print_function
    from print2comment import prnt as print
    print('test')

Result:

    from __future__ import print_function
    from print2comment import prnt as print
    print('test')
    #test
