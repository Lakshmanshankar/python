## Standard Modules
""" Python provides standard modules like sys math os time etc.
Python standard modules is very extensive. 
"""

import sys,os,time

# Sys
## sys is used to manipulate the various runtime env
sys.stdout.write('Hello') # single quotes
# for line in sys.stdin:   buggy
#     print(line)
# print()

args=len(sys.argv) # great for cli tools
print(f"Args  {args} is len and {sys.argv}") # python3 8.modules.py 1st 2nd 


## OS module

print(os.cpu_count()) # no of threads in your computer
# print(os.mkdir("HelloTem"))  # create a folder
# os.chdir("../unit-2")     # what is does is change directory and create folder in it
# print(os.mkdir("HelloTem"))
print(os.ctermid()) # terminal /dev/tty
print(os.getcwd()) # pwd same


# Time

print(time)
# print(time.sleep(10))
print(time.asctime())
print(time.ctime())
print(time.clock_gettime(1)) 

## dir func

print(dir(time)) # list all method and object for the given obj even built in props aswell
print(dir(os))


## Help
# is similar to man in linux
# AKA built-in python help system

help() # invoke the help utilty