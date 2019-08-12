class student:
    def get_student(self):
        self.name=input("enter student name:")
        self.srn=input("enter student srn:")
        self.gender=input("enter student gender")

    def show_student(self):
        print("student details are:")
        print("Name is:",self.name)
        print("SRN is:",self.srn)
        print("Gender is:",self.gender)

class stud_res(student):
    def get_marks(self):
        self.mark1=int(input("enter ADA marks:"))
        self.marks2=int(input("enter CN marks:"))
        self.marks3=int(input("enter DBMS marks:"))
        self.marks4=int(input("enter Python marks:"))
        self.marks5=int(input("enter IDS marks:"))
    def get_result(self):
        print("ISA marks:\n")
        print("enter marks out of 60:")
        self.get_marks()
        self.total=self.mark1+self.marks2+self.marks3+self.marks4+self.marks5
        self.score=self.total/300
        print("ESA marks:\n")
        print("enter marks out of 100")
        self.get_marks()
        self.total1=self.mark1+self.marks2+self.marks3+self.marks4+self.marks5
        self.score1=self.total1/500
        self.sgpa=((self.score*6)+(self.score*4))
    def show_result(self):
            print("ISA marks are:",self.total)
            print("ESA marks are:",self.total1)
            print("SGPA is :",self.sgpa)
s=stud_res()
s.get_student()
s.show_student()
s.get_result()
s.show_result()

