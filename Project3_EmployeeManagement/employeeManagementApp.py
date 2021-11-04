
class employee:
    
    def __init__(self, name, age, position) -> None:
        '''Initializes all employees with name, age, position attributes'''
        self.name = name
        self.age = age
        self.position = position
    
    def display_employees(listOfEmployees):
        '''Displays all employees in the company'''
        print()
        print("Employees in Dunder Mifflin are:")
        print()
        for item in listOfEmployees:
            print(item.name + ",", str(item.age) + ",", item.position)

    def allocate_department(listOfEmployees):
        '''Sorts all employees to departments and returns a list of departments'''
        allocatedList = []
        managementList = []
        salesList = []
        accountsList = []
        for employee in listOfEmployees:
            if employee.position == "Manager" or "Manager" in employee.position:
                managementList.append(employee)
            elif employee.position == "Salesperson" or "Salesperson" in employee.position:
                salesList.append(employee)
            elif employee.position == "Accountant" or "Accountant" in employee.position:
                accountsList.append(employee)
            else:
                pass
        allocatedList.append(managementList)
        allocatedList.append(salesList)
        allocatedList.append(accountsList)
        return allocatedList
    
    def display_department_employees(listOfDep):
        '''Displays employees in their departments'''
        print()
        print("The individual employees in each department are shown below:")
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
            
    def head_of_department(listOfDep):
        '''Finds max age and then sets employee as head'''
        for dep in listOfDep:
            max = 0
            for empl in dep:
                if empl.age > max:
                    max = empl.age
            for empl in dep:
                if max == empl.age:
                    empl.position = "Head " + empl.position
            
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
employee.head_of_department(employee.allocate_department(employeeList))
print("#####################################")
print("Head of department allocation done!!!")
print("#####################################")
employee.display_department_employees(employee.allocate_department(employeeList))
print()
