class SportCar(object):
    def __init__(self):
        self._speed = 0

    def start(self):
        self._speed = 20

    def get_speed(self):
        return self._speed

    def accelerate(self):
        self._speed = self._speed + 40

    def turbo_charge(self):
        self._speed = self._speed + 70

    def stop(self):
        self._speed = 0

if __name__=="__main__":
    my_sport_car = SportCar()
    my_sport_car.start()
    print("속도 :",my_sport_car.get_speed())
    my_sport_car.accelerate()
    print("속도 :",my_sport_car.get_speed())
    my_sport_car.turbo_charge()
    print("속도 :",my_sport_car.get_speed())
    my_sport_car.stop()
    print("속도 :",my_sport_car.get_speed())
