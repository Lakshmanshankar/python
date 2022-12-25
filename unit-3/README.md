# Unit 3

Functions paramenter and Built in modules

## Unit description
```
FUNCTIONS: Definition - Passing parameters to a Function - Built-in functions- Variable Number
of Arguments - Scope – Type conversion-Type coercion-Passing Functions to a Function -
Mapping Functions in a Dictionary – Lambda - Modules - Standard Modules – sys – math – time -
dir - help Function.
```

# functions
function in a programming language is a block of code will perform certain actions when the function is being called. Theer are mainly two types of functions available one is built in and other one is user defined.


Function may or may not return values 
fruitfull function return any type of value (list , int etc)

The code inside the block will run only if the function called and 

functions have mainly two parts:
1. definition
2. calling 


### definition
function definition will contain all the code. these function definition can be created using the def key word

example:
refer 
[1.functions.py](https://github.com/Lakshmanshankar/python/tree/main/unit-3)

### calling
function calling the part where you call the definied function when you call the function then only the code inside the function will run

To call a function type functionname followed by a parenthesis 
example:
func()


## Type conversion
Type Conversion is the conversion of an object from one data type to another data type.
Implicit Type Conversion is automatically performed by the Python interpreter. 

Python avoids the loss of data in Implicit Type Conversion.   \ \(@ - @)/ /


Mainly there are two types of conversion 
Implicit and Explicit


## Implicit
Done by python interpreter 
Python does not loss the values when implicitly conver the type
 refer 5.types.py

## Explict Conversion
Convert the data type by us data loss may occur during explicit type conversion aka type casting


## Type coersion
The automatic type conversion from one data type to another is called as Type Coercion. This is also called as Implicit Type Conversion. 

The major difference between Type Conversion and Type Coercion is that, type conversion is done manually using built-in functions where as type coercion is done automatically.


## Function as args
python allow us to give functions as input to another functions
more refer 6.func2func.py
