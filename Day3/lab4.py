#Given three integers, print the smallest one. (Three integes should be user input)
list1 = []
num = int(input("Enter number of elements in list: "))

for i in range(1, num + 1):
	ele= int(input("Enter elements: "))
	list1.append(ele)
	
print("Smallest element is:", min(list1))




#num=int(input("Enter elements : "))
#print(f"smallest element is : ", min(num))

