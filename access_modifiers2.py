class Car:
    def __init__(self, price, speed, color):
        self._price = price
        self._speed = speed
        self._color = color

    def get_price(self):
        return self._price

    def set_price(self, value):
        self._price = value

    def get_speed(self):
        return self._speed

    def set_speed(self, value):
        self._speed = value

    def get_color(self):
        return self._color

    def set_color(self, value):
        self._color = value


if __name__ =="__main__":
    my_car = Car(2500, 30, "white")

    #my_car.set_price(2000)
    #my_car.set_speed(50)
    #my_car.set_color("blue")

    print("가격 :", my_car.get_price())
    print("색깔 :", my_car.get_color())
