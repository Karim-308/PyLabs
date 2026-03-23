from car import Car
from employee import Employee
from office import Office

bmw = Car("bmw 320", fuel_rate=80, velocity=90)
fiat128 = Car("fiat 128", fuel_rate=100, velocity=60)

karim = Employee(
    "karim ibrahim", money=1000, mood="happy", health_rate=90,
    emp_id=1, car=bmw, email="karim@iti.com",
    salary=7000, distance_to_work=20
)

samy = Employee(
    "samy", money=500, mood="tired", health_rate=100,
    emp_id=2, car=fiat128, email="samy@iti.com",
    salary=5000, distance_to_work=15
)

iti = Office("ITI Smart Village")
iti.hire(karim)
iti.hire(samy)

print(f"all employees  {[e.name for e in iti.get_all_employees()]}")
print(f"total employees  {Office.employeesNum}")

karim.eat(2)
print(f"karim health after 2 meals  {karim.health_rate}")

karim.buy(3)
print(f"karim money after buying 3 items  {karim.money}")

karim.work(10)
print(f"karim mood after 10h work  {karim.mood}")

karim.sleep(7)
print(f"karim mood after 7h sleep  {karim.mood}")

samy.eat(1)
print(f"samy health after 1 meal  {samy.health_rate}")

samy.work(6)
print(f"samy mood after 6h work  {samy.mood}")

print(f"bmw fuel before drive  {bmw.fuel_rate}")
karim.drive(20)
print(f"bmw fuel after drive  {bmw.fuel_rate}")

karim.refuel(50)
print(f"bmw fuel after refuel  {bmw.fuel_rate}")

iti.check_lateness(1, 8)
print(f"karim salary after lateness check  {karim.salary}")

iti.check_lateness(2, 7)
print(f"samy salary after lateness check  {samy.salary}")

iti.fire(2)
print(f"employees after firing samy  {[e.name for e in iti.get_all_employees()]}")
print(f"total employees  {Office.employeesNum}")

iti.save_to_json()
print("saved to office_data.json")
