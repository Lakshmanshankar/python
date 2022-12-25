"""
Conditional statement allow us to run the program based on certain condition
"""
a,b=10,20
## conditional statements
if a>b:
    print("A is bigger")
elif a==b:
    print("A is equal To B")
else:
    print("C is Greater")


if True:
    print(True)
else:
    print(False)


## String Expressions
mystr='  Hello,world   '
mystring='jellybean   '

print(mystr.capitalize()+mystring.lower())
print(mystr.capitalize()) #upper() .lower()
print(mystring.isnumeric()) #mystring.isalpha() .isascii() .lstrip() .rstrip() .islower()
# find() count index() and many more



## Boolean Expression
a1,b1=1,2
print('Boolean express')
print(bool(1)) # true
print(bool(0)) #false


print(bool(''))   #false
print(bool('1'))  #true

print(int(True)) # 1
print(int(False)) # 0

print(True and False) #False
print(a>b) #false


