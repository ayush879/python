class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return point(x,y)
    def __It__(self,other):
        self_mag=(self.x**2)+(self.y**2)
        other_mag=(other.x**2)+(other.y**2)
        return self_mag<other_mag
p1=point(4,-3)
p2=point(-1,2)
print(p1+p2)
print((1,1) > (-2,-3))

