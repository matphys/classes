class point:
    def __init__(self,strk='0,0'):
        self.x=float(strk[:strk.index(',')])
        self.y=float(strk[strk.index(',')+1:])
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'
    def __add__(self,other):
        return point(str(self.x+other.x)+','+str(self.y+other.y))
    def __sub__(self,other):
        return point(str(self.x-other.x)+','+str(self.y-other.y))
A=Point(input())
B=Point(input())
print(A+B,A-B)
