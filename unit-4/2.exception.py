# Exception model

# BaseException ignore any error
intNum=int(input("enter number"))
SeC=1203
try:
    print(SeC/intNum)
except:
    print("Number cannot be zero")


# Handling Specific Exceptions
intNum=int(input("enter number"))
SeC=1203
try:
    print(SeC/intNum)
except ZeroDivisionError as zd:
    print(zd)


# using else block
try:
    print(SeC/intNum)
except ZeroDivisionError as zd:
    print(zd)
else:
    print('Successfully passed exception model')


# using finally
# finally will run always
try:
    print(SeC/intNum)
except ZeroDivisionError as zd:
    print(zd)
else:
    print('Successfully passed exception model')
finally:
    print("End of Exception Model")