from typing import AsyncGenerator


class employee:
    
    def __init__(self, name, age, position) -> None:
        self.name = name
        self.age = age
        self.position = position
    
    def display_employees(listOfEmployees):
        print()
        print("Employees in Dunder Mifflin are:")
        print()
        for item in listOfEmployees:
            print(item.name + ",", str(item.age) + ",", item.position)

    def allocate_department(listOfEmployees):
        allocatedList = []
        managementList = []
        salesList = []
        accountsList = []
        for employee in listOfEmployees:
            if employee.position == "Manager" or "Manager" in employee.position:
                managementList.append(employee)
            elif employee.position == "Salesperson":
                salesList.append(employee)
            elif employee.position == "Accountant":
                accountsList.append(employee)
            else:
                pass
        allocatedList.append(managementList)
        allocatedList.append(salesList)
        allocatedList.append(accountsList)
        return allocatedList
    
    def display_department_employees(listOfDep):
        print()
        print("The individual employees in each department are show below:")
        print("---------------------------------------------------------")
        print()
        n= 1
        for dep in listOfDep:
            if n == 1:
                print("Management:")
                print("-----------")
            elif n ==2:
                print("Salespersons:")
                print("-------------")
            else:
                print("Accountants:")
                print("------------")
            for empl in dep:
                print(empl.name + ",", str(empl.age) + ",", empl.position)
            print()
            n += 1


employeeList = []
employeeList.append(employee("Michael", 45, "Manager"))
employeeList.append(employee("Dwight", 40, "Assistant to the Manager"))
employeeList.append(employee("Jim", 35, "Manager"))
employeeList.append(employee("Pam", 30, "Receptionist"))
employeeList.append(employee("Angela", 32, "Accountant"))
employeeList.append(employee("Kevin", 42, "Accountant"))
employeeList.append(employee("Oscar", 40, "Accountant"))
employeeList.append(employee("Stanley", 55, "Salesperson"))
employeeList.append(employee("Phyllis", 45, "Salesperson"))
employeeList.append(employee("Andy", 38, "Salesperson"))
employeeList.append(employee("Ryan", 30, "Salesperson"))
employeeList.append(employee("Creed", 55, "Salesperson"))

employee.display_employees(employeeList)
employee.display_department_employees(employee.allocate_department(employeeList))
