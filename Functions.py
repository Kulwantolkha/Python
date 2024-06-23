#Function 

# greet()  ❌ this is not possible as function is not defined yet

#1. defining a function 
def greet():
    print("Hello")

#2. Calling a function (We can only call a function after defining that function)
greet()
greet()

#3. If we define the same function again then the last defined function will be the final value
def greet():
    print("Hi")
    
greet()
print("-"*50)

#4. Global Variable: Defined Outside of function can be used anywhere inside as well as outside the function
#5. Local Variable: Defined Inside a function can be used only inside the function not outside 
g_var = 10
def greet():
    l_var = 5
    print(g_var,l_var)
    
greet()
print(g_var)
#6. print(l_var) ❌ as it is a local variable
print("-"*50)

#7. Passing a parameter inside a function

def greet(n):
    print("Hello,",n)
greet("Kulwant")
greet(n = "Kulwant")

#8. greet() ❌ only work when we pass a parameter
#9. default parameter

def greet(n="Mr/Mrs"):
    print("Hello",n)
greet()
greet("Kulwant")

def sum(a=0,b=0):
    print(a,b,a+b)
sum()
sum(5,10)
sum(a=4,b=6)
# sum(x=9,y=38) ❌ should be a and b only
# sum(a=4,8) ❌
sum(4)
print("-"*50)

#10. Return from a function
# in the above function we need not any print statement as our function already contain print statement it is not returning anything
print(greet()) #will print one extra "none" as well because print statement will print the return value only as greet() function does not have any return value this will print none 

def airthmetic(a=0,b=0):
    return a+b, a-b, a*b

s = airthmetic(10,5)
print(s)
print(airthmetic(23,23))
print(type(s))

#11. as it is returning a tuple we can make 3 different variable to store three different return values of this function
sum, sub, mul = airthmetic(19,8)
print(sum)
print(sub)
print(mul)

# sub, mul = airthmetic(19,8) ❌
print("-"*50)


lst = [1,2,3,4,5]
def sq(lst):
    return [i**2 for i in lst]

def cube(lst):
    return [i**3 for i in lst]

def final(lst):
    lst1 = sq(lst)
    lst2 = cube(lst)
    return [lst1[i]+lst2[i] for i in range(len(lst1))]

print(sq(lst))
print(cube(lst))
print(final(lst))

