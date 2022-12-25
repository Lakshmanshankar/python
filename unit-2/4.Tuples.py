# Tuple is also similar to list but these are immutable

tup=(1,2,3,4,5)
tup2=(6,7,8,2,3)

# Adding
tup3=(tup+tup2)
print(tup3)

# tuple does not have many method like list
print(tup.count(2)) # 1 there is only one two in the tup
print(tup3.index(2)) # return the index of the values if many values are there return first value's index


## Unpacking tuple
a=(1,2,3)
b,c,d=a
print(b,c,d)


#tuple assignment
#packing and unpack
x,y,z=(1,2,3)
g=x,y,z
print("Before assign",g)
x=10
g=x,y,z
print("After assign",g)



## tuple as return
def func():
    return (1,2,3)
print(func()) # (1,2,3)


## that's all for tuple