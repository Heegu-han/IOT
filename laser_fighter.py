from airforce import AirForce

class LaserFighter(AirForce):
    def __init__(self, weapon_num):
        self._laser_num = weapon_num

    def take_off(self):
        print("레이저 전투기가 이륙합니다.")

    def fly(self):
        print("레이저 전투기가 목적지로 날아갑니다.")

    def attack(self):
        for i in range(self._laser_num):
            print("레이저 발사")
        self._laser_num = 0

    def land(self):
        print("레이저 전투기가 착륙합니다.")
