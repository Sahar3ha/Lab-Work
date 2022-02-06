#. Write a Python program to sum all the items in a dictionary
def Sum(Dic):
     
    list = []
    for i in Dic:
        list.append(Dic[i])
    final = sum(list)
     
    return final
 

dict = {'a': 100, 'b':200, 'c':300}
print("Sum :", Sum(dict))