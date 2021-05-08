class Car:
    def __init__(self):
        self._speed = 0

    def get_speed(self):
        return self._speed

    def start(self):
        print("차가 출발합니다.")
        self._speed = 20

    def accelerate(self):
        print("차가 가속합니다.")
        self._speed = 50

    def stop(self):
        print("차가 멈춥니다.")
        self._speed = 0

if __name__ == "__main__":
    car = Car()
    print("속도 :", car.get_speed())
    car.start()
    print("속도 :", car.get_speed())
    car.accelerate()
    print("속도 :", car.get_speed())
    car.stop()
    print("속도 :", car.get_speed())
