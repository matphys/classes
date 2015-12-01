
class Point:
    def __init__(self,stroka="0,0"):
        self.x = float(stroka[:stroka.index(",")])
        self.y = float(stroka[stroka.index(",")+1:])
    def __add__(self,other):
        return(str(self.x + other.x) + ','+str(self.y + other.y))
    def __str__(self):
        return('(' + str(self.x) + ',' + str(self.y)+')')
    def rast(self, other):
        return str((other.x +self.x)/2) + ',' + str((other.y + self.y)/2)
    def rast2(self, other):
        return ((self.x- other.x)**2 + (self.y-other.y)**2)**0.5
    def Plos(self,other,onemore):
        p = (self.rast2(other)+self.rast2(onemore)+other.rast2(onemore))/2
        return (p*(p-self.rast2(other))*(p-self.rast2(onemore))*(p - other.rast2(onemore)))**0.5
N=int(input())
A=[]
maximum=None
B=[Point()]*3
for i in range(N):
    A.append(Point(input()))
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if maximum==None or maximum<A[i].Plos(A[j],A[k]):
                B[0],B[1],B[2]=A[i],A[j],A[k]
                maximum=A[i].Plos(A[j],A[k])
print(*B)
