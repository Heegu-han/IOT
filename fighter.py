from airforce import AirForce

#전투기 클래스
class Fighter(AirForce):
    def __init__(self,weapon_num):
        self._missile_num = weapon_num

    def take_off(self):
        print("전투기가 이륙합니다.")

    def fly(self):
        print("전투기가 목적지로 날아갑니다.")

    def attack(self):
        for i in range(self._missile_num):
            print("미사일 발사")
        self._missile_num = 0

    def land(self):
        print("전투기가 착륙합니다.")
