# in python we can use function as argument to another functions
def toUpper(string):
    return string.upper()

def makeWish(Wish):
    print(Wish*3)

string="Hello, Python "
makeWish(toUpper(string))


## more to know

mk=makeWish
mk("This is also possible c")


# These functions are called as higher order functions
# these may accept other function as arg or return function as result

## lambda
## Its anonymous 
# A lambda function can take any number of arguments, but can only have one expression.

x = lambda a : a + 10
print(x(5))