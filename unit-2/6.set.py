## Set in python

set1={1,2,3}
set2={4,5,6}

set3=set1.union(set2)
print(set3)   #{1, 2, 3, 4, 5, 6}


## intersection
print(set1.intersection(set3))  #{1, 2, 3}

#difference
print(set3.difference(set1))  # {4,5,6} (in a not in b)

# subset and superset
print(set3.issuperset(set1))  #subset and superset return boolean values

print(set3.pop()) # 1