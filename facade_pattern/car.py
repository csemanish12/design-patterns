from facade_pattern.IgnitionSystem import IgnitionSystem
from facade_pattern.dashboard import Dashboard
from facade_pattern.engine import Engine
from facade_pattern.fuel_tank import FuelTank


class Car:
    def __init__(self):
        self.ignition_system = IgnitionSystem()
        self.engine = Engine()
        self.fuel_tank = FuelTank()
        self.dashboard = Dashboard()

    @property
    def km_per_litre(self):
        return 17

    def consume_fuel(self, km):
        litres = min(self.fuel_tank.level, km / self.km_per_litre)
        self.fuel_tank.level -= litres

    def start(self):
        print("\nStarting...")
        self.dashboard.show()
        if self.ignition_system.produce_spark():
            self.engine.turn_on()
        else:
            print("Can't start. Faulty ignition system")

    def has_enough_fuel(self, km, km_per_litre):
        litres_needed = km / km_per_litre
        return self.fuel_tank.level > litres_needed

    def drive(self, km=100):
        print("\n")
        if self.engine.revs_per_minute > 0:
            while self.has_enough_fuel(km, self.km_per_litre):
                self.consume_fuel(km)
                print(f"Drove {km}km")
                print(f"{self.fuel_tank.level} of fuel still left")
        else:
            print(f"Can't drive. The engine is turned off")

    def park(self):
        print("\nParking...")
        self.dashboard.lights["handbrake"].is_on = True
        self.dashboard.show()
        self.engine.turn_off()

    def switch_fog_lights(self, status):
        print("\nSwitching {} fog lights...".format(status))
        boolean = True if status == "ON" else False
        self.dashboard.lights["fog"].is_on = boolean
        self.dashboard.show()

    def fill_up_tank(self):
        print("\nFuel tank filled up!")
        self.fuel_tank.level = 100