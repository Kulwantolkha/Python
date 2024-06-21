
class agent:
    def __init__(self,name,age):
        print("Welcome to agent class")
        self.name = name
        self.age = age
        self.health = 100
        self.alive = True
        
    def curr_health(self):
        print("Current Health of:",self.name,"is",self.health)
        
    def punched(self):
        self.health -= 10
    
    def shooted(self):
        self.health -= 50
        
    def is_alive(self):
        if self.health <= 0:
            self.alive = False
            
    def info(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Health: ",self.health)
        print("Alive: ",self.alive)
        
a1 = agent("Ashish",20)
a1.punched()
a1.shooted()
a1.is_alive()

a2 = agent("Ankur",29)
a2.shooted()
a2.shooted()
a2.shooted()
a2.is_alive()

a1.info()
print("#"*50)
a2.info()

print('-'*50)

# - If we want to make a separate class having all the properties of above class as well as some properties of its own as well

class boss(agent):
    
    def blow_fire(self):
        print("Boss can blow fire as well")
    
# - If you want to change any property of boss class then this can be done by 

    def __init__(self,name,age):
        super().__init__(name,age)   #call the parent class init
        self.health = 1000
    
bs = boss("boss1",19)
bs.punched()
bs.shooted()
bs.shooted()
bs.punched()
bs.punched()
bs.is_alive()
bs.blow_fire()
bs.info()
    

        
