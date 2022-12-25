##looping statements
#break
i = 0
while i < 9:
  i += 1
  if i == 4:
    break
  print(i)

print("*"*22)
# continue
i = 0
while i < 9:
  i += 1
  if i == 3:
    continue
  print(i)


## for loop in python
# for in str
for i in "Hello":
    print(i)
# for in tuple
for i in (1,2,3,4):
    print(i)
#for in list
for i in [1,2,3,4]:
    print(i)


## for in range
for i in range(0,10):
    print(i,end=" ")
print("\n")