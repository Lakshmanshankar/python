## python builtin functions

# print(license())  # view python license info and bit about the history

lis=[1,2,3,4,5]

print(all(lis)) # Return true if does not have zero 
print(any(lis)) # " true if any of values is true
print(sum(lis)) # sum of the iterable
print(max(lis)) # max value of the list
print(min(lis)) # min value of the list
print(set(lis)) # convert the list to set 
print(list(lis))# convert to list
## similarly you can convert to int float() str() dict etc

x=range(0,10) 
print(x) #range(0,10)


## check types 
oct(12) # convert the number to octal 
bin(12) # convert to binary

#math functions
print(pow(2,3)) # 8 (2*2*2)
print(ord('A')) # 65 (ascii) value

## few more
print()
help()
next()
exit()

## continue