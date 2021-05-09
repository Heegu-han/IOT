import car_module

class SportCar(car_module.Car):
    def __init__(self):
        super().__init__()
        self._color = "red"

    def accelerate(self):
        print("가속을 합니다")
        self._speed = self._speed + 40

    def turbo_charge(self):
        print("터보기능을 사용합니다.")
        self._speed = self._speed + 70

    def get_color(self):
        return self._color


