class FuelTank:
    def __init__(self, level=30):
        self.__level = level

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        self.__level = level

