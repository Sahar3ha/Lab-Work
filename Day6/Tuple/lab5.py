#Write a Python program to add an item in a tuple.
tuple1=("ram","shyam","mohan")
print("original tuple",tuple1)
list1=list(tuple1)
print("original list",list1)
list1.insert(3,"krishna")
print("changed list",list1)
tuple2=tuple(list1)
print("changed tuple",tuple2)