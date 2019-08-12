class basic_info:
    def get_info(self):
        self.name = input("Enter the name of the employee : ")
        self.id = input("Enter the employee ID : ")
        self.age = input("Enter the age of the employee : ")
        self.gender = input("Enter the gender of the employee : ")
    
class dept_info:
    def get_dept(self):
        self.dname = input("Enter the name of the department : ")
        self.work = input("Enter the assigned work : ")
        self.time = input("Enter the time of completion : ")
        
class Employee(basic_info,dept_info):
    def show_info(self):
        print("\nThe employee details are : ")
        print("Name : ",self.name)
        print("ID : ",self.id)
        print("Age : ",self.age)
        print("Gender : ",self.gender)
        print("Department Name : ",self.dname)
        print("Assigned work : ",self.work)
        print("Completion time : ",self.time)
        
e = Employee()
e.get_info()
e.get_dept()
e.show_info()