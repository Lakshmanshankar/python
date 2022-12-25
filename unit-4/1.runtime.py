# Example for runtime errors

intNum=int(input("enter number"))
SeC=1203
try:
    print(SeC/intNum)
except:
    print("Number cannot be zero")


# type error
str='12'
try:
    print(SeC/str)
except:
    print("Incompatibale data types")


## File Not found
try:
    with open('/unit-1/textone.txt','r') as f:
        print(f.read())
except:
    print("No such file")


