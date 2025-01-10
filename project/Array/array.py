import array as  arr


a=arr.array("i",[1,2,3])




print(a[0])

a.append(5)


print(a)


for i in range (0,3):
    
    print(a[i],end="")
    break




a.insert(1,4)
print("integer after insertion",a)

a.remove(1)
a.pop(2)
print("removed",a)