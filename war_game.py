from fighter import Fighter
from bomber import Bomber
from laser_fighter import LaserFighter

def war_game(airforce):
    airforce.take_off()
    airforce.fly()
    airforce.attack()
    airforce.land()

if __name__=="__main__":
    f15 = Fighter(3)
    war_game(f15)
    b29 = Bomber(3)
    war_game(b29)
    l75 = LaserFighter(5)
    war_game(l75)
