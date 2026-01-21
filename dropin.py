#Learning how to drop-in a module for my 302 homework

#!/usr/bin/env python
'''this tells the computer to run program in python (specifying interpreter)'''
'''you can also do !/usr/bin/python'''

import time

def show_time():
    return time.ctime()

if __name__ == '__main__':
    #store code that should only run when file executed as script
    print(show_time())




