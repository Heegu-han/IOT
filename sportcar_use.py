import sportcar_module

if __name__=="__main__":
    my_sportcar = sportcar_module.SportCar()
    my_sportcar.start()
    my_sportcar.accelerate()
    print("속도:",my_sportcar.get_speed())
    my_sportcar.turbo_charge()
    print("속도:",my_sportcar.get_speed())
    my_sportcar.stop()
    print("색상:",my_sportcar.get_color())
