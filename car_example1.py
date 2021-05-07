class Car:
    def __init__(self):
        self._speed=0

    def get_speed(self):
        return self._speed
    def start(self):
        self._speed=20
        print("자동차가 출발합니다.")

    def accelerate(self):
        self._speed=self._speed+30
        print("자동차가 가속합니다.")

    def stop(self):
        self._speed=0
        print("자동차가 멈춥니다.")

if __name__=="__main__":
    my_car=Car()
    my_car.start()
    print("속도:",my_car.get_speed())
    my_car.accelerate()
    print("속도:",my_car.get_speed())
    my_car.stop()
    print("속도:",my_car.get_speed())
    
