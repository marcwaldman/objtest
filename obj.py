import random

class Player:
    def __init__(self,gender, health, name, defaultWeapon, credits):
        self.gender=gender
        self.health=health
        self.name=name
        self.defaultWeapon=defaultWeapon
        self.credits=credits
        print("Player Object Created",self.gender,self.health)

    def playerHurt(self,damage):
        self.health=self.health-damage
        print("Damage=",damage,"New self.health=",self.health)

    def healthString(self):
        if self.health >= 80: return "healthy"

        elif self.health >=70: return "Stable"

        elif self.health >=60: return "Weak"

        elif self.health >0: return "Critical"

        else: return "Dead"

    def isDead(self):
        if self.health<=0:
            return True
        else: 
            return False

    def attack(self,target):
        outcome=random.randint(1,2)
        if outcome==1:
            damage=random.randint(5,20)
            target.playerHurt(damage)
            print(self.name,"successfully attacked",target.name,"causing",damage,"damage")
        else:
            print(self.name,"attacked",target.name,"causing no damage - attack failed")

p1=Player("F",110,"Mary","axe",40)
p2=Player("M",100,"Chee","shotgun",89)
p3=Player("F",100,"Tamar","sword",98)
p1.playerHurt(20)
p2.playerHurt(10.5)

players=[p1,p2,p3]

for p in players:
    print(p.name,p.health,p.healthString())

# p1.attack(p2)
for i in range(6):
    combatants=random.sample(players,2)
    combatants[0].attack(combatants[1])
for i in players:
    print(i.name,i.healthString())