class employee:
    def __init__(self, name, age, rank_ID):
        self.name = name
        self.age = age
        self.rank_ID = rank_ID

    def is_higher_rank(self, employee2):
        if (self.__eq__(employee2)) == True:
            return "These employees are both the same rank!"
        elif self.rank_ID < employee2.rank_ID:
            return (self.name+" is senior in rank than "+employee2.name+"!")
        else:
            return (employee2.name+" is senior in rank than "+self.name+"!")

    def __eq__(self, employee2):
        return (self.rank_ID == employee2.rank_ID)
    
    def __repr__(self):
        rep = ("Employee Name: "+str(self.name)+"\n"+"Age: "+str(self.age)+"\n"+"ID: "+str(self.rank_ID)+"\n")
        return rep

employee1 = employee("Michael", 45, 12345)
employee2 = employee("Dwight", 40, 23456)
employee3 = employee("Pam", 30, 34567)
employee4 = employee("Jim", 35, 12345)

print()
print(employee1)
print(employee2)
print(employee3)
print(employee4)

print(employee1.is_higher_rank(employee4))
print(employee3.is_higher_rank(employee2))
print(employee4.is_higher_rank(employee2))
print(employee4.is_higher_rank(employee3))
print()

def test_is_higher_rank():
    assert employee1.is_higher_rank(employee4) == 'These employees are both the same rank!', "Should be the same"
    assert employee3.is_higher_rank(employee2) == 'Dwight is senior in rank than Pam!', "Should be the Dwigth senior Pam"
    assert employee4.is_higher_rank(employee2) == 'Jim is senior in rank than Dwight!', "Should be Jim senior Dwight"
    assert employee4.is_higher_rank(employee3) == 'Jim is senior in rank than Pam!', "Should be Jim senior Pam"

test_is_higher_rank()
print("Everything Passed.")
print()