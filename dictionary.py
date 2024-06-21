#Dictionary
# {key:value} {1:'',2:'',3:''}  keys should not be same, values could be same
dict = {1: "Ashish",2: "Avneet",3:"Ankur",4:"Ankush"}
print(dict)
dict1 = {1: "Ashish",2: "Avneet",3:"Ankur",4:"Ankush",2:"Ayush"}
print(dict1)
print(len(dict))

#key can be of any type but should be different
dict2 = {1: "Ashish",2: "Avneet",3:"Ankur",4:"Ankush",'2':"Ayush"}
print(dict2)
dict3 = {"Ashish":1,2: "Avneet",3:"Ankur",4:"Ankush",'2':"Ayush"}
print(dict3)

#accessing the element of dictionary 
print(dict[1])  #using keys only, this will be wrong -> dict['Ashish']
print(dict3['Ashish'])  #this can be used as ashish is key in dict3
print(dict.get(2))   #2 is key only not index

#Adding new key value pair
dict[6] = 'Kulwant'
print(dict)

#delete key value pair
del dict[6]
print(dict)

#updateing dictionary
dict[1] = 'Aakash'
print(dict)

#clear dict
dict2.clear
print(dict2)

#to print keys only
print(dict.keys())
#to print values only
print(dict.values())

#iterate through dictionary 
#to iterate through key only
for k in dict.keys():
    print(k)
#to iterate through values as well
for k in dict.keys():
    print(k,dict[k])
    
#2nd method
print(dict.items())
for i in dict.items():
    print(i)
    
#check key is present or not 
print(1 in dict)
print('Aakash' in dict) #not work for value

#updating dict
# print(dict3)
# print(dict1)
# # dict1.update(dict3)
# print(dict3)
# print(dict1)

#merging dict
dict4 = {'a': 1, 'b': 2, 'c': 3}
dict5 = {'f': 10, 'd': 4, 'e': 5}
for i in dict4.keys():
    dict5[i] = dict4[i]
print(dict5)

#merging if same keys arise
# important code that shows us that list can be a part of values in a dict
# Define the two dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 10, 'd': 4, 'e': 5}
# Merge dict1 into dict2 with conflict handling
for key, value in dict1.items():
    if key in dict2:
        # If the key exists in both dictionaries, combine values into a list
        if type(dict2[key]) is list:
            dict2[key].append(value)
        else:
            dict2[key] = [dict2[key], value]
    else:
        # If the key does not exist, simply add it
        dict2[key] = value

# Print the merged dictionary
print(dict2)
            
dict = {1: {'Name': 'Ashish','phone':1234321},
        2: {'Name': 'Ankush','phone':1224122}}
#this dict is of size 2
print(len(dict))
#Accessing the values of dictionary
print(dict[1])
print(dict[1]['Name'])
#Adding new data in the dict 
dict[3] = {"Name":"Ayush","phone": 1312312}
print(dict)
#Update the values in a dict
dict[3]["Name"] = "Aayush"
print(dict)
#delete the data in dict
del dict[3]
print(dict)
#iterating through the dict
for i in dict.keys():
    print(i,dict[i]["Name"])
    print(i,dict[i]["phone"])
    print(i,dict[i]["Name"],dict[i]['phone'])
    
data = {1: {'name':'Ashish','phone':1233123,'marks':{'hin':45,'eng':41,'mth':39,'sci':45}},
        2: {'name':'Ankush','phone':1231231,'marks':{'hin':39,'eng':43,'mth':39,'sci':40}},
        3: {'name':'Ayush','phone':1233231,'marks':{'hin':30,'eng':44,'mth':32,'sci':45}},
        }
print(data[1]['marks']['hin'])
for i in data.keys():
        print(data[i]['name'],data[i]['marks']['hin'])
        
