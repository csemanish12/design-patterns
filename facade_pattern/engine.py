class Engine:
    def __init__(self):
        self.revs_per_minute = 0

    def turn_on(self):
        self.revs_per_minute = 2000

    def turn_off(self):
        self.revs_per_minute = 0