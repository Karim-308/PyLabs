import json


class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, emp_id):
        for emp in self.employees:
            if emp.id == emp_id:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, emp_id):
        emp = self.get_employee(emp_id)
        if emp:
            self.employees.remove(emp)
            Office.employeesNum -= 1

    def deduct(self, emp_id, deduction):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary -= deduction

    def reward(self, emp_id, reward):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary += reward

    def check_lateness(self, emp_id, move_hour):
        emp = self.get_employee(emp_id)
        if emp:
            is_late = self.calculate_lateness(
                9, move_hour, emp.distance_to_work,
                emp.car.velocity if emp.car else 0
            )
            if is_late:
                self.deduct(emp_id, 10)
            else:
                self.reward(emp_id, 10)

    @staticmethod
    def calculate_lateness(target_hour, move_hour, distance, velocity):
        if velocity == 0:
            return True
        return move_hour + distance / velocity > target_hour

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num

    def to_dict(self):
        return {
            "name": self.name,
            "employeesNum": Office.employeesNum,
            "employees": [
                {
                    "id": e.id,
                    "name": e.name,
                    "email": e.email,
                    "salary": e.salary,
                    "mood": e.mood,
                    "health_rate": e.health_rate,
                    "car": e.car.name if e.car else None,
                    "distance_to_work": e.distance_to_work
                }
                for e in self.employees
            ]
        }

    def save_to_json(self, filename="office_data.json"):
        with open(filename, "w") as f:
            json.dump(self.to_dict(), f, indent=4)
