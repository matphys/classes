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
    def russt_do_0(self):
        return (self.x**2+self.y**2)**0.5
N=int(input())
maxx=None
for i in range(N):
    A=point(input())
    if maxx==None or A.russt_do_0()>maxx.russt_do_0():
        maxx=A
print(maxx)
