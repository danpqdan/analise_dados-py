lst = [0,1,2,3,4,5]
print(lst)

lst2 = [0,1,2,"4", False]
print(lst2)

lst3 = [12,[1,2,3,4,5], "a"]
print(lst3)

lst4 = list(range(0,10))
print(lst4)

print(len(lst))
print(len(lst2))
print(len(lst3))
print(len(lst4))

#Processando elementos

print(lst[0])
lst[0] = 7
print(lst)

#For percorrendo a lista
for n in range(0, len(lst4)):
    print(lst4[n])
    lst4[n]+1