class DashboardLight:
    def __init__(self, is_on=False):
        self.__is_on = is_on

    def __str__(self):
        return self.__class__.__name__

    @property
    def is_on(self):
        return self.__is_on

    @is_on.setter
    def is_on(self, status):
        self.__is_on = status

    def status_check(self):
        if self.__is_on:
            print(f"{self}: ON")
        else:
            print(f"{self}: OFF")