

## function definition

def addition(a:int,b:int)->int:    # you can optionally specify the types however if you give wrong data type args python will recognise it as error
    return a+b
# or 
def addition(a,b):
    return a+b
print(addition(12,32.3))   # calling the funciton



## Passing Parameters
def addtionalArgs(*args):   # *args can be used when we dont number the number of arguments that can be passed to the function
    x=len(args)
    sum=0
    for i in args:
        sum+=i
    return sum

print(addtionalArgs(1,2,3,5))


# a function may or maynot have any arguments
