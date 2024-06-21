#String
#Concatination
print("kulwant"+"olkha")
#replicate string
print("kulwant"*5)
print("-_"*10)
#length
print(len("Kulwant Olkha"))
print("kulwant olkha "[9])
print("kulwant olkha "[-10])
print("kuwlant olkha"[0:5]) #[index of starting number  : index of ending number + 1]
print("kuwlant olkha"[4:])
print("kuwlant olkha"[:9])
print("kuwlant olkha"[-5:-1])
print("kuwlant olkha"[-5:])
print("kulwant olkah"[::-1])
s = "kulwant"
print(s[::-1])
print("-"*50)
#case conversion
print("kulwantolkha".upper())
print("KULWANTOLKHA".lower())

#String Stripping 
print("           Kulwant Olkha       ")
print("           Kulwant Olkha       ".strip())

#String Replace
print("kuwlant olkha".replace('wl','lw'))

#String Count
print("Kuwlant olkhA".count('a')) #Case Sensitive
print("Kuwlant olkhA".lower().count('a')) 

#String Find
print("Kulwant Olkha".find("want"))

#String Check
print("kuwlant".isalpha())
print("kuwlant".isupper())
print("123".isdigit())

#String capitalize and title
print("kulwant olkha".capitalize())
print("kulwant olkha".title())

#String start and end
print("kulwant olkha".startswith("kul"))
print("kulwantolkha".endswith("kha"))

#String change length
print("kulwant olkha".center(20,"*"))
print("kulwant olkha".ljust(20,"*"))
print("kulwant olkha".rjust(20,"*"))
print("-"*50)

def reverseString(s):
    s = s[::-1]
    #Write your code below to reverse s and return it
#{ 
 # Driver Code Starts.



def main():
    t=int(input())
    while(t>0):
        s=input()
        print(reverseString(s))
        t-=1

if __name__ == "__main__": 
    main()
# } Driver Code Ends


