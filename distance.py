class distance:
    def __init__(self):
        self.count=0
    def get_distance(self):
        self.dis1=int(input("enter 1st distance in kms: "))
        self.dis2=int(input("enter 2nd distance in kms: "))
        self.count+=2

    def show_distance(self):
        print("distance 1:",self.dis1,"kms","and",self.dis1*1000,"mts")
        print("distance 2:",self.dis2,"kms","and",self.dis1*1000,"mts")
    def add_distance(self):
        result=self.dis1+self.dis2
        print("sum of given distances:",result," in kms","and",result*1000,"in mts")
d=distance()
d.get_distance()
d.show_distance()
d.add_distance()  