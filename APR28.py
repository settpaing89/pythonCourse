class Employee:
    def __init__(self, name, experience, hourly_rate):
        self.name = name
        self.experience = experience
        self.hourly_rate = hourly_rate

    def calculate_salary(self, hours_worked):
        salary = self.hourly_rate * hours_worked * 30  # calculating for a month
        tax_deduction = salary * 0.13

        if self.experience < 8:
            total_salary = salary
        elif self.experience >= 8 and self.experience <= 15:
            total_salary = salary + 5000
        else:
            total_salary = salary + 8000

        return total_salary - tax_deduction


name = input("Enter employee name: ")
experience = int(input("Enter employee experience (in years): "))
hourly_rate = float(input("Enter employee hourly rate: "))
hours_worked = int(input("Enter number of hours worked for a day: "))

emp = Employee(name, experience, hourly_rate)
salary = emp.calculate_salary(hours_worked)

print("Employee name:", emp.name)
print("Experience (in years):", emp.experience)
print("Hourly rate:", emp.hourly_rate)
print("Hours worked:", hours_worked)
print("Salary:", salary)
