            ## Employee Management System

class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary
        

    def annual_salary(self):
        return self.monthly_salary * 12 


    def increase_salary (self, percent):
        if percent < 0:
            print("Percentage must be positive.")
            return
        self.monthly_salary =  self.monthly_salary + (percent * self.monthly_salary) / 100


    def compare(self, other_employee):
        if self.monthly_salary > other_employee.monthly_salary:
            return f"{self.name} has a higher salary than {other_employee.name}."
        elif self.monthly_salary < other_employee.monthly_salary:
            return f"{other_employee.name} has a higher salary than {self.name}."
        return f"{self.name} and {other_employee.name} have the same salary."

    
    def __str__ (self):
        return (
            f"Name: {self.name}\n"
            f"Monthly Salary: {self.monthly_salary:,.2f}\n"
            f"Annual Salary: {self.annual_salary():,.2f}"
        )
    
employee1= Employee("Fiona", 4500)
employee2= Employee("Ian", 5200)

print ("----- Employee Management System -----")

while True:
    print()

    mode = input(
        "1. View Employee Details\n"
        "2. Increase Salary\n"
        "3. Compare Employees\n"
        "Q. Quit\n"
        "Choose an option: "
    ).lower()

    print()
    if mode == "q":
        break

    if not mode.isdigit() or int(mode) not in [1, 2, 3]:
        print("Invalid option.")
        continue

        # view employee details

    if mode == "1":
        view_employee = input ("Which employee do you want to view? (Fiona/Ian): ").lower()
        if view_employee == "fiona":
            print (employee1)
        elif view_employee == "ian":
            print (employee2)
        else:
            print("Employee not found.")

    elif mode == "2":
        add_to_employee = input ("Which employee do you want to add money to their salary? (Fiona/Ian): ").lower()
        try:
            percent = float(input("Enter the percentage to add to the salary: "))
        except ValueError:
            print("Invalid number.")
            continue

        if add_to_employee == "fiona":
            employee1.increase_salary(percent)
            print(f"New monthly salary for {employee1.name}: {employee1.monthly_salary}")
        elif add_to_employee == "ian":
            employee2.increase_salary(percent)
            print(f"New monthly salary for {employee2.name}: {employee2.monthly_salary}")
    elif mode == "3":
        print(employee1.compare(employee2))
    else:
        print("Invalid option.")

