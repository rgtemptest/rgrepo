mylist = [1, "two", None, True]

for element in mylist:
    print(element)

print(mylist)

print(mylist[1])
print(mylist[3])

# print(mylist[999])

print(dir(mylist))

mylist.append("taco")
mylist.append("cat")

print(mylist)

mylist.insert(0, "new first element!")

print(mylist)

for index, element in enumerate(mylist):
    print(index, element)


