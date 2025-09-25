class Vectors:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2

    def __add__ (self,other):
        return Vectors(self.n1+other.n1,self.n2+other.n2)
    
    def __sub__(self,other):
        return Vectors(self.n1-other.n1,self.n2-other.n2)
    

    def __str__(self):
        return f"{self.n1}i+{self.n2} j"
    



s1=Vectors(78,98)
s2=Vectors(98,76)

s3=s1+s2
print(s3)

s4=s1-s2
print(s4)

    
