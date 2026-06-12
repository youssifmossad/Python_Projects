# This program removes duplicate values from a list.
# It checks each element and removes repeated ones.
# Finally, it prints the cleaned list without duplicates.
list=[1,2,3,4,5,6,6,7,8,8,9,9,9,10,11,21,36,63,36]
for i in list:
    if list.count(i)>1:
        list.remove(i)
print(list)        