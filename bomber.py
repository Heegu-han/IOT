from airforce import AirForce

#폭격기 클래스
class Bomber(AirForce):
    def __init__(self,weapon_num):
        self._bomb_num = weapon_num

    def take_off(self):
        print("폭격기가 이륙합니다.")

    def fly(self):
        print("폭격기가 목적지로 날아갑니다.")

    def attack(self):
        for i in range(self._bomb_num):
            print("폭탄 투하")
        self._bomb_num = 0

    def land(self):
        print("폭격기가 착륙합니다.")
