#import car_module
from car_module import Car

if __name__=="__main__":
    my_car = Car()
    my_car.start()
    my_car.accelerate()
    print("속도:",my_car.get_speed())
    my_car.stop()
    print("속도:",my_car.get_speed())
