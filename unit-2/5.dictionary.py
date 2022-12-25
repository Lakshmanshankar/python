dict={

    "names":"alex",
    "age":21,
    "role":"devOps",
    "salary":23000
}

# dictionary is changable

# Accessing Values
print(dict["names"]) # alex

# Assign values
dict["age"]=23

# len(dic)
print(len(dict)) # 4

#update the dict
dict.update({"location":"toronto"})
print(dict)



# iterate the dict
for i in dict:
    print(i) #keys
    print(dict.values(i)) # values of i->key


## Remove from dict
dict.pop("location") # requires a key to delete 
print(dict)
# clear the dict
dict.clear()


## All for dict