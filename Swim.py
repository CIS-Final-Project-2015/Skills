<<<<<<< HEAD
=======
#Swim Skill
>>>>>>> 1ee1bc23eec4e359899f05dc6a753783dd5e5579
import random
class item(object):
    def __init__(self):
        self.value = 150.00
def Swim_Dcs(water, Dc):
    if water == "calm":
        print("The water is calm and easy to cross.")
        Dc=10
    elif water == "rough":
<<<<<<< HEAD
        print("The water is a bit rough but can still be crossed.\n")
=======
        print("The water is a bit rough but can still be crossed.")
>>>>>>> 1ee1bc23eec4e359899f05dc6a753783dd5e5579
        Dc=15
    else:
        print("The water is stormy, I wish you luck.")
        Dc=20
    return Dc
def SkillCheck(Dc):
    Verdict=""
    Roll = random.randint(1,41)
    if Roll >= Dc:
        Verdict = "Half-Speed"
    elif Roll >= Dc-4 and Roll < Dc:
        Verdict = "Quarter-Speed"
    else:
        Verdict ="Failure"
    return Verdict
#Swim Class
class Swim(object):
    def __init__(self):
        self.name="Swim"
        self.Dc=10
    def Skill_Check(self):
        Player=player()
        Verdict=SkillCheck(self.Dc)
        
class swim_speed(object):
    def __init__(self):
        playerspeed=1
        self.half_speed = playerspeed/2
        self.quarter_speed = playerspeed/4
        self.failure=playerspeed*0

<<<<<<< HEAD
=======
Dc=0
waterConditions=["calm","rough","stormy"]
water=waterConditions[random.randrange(0,3)]
Swim_Dcs(water, Dc)
SkillCheck(Dc)
    

>>>>>>> 1ee1bc23eec4e359899f05dc6a753783dd5e5579

