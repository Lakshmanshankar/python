## Handling Mulitple exceptions

floaInt=float(input('Enter Float for execpt'))
list=[1,2,3,4,5,6,7]
try:
    print(list[floaInt])
except (IndexError,TypeError) as i:
    print(i)    # Error here is simple [list indices must be integers or slices, not float ]
"""Here we check the index error for index out of range and type error for invalid types"""



## Raise Own Exceptions
floaInt=float(input('Enter Float for execpt'))
list=[1,2,3,4,5,6,7]
try:
    print(list[floaInt])
except (IndexError,TypeError) as i:
    raise TypeError('Sorry Input is not int')  # this will raise an error with following msg
"""
Traceback (most recent call last):
  File "/path", line 20, in <module>
    raise TypeError('Sorry Input is not int')
TypeError: Sorry Input is not int
"""