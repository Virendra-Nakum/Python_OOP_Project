print("--- Python OOP Project: Employee Management System ---")
print()

class Employee :

    def __init__(self,employee_id= None,name= None,age = None,salary = None):
        self.__employee_id = employee_id
        self.name = name 
        self.age = age
        self.__salary = salary

    def set_id(self,employee_id):
        self.__employee_id = employee_id

    def get_id(self):
        return self.__employee_id        

    def Set_salary(self,salary):
        self.__salary  = salary

    def get_salary(self):
        return self.__salary

    def display(self):

        print(f"Employee name is {self.name}")
        print(f"Employee age is {self.age}")
        print(f"Employee ID is {self.__employee_id}")
        print(f"Employee salary : {self.__salary}")

    def __del__(self):
        pass

class Manager(Employee):

    def __init__(self, employee_id, name, age, salary,department):
        super().__init__(employee_id, name, age, salary)
        
        self.department = department

    def display(self):
        super().display()
        print(self.department)

class Developer(Employee):

    def __init__(self, employee_id, name, age, salary,programming_language):
        super().__init__(employee_id, name, age, salary)
        
        self.programming_language = programming_language

    def display(self):
        super().display()
        print(self.programming_language)

print(f"is Manager class is Sub class of Employee Class {issubclass(Manager,Employee)}")
print(f"is Developer class is Sub class of Employee Class {issubclass(Developer,Employee)}")


person = None
employee = None
manager = None

while True :
    print("--- Choice another opration ---")
    print()
    print("Choice An Operation")
    print("1. Create a Person ")
    print("2. Create an Employee ")
    print("3. Create a Manager ")
    print("4. Show Details ")
    print("5. Exit ")

    choice = int(input("Enter Your Choice:-"))

    if choice == 1 :
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))

        person = Employee(name=name,age= age)
        print(f"person Created with name :- {name} and Age :- {age}.")

    elif choice == 2 :
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        id = int(input("Enter Employee ID: "))
        salary = int(input("Enter Salary: "))

        employee = Employee(name,age,id,salary)
        print(f"Employee  created with name:- {name} ,age:- {age} ,ID:- {id} ,salary:- ${salary}.")

    elif choice == 3 :
        name = input("Enter Name :")
        age = int(input("Enter Age: "))
        id = int(input("Enter Employee ID: "))
        salary = int(input("Enter Salary: "))
        dept = input("Enter Department: ")

        manager = Manager(name,age,id,salary,dept)
        print(f"Manger created with name:- {name},age:- {age},ID:- {id},salary:- ${salary}, and  department:- {dept}.")


    elif choice == 4 :
        print("Choose Details To Show: ")
        print()
        print("1. Show Person")
        print("2. Show Employee")
        print("3. Show Manager")
        print()
        ch = int(input("Enter Choice :-"))
        if ch == 1 :
            if person is None :
                print("Data Not Found !")
            else:
                person.display()

        elif ch == 2 :
            if employee is None:
                print("Data Not Found")
            else:
                employee.display()

        elif ch == 3 :
            if manager is None :
                print("Data Not Found !")
            else:
                manager.display()

        else:
            print("Enter Valide Choice !")


    elif choice == 5 :
        print("Exiting the system. All resoures have been freed.")
        print("GoodBye!")
        break
        
    else:
        print("Enter Valide Choice !")


