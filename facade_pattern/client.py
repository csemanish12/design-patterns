from facade_pattern.car import Car


def main():
    car = Car()
    car.start()
    car.drive()
    car.switch_fog_lights("ON")
    car.switch_fog_lights("OFF")
    car.park()
    car.fill_up_tank()
    car.drive()
    car.start()
    car.drive()
    car.park()


if __name__ == "__main__":
   main()