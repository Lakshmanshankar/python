## list 
lis=[1,2,3,4,5]
lis4=[9,10]

## adding elems to list
print(lis+lis4)
lis.append(2)
lis.insert(0,23) # index (0), val (23)
lis.extend([6,7])
print(lis)

## Removing from list
print(lis.pop())# remove last elem
print(lis.pop(0)) # remove first elem
lis.remove(3) # if the value (3) is in the list then remove it
#lis.clear() # delete all elem
#del lis  #will delete the variable


## more operations
lis.sort() #sort the list
len(lis)   #length of list
lis.count(1) # count number of occurence for the given value
lis.index(2) # return index of given val
newLis=lis.copy() # copy the list to the new variable
lis.reverse() # reverse the list
print(lis)


## that all for list methods
## few more
print(all(lis)) # iterate the obj return true if no zero
print(any(lis)) # if any of value is true return true


#List loop
for i in lis:
    print("[",i,end=" ]")

#mutablity
lis[0]=1
lis[1]=0
lis[2]=0
print(lis)

## aliasing
list1=[1,2,3]
list2=list1
print(id(list1),id(list2),"! important")  # both ids are same
list2.append(10)
print(list1) #[1,2,3,10]

# # cloning
# list1=[1,2,3]
# list2=list1.copy()
# list2.append(10)
# print(list1) #[1,2,3]




