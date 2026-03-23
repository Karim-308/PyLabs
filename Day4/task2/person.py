class Person:
    moods = ("happy", "tired", "lazy")

    def __init__(self, name, money=0, mood="happy", health_rate=100):
        self.name = name
        self.money = money
        self.mood = mood
        self.health_rate = health_rate

    @property
    def health_rate(self):
        return self._health_rate

    @health_rate.setter
    def health_rate(self, value):
        if 0 <= value <= 100:
            self._health_rate = value
        else:
            self._health_rate = max(0, min(100, value))

    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def eat(self, meals):
        if meals == 3:
            self.health_rate = 100
        elif meals == 2:
            self.health_rate = 75
        elif meals == 1:
            self.health_rate = 50

    def buy(self, items):
        self.money -= items * 10
