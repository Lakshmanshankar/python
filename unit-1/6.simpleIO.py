# input
name=str(input('Enter your name'))
print(name)

age=int(input('Enter your age'))
print(age)

## if you don't understand no problem
## input from file
with open('./variables/textone.txt','w+') as file:
    str=f'{name} and {age} is written into the file'
    print(file.write(str))
    print(str)