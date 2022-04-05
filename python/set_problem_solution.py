int_set = {1,2,3,4}
print(int_set)

#add 5 to the set

int_set.add(5)
print(int_set)

if int_set == {1,2,3,4,5}: answer = True
print(answer)

# add 6, 7, 8, and 9 at the same time

int_set.update([6,7,8,9])
print(int_set)

if int_set == {1,2,3,4,5,6,7,8,9}: answer = True
print(answer)

# remove 7 and 9

int_set.remove(7)
int_set.remove(9)
print(int_set)

if int_set == {1,2,3,4,5,6,8}: answer = True
print(answer)