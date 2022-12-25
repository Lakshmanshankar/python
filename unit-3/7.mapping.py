# map function will allow us to iterate through a iterable object
## map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
#syntax
# map(function,__iterable__)


list01=[1,2,3,4,5,6,7]
list02=[1,2,3,4,5,6,7]
def pow(x):
    return x*x

print(list(map(pow,list01)))  # <map object at memlocation>

## using with lambda's
res=map(lambda x: x*x,list01)
print(list(res))


# For multiple rows like addition
def add(a,b):
    return a+b
result=map(add,list01,list02)
print(list(result))



## mapping func with dicts
lisDict=[
    {"name":"alex","age":32},
    {"name":"bob","age":21},
    {"name":"chan","age":20}
]
f={i["name"]:i["age"] for i in lisDict}  # {alex:32,bob:21,chan:20}
print(f)

