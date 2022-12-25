# global var can be accesed from any where
# local var can accessed only from the block it has been declared

my_gloa=12
def localFunc():
    my_loac=13
    print(my_gloa,my_loac) # 12 13
    # changes made to my_gloa from here will not reflect outside of this functions but we can use global keyword to do this

localFunc()
#print(my_gloa,my_loac) # ERR: my_loac is not defined

## using global keyword


def changeGlbal():
    global my_gloa    # now the changes made inside the function will reflect where the var is used similarly non local can be used in case of nested functions (or non global vars)
    my_gloa=23
changeGlbal()
print(my_gloa)
