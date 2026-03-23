import re
from person import Person


class Employee(Person):
    def __init__(self, name, money=0, mood="happy", health_rate=100,
                 emp_id=None, car=None, email="", salary=1000, distance_to_work=20):
        super().__init__(name, money, mood, health_rate)
        self.id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distance_to_work = distance_to_work

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value >= 1000:
            self._salary = value
        else:
            self._salary = 1000

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value == "" or re.match(r"[^@]+@[^@]+\.[^@]+", value):
            self._email = value
        else:
            self._email = ""

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self, distance):
        if self.car:
            self.car.run(self.car.velocity or 60, distance)

    def refuel(self, gas_amount=100):
        if self.car:
            self.car.fuel_rate += gas_amount

    def send_mail(self, to, subject, msg, receiver_name):
        with open(f"{subject.replace(' ', '_')}.txt", "w") as f:
            f.write(f"From: {self.email}\nTo: {to}\n\n")
            f.write(f"Hi, {receiver_name}\n{msg}\nthanks\n")
