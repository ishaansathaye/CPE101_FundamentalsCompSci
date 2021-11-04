from typing import AsyncGenerator


class employee:
    
    def __init__(self, name, age, position) -> None:
        self.name = name
        self.age = age
        self.position = position
    
    def display_employees(listOfEmployees):
        print("Employees in Dunder Mifflin are:")
        print()
        for item in listOfEmployees:
            print(item.name + ",", str(item.age) + ",", item.position)

    def allocate_department(self, listOfEmployees):
        self.allocatedList = []
        managementList = []
        salesList = []
        accountsList = []
        for item in listOfEmployees:
            if item.position == "Manager" or "Manager" in item.position:
                managementList.append(item)
            elif item.position == "Salesperson":
                salesList.append(item)
            elif item.position == "Accountant":
                accountsList.append(item)
            else:
                pass
        self.allocatedList.append(managementList)
        self.allocatedList.append(salesList)
        self.allocatedList.append(accountsList)
        return self.allocatedList
    
    def display_department_employees(self):
        pass

print()
employeeList = []
employeeList.append(employee("Michael", 45, "Manager"))
employeeList.append(employee("Dwight", 40, "Assistant to the Manager"))
employeeList.append(employee("Jim", 45, "Manager"))
employeeList.append(employee("Pam", 45, "Receptionist"))
employeeList.append(employee("Angela", 45, "Accountant"))
employeeList.append(employee("Kevin", 45, "Accountant"))
employeeList.append(employee("Oscar", 45, "Accountant"))
employeeList.append(employee("Stanley", 45, "Salesperson"))
employeeList.append(employee("Phyllis", 45, "Salesperson"))
employeeList.append(employee("Andy", 45, "Salesperson"))
employeeList.append(employee("Ryan", 45, "Salesperson"))
employeeList.append(employee("Creed", 45, "Salesperson"))

employee.display_employees(employeeList)
