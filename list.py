#squared brackets are used in list, all type of data can be filled inside the list like string, boolean, integer
demo_list = [1,4.3,"tom",True]
print(demo_list)
print(demo_list[2]) #index start from 0
print(demo_list[-1]) #last index starts from -1
demo_list[2] = "jerry" #list value can be changed *mutable*
print(demo_list)
demo_list[0] = "tom"
print(demo_list)
print("-"*50)
print(demo_list[1:4])
print("-"*50)
print(demo_list[::-1]) #reverse the list 
print(demo_list[::-2])
print("-"*50)
demo_list.append('Ankit') #add new item to the list
print(demo_list)
demo_list.remove("Ankit") #remove from the list
print(demo_list)
print("-"*50)
print(len(demo_list)) #print length of the list
print("-"*50)

#Sorting a list 
lst = [2,4,6,3,34,234,25,34,343,3233,24,25,345,243,2,53]
print(sorted(lst))
print("-"*50)

#Find the element 
print(demo_list.count("tom"))
print("-"*50)

#Extend a list (Adding more than one value)
demo_list.extend(["Rahul", "Sanjay", "Sumit", "Kartik"])
print(demo_list)
print("-"*50)

#Find min and max of a list
print(min(lst))
print(max(lst))
print("-"*50)

#iterating through list
for i in demo_list:
    print(i)
print("-"*50) 

# for i in range(len(demo_list)):
#     print("at index",i,"element present is",demo_list[i])

#reverse order important (-1 in third)
for i in range(len(demo_list)-1,-1,-1):
    print(demo_list[i])
    
from support import greet
greet("Kulwant")
