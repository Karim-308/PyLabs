class Car:
    def __init__(self, name, fuel_rate=100, velocity=0):
        self.name = name
        self.fuel_rate = fuel_rate
        self.velocity = velocity

    @property
    def fuel_rate(self):
        return self._fuel_rate

    @fuel_rate.setter
    def fuel_rate(self, value):
        self._fuel_rate = max(0, min(100, value))

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        self._velocity = max(0, min(200, value))

    def run(self, velocity, distance):
        self.velocity = velocity
        traveled = 0
        while traveled < distance:
            if self.fuel_rate <= 0:
                self.stop(distance - traveled)
                return
            step = min(10, distance - traveled)
            traveled += step
            if step == 10:
                self.fuel_rate -= 10
        self.stop(0)

    def stop(self, remaining=0):
        self.velocity = 0
        if remaining > 0:
            print(f"car stopped, out of fuel. {remaining} km remaining")
        else:
            print("arrived at destination")
