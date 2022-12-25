# variable number of arguments

# python will allow us pass any number of argumets to the function
# The Keywords like *args and **kwrgs is used to achieve this

# normal function
def add(a,b):
    return a+b

# there is a limition in the above program it will accept exactly two arguments. To overcome the issue we use * args

def addtion(*args):  # *args will consider as a tuple
 
    return sum(args)

## testing
print(add(1,2)) #3
print(addtion(1,2,3,4)) #10

## Kwargs -> Keyword Arguments


def kwargsfunc(**kwargs):  # *kwargs will consider as dict
    print(kwargs)

kwargsfunc(name="Alex",age=21)


## default arguments

def defualtName(first,name='hello'):
    print(first,name)
defualtName('alex') # alex hello
defualtName('alex','bob') # alex bob